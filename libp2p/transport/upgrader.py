import logging
from typing import Union

from libp2p.abc import (
    IMuxedConn,
    ISecureConn,
    IUpgradeableConn,
)
from libp2p.custom_types import (
    TMuxerOptions,
    TSecurityOptions,
)
from libp2p.peer.id import (
    ID,
)
from libp2p.protocol_muxer.exceptions import (
    MultiselectClientError,
    MultiselectError,
)
from libp2p.protocol_muxer.multiselect import (
    DEFAULT_NEGOTIATE_TIMEOUT,
)
from libp2p.security.exceptions import (
    HandshakeFailure,
)
from libp2p.security.security_multistream import (
    SecurityMultistream,
)
from libp2p.stream_muxer.muxer_multistream import (
    MuxerMultistream,
)
from libp2p.transport.exceptions import (
    MuxerUpgradeFailure,
    NoSecureUpgradationProtocolFound,
    SecurityUpgradeFailure,
)

logger = logging.getLogger(__name__)


class TransportUpgrader:
    security_multistream: SecurityMultistream
    muxer_multistream: MuxerMultistream

    def __init__(
        self,
        secure_transports_by_protocol: TSecurityOptions,
        muxer_transports_by_protocol: TMuxerOptions,
        negotiate_timeout: int = DEFAULT_NEGOTIATE_TIMEOUT,
    ):
        self.security_multistream = SecurityMultistream(secure_transports_by_protocol)
        self.muxer_multistream = MuxerMultistream(
            muxer_transports_by_protocol, negotiate_timeout
        )

    async def upgrade_security(
        self,
        raw_conn: IUpgradeableConn,
        is_initiator: bool,
        peer_id: ID | None = None,
    ) -> Union[ISecureConn, IMuxedConn]:
        """Upgrade conn to a secured connection."""
        if isinstance(raw_conn, IMuxedConn) and raw_conn.provides_security:
            logger.info(
                "Raw connection already provides inbuilt security, " \
                "skipping security upgrade"
            )
            return raw_conn

        if isinstance(raw_conn, ISecureConn):
            logger.info(
                "Raw connection already provides security, skipping security upgrade"
            )
            return raw_conn
        try:
            if is_initiator:
                if peer_id is None:
                    raise ValueError("peer_id must be provided for outbout connection")
                secure_conn = await self.security_multistream.secure_outbound(
                    raw_conn, peer_id
                )
                # Validate the authenticated peer ID matches the expected peer ID.
                authenticated_peer_id = secure_conn.get_remote_peer()
                if authenticated_peer_id != peer_id:
                    await secure_conn.close()
                    raise SecurityUpgradeFailure(
                        f"Peer ID mismatch: expected {peer_id}, "
                        f"got {authenticated_peer_id}"
                    )
                return secure_conn
            return await self.security_multistream.secure_inbound(raw_conn)
        except (MultiselectError, MultiselectClientError) as error:
            raise SecurityUpgradeFailure(
                "failed to negotiate the secure protocol"
            ) from error
        except HandshakeFailure as error:
            raise SecurityUpgradeFailure(
                "handshake failed when upgrading to secure connection"
            ) from error

    async def upgrade_connection(self, conn: IUpgradeableConn,
                                  peer_id: ID) -> IMuxedConn:
        """Upgrade secured connection to a muxed connection."""
        if isinstance(conn, IMuxedConn) or conn.provides_muxing:
            logger.info(
                "Connection already provides inbuilt muxing, skipping muxer upgrade"
            )
            return conn

        if not isinstance(conn, ISecureConn) and not conn.provides_security:
            # If the connection provides neither negotiated nor inbuilt security,
            # we cannot upgrade it to a muxed connection.
            raise NoSecureUpgradationProtocolFound(
                "connection is not secure, cannot upgrade to muxed connection"
            )
        try:
            return await self.muxer_multistream.new_conn(conn, peer_id)
        except (MultiselectError, MultiselectClientError) as error:
            raise MuxerUpgradeFailure(
                "failed to negotiate the multiplexer protocol"
            ) from error
