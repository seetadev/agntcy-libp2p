### Libp2p team's Recent Technical Contributions to AGNTCY

### Overview

@seetadev in collaboration with @johannamoran has recently been contributing at the intersection of **AGNTCY's agent networking architecture and libp2p**, with a focus on strengthening the underlying peer-to-peer layer, improving transport architecture, documenting upgrade paths, and bringing stronger observability and interoperability practices into the ecosystem.

The work spans **architecture, implementation, testing, observability, and protocol engagement**, helping connect libp2p capabilities with concrete AGNTCY requirements.

### 1. AGNTCY–libp2p Technical Deep Dive

We have developed a dedicated **AGNTCY ↔ libp2p deep dive** documenting how libp2p can support AGNTCY's networking requirements and identifying relevant architectural, transport, and operational considerations.

This provides a technical reference for the AGNTCY community and helps map libp2p capabilities to concrete AGNTCY requirements.

- [AGNTCY–libp2p Deep Dive](https://github.com/seetadev/agntcy-libp2p/tree/main/agntcy-libp2p-deep-dive)

### 2. AGNTCY DIR Architecture and libp2p Usage

We have contributed to the **AGNTCY Directory working-group discussions** around improving the architecture and usage of libp2p within DIR.

The work considers the networking layer more holistically, including:

- Kademlia/DHT and peer discovery
- PubSub/GossipSub
- Transport architecture
- Separation of application and networking concerns
- More modular composition of networking components

- [Improving libp2p architecture and usage in AGNTCY](https://github.com/agntcy/dir/discussions/1968###discussioncomment-17895496)

### 3. Greenfield Networking Redesign

Manu contributed a **greenfield redesign proposal** for the AGNTCY networking architecture, with an emphasis on simplifying the networking abstraction and making transport choices more modular.

A key theme is establishing a cleaner separation between application/protocol concerns and the underlying transport and peer-to-peer networking layer.

- [Greenfield redesign discussion](https://github.com/agntcy/dir/discussions/1895###discussioncomment-17906464)

### 4. Go-stream Transport Work

The **gostream-test pull request was merged**, demonstrating a common gRPC service behind a transport abstraction.

The work explores a common service interface across multiple transports, including libp2p gostream, and provides a practical reference for a **transport seam** that avoids coupling the application service directly to a single networking mechanism.

- [gostream-test PR ###1](https://github.com/tkircsi/gostream-test/pull/1)

This is particularly relevant to AGNTCY because it provides a clearer boundary between application/service protocols and the networking substrate.

### 5. AGNTCY Dependency Issue Resolution

Tibor and Manu have discussed on an issue resolved through an upstream fix in `ugorji/go`.

This represents a concrete contribution at the dependency level, helping address an underlying issue affecting the AGNTCY stack.

- [upstream ugorji/go fix](https://github.com/ugorji/go/commit/1077c6675e84b0a70b6b4a68afe5a42fb9242f59)

### 6. Mapping Recent libp2p Releases to AGNTCY

We prepared a detailed analysis of **recent go-libp2p release features relevant to AGNTCY**.

Rather than treating the release as a generic dependency upgrade, the analysis maps relevant libp2p improvements to AGNTCY requirements and identifies areas where newer capabilities can strengthen the platform.

- [go-libp2p upgrade analysis for AGNTCY](https://github.com/seetadev/agntcy-libp2p/blob/main/agntcy-libp2p-deep-dive/go-libp2p-upgrade.md)

### 7. Testing and Observability

A complementary area of the work is connecting **network architecture with measurable operational behavior**.

Manu has been working around CSIT testing, peer-to-peer observability, and standardized measurement artifacts so that networking decisions can be evaluated through evidence and repeatable measurements.

- [AGNTCY CSIT Test Reports](https://agntcy.github.io/csit/)
- [Luminar – p2p observability](https://luminar-6rlv.onrender.com/)

The broader observability work also includes:

- [Observability WG meeting slides](https://tinyurl.com/Observability-WG-meeting)
- [Observability WG reference guide](https://tinyurl.com/Observability-WG-References)
- [Composable Trust Blueprint and VTO Documentation](https://tinyurl.com/Composable-Trust-Blueprint)

### 8. IETF 126 Technical Engagement

We also presented **two technical contributions at IETF 126 in Vienna**, extending the work beyond the AGNTCY/libp2p implementation itself into broader protocol, trust, telemetry, and observability discussions.

The associated observability material provides additional technical context for the measurement and trust architecture.

### Overall Contribution

Taken together, Manu's recent AGNTCY work is not limited to **using libp2p as a dependency**. It is focused on helping shape **how libp2p can be integrated, abstracted, tested, upgraded, and observed within an Internet-of-Agents environment**.

The contribution can be viewed across three complementary layers:

### Architecture → Implementation → Evidence

**Architecture**
- AGNTCY/libp2p deep dive
- DIR networking improvements
- Greenfield networking redesign
- Transport abstraction and modularity

**Implementation**
- gostream transport seam
- libp2p upgrade analysis
- Upstream dependency issue resolution

**Evidence and Observability**
- AGNTCY CSIT testing
- P2P observability through Luminar
- VTO / Composable Trust work
- IETF 126 technical presentations

Together, these efforts provide a stronger foundation for **peer discovery, Kademlia/DHT, PubSub/GossipSub, transport flexibility, interoperability, and production-grade observability** in AGNTCY.

They also help establish a clearer path for libp2p to serve as a reusable networking substrate for the **Internet of Agents**.
