# libp2p × SLIM HTTP Transport Gateway Specification

**Status:** Draft
**Date:** 6 October 2026

## Abstract

This specification defines an HTTP Transport Gateway for the AGNTCY Internet of Agents that enables HTTP-based applications and agent protocols to communicate over **SLIM and libp2p-based networks**.

The gateway provides an interoperability boundary between conventional HTTP services and decentralized agent communication infrastructure. It maps HTTP requests, responses, streaming semantics, metadata, and authenticated identities onto SLIM sessions and libp2p transports while preserving the application semantics required by HTTP clients.

The specification is designed to support heterogeneous agent ecosystems in which agents may communicate using HTTP, A2A-compatible protocols, SLIM, libp2p, or combinations of these technologies. The gateway therefore separates **application protocol semantics**, **agent messaging**, and **network transport**, allowing each layer to evolve independently.

A conforming implementation MUST support HTTP interoperability and SHOULD support SLIM as the primary agent messaging interface. It MAY expose the same gateway over one or more libp2p transports.

## 1. Scope

This specification defines:

1. discovery of HTTP services exposed through a libp2p/SLIM gateway;
2. mapping between HTTP requests/responses and SLIM messages;
3. establishment and management of authenticated sessions;
4. binding of HTTP and agent identities to SLIM and libp2p identities;
5. streaming and multiplexing of HTTP traffic;
6. protocol and capability discovery;
7. authorization and policy enforcement at the gateway boundary;
8. error and connection semantics;
9. interoperability between HTTP-native, SLIM-native, and libp2p-native agents.

This specification does **not** define a new HTTP protocol, a replacement for SLIM, or a replacement for libp2p. Instead, it specifies how these technologies can be composed into an interoperable transport gateway for agentic systems.

## 2. Design Principles

The gateway is designed around the following principles.

### 2.1 HTTP compatibility

Existing HTTP clients and services SHOULD be usable without requiring them to implement libp2p or SLIM.

### 2.2 Transport independence

Application protocols SHOULD NOT depend on a particular underlying libp2p transport. TCP, QUIC, WebTransport, or other supported libp2p transports MAY be used.

### 2.3 Agent identity separation

HTTP authentication, agent identity, SLIM identity, and libp2p Peer ID are distinct concepts. Implementations MUST NOT assume that they are equivalent.

Where an authenticated binding exists, the gateway SHOULD provide an explicit and verifiable relationship between these identities.

### 2.4 Decentralized operation

A gateway SHOULD NOT require a centralized broker for peer discovery, routing, or communication.

### 2.5 Capability-based interoperability

The gateway SHOULD expose protocol capabilities so that an agent can determine which operations, message types, streaming modes, and security mechanisms are supported before establishing application communication.

### 2.6 Resilience

Gateway implementations SHOULD tolerate intermittent connectivity, peer changes, connection migration, and transport failures where supported by the underlying SLIM and libp2p implementation.

### 2.7 Explicit trust boundaries

The gateway is a security boundary between HTTP and the decentralized network. Implementations MUST define which identity, authorization, routing, and policy decisions are performed locally and which are delegated to SLIM or the underlying libp2p network.

## 3. Architectural Model

A conforming deployment consists of three logical layers:

```text
┌───────────────────────────────────────────────┐
│             Agent Applications                │
│                                               │
│       HTTP / A2A / AGNTCY protocols           │
└───────────────────────┬───────────────────────┘
                        │
                        │ HTTP
                        ▼
┌───────────────────────────────────────────────┐
│          HTTP Transport Gateway               │
│                                               │
│  protocol mapping • identity • policy        │
│  streaming • capability discovery             │
└───────────────────────┬───────────────────────┘
                        │
                        │ SLIM
                        ▼
┌───────────────────────────────────────────────┐
│                  SLIM                         │
│                                               │
│       agent messaging / sessions / routing    │
└───────────────────────┬───────────────────────┘
                        │
                        │ libp2p
                        ▼
┌───────────────────────────────────────────────┐
│             libp2p Network                    │
│                                               │
│ identity • discovery • multiplexing           │
│ transport • connectivity • peer networking    │
└───────────────────────────────────────────────┘
```

The logical layers MAY be implemented by separate processes or combined into a single implementation.

## 4. Gateway Roles

A gateway MAY operate in one or more of the following roles.

### 4.1 HTTP Ingress Gateway

Accepts HTTP requests from HTTP-native clients and forwards them through SLIM/libp2p to an agent or service.

### 4.2 HTTP Egress Gateway

Receives requests from SLIM/libp2p and exposes them as HTTP requests to an HTTP-native service.

### 4.3 Bidirectional Gateway

Supports both ingress and egress operation.

### 4.4 Agent Gateway

Associates HTTP requests with an authenticated agent identity and applies agent-level authorization and policy before forwarding the request.

### 4.5 Relay Gateway

Provides connectivity between otherwise non-directly-connected HTTP and SLIM/libp2p endpoints.

A relay gateway MUST NOT implicitly acquire authority to act as the requesting agent unless that authority has been explicitly delegated.

## 5. Protocol Discovery

A gateway SHOULD expose protocol capabilities using a well-known resource.

A deployment MAY expose:

```text
/.well-known/libp2p/protocols
```

and:

```text
/.well-known/slim/protocols
```

The libp2p resource identifies protocols reachable through the libp2p HTTP interface.

The SLIM resource identifies SLIM-facing application protocols, message types, and gateway capabilities.

An implementation MAY combine these capabilities into a single discovery document where appropriate.

Example:

```json
{
  "protocols": {
    "/slim/http/1.0": {
      "path": "/",
      "streaming": true,
      "authentication": ["peer-id", "agent"],
      "methods": ["GET", "POST"]
    }
  }
}
```

The exact protocol identifier MUST be registered or otherwise uniquely defined before interoperability claims are made.

## 6. HTTP-to-SLIM Mapping

The gateway maps an HTTP request to a SLIM message.

At minimum, the mapping MUST preserve:

* HTTP method;
* request target;
* relevant headers;
* request body;
* content type;
* correlation identifier;
* authentication context where applicable.

A gateway MUST NOT silently discard application-significant metadata.

The response MUST preserve, where representable:

* HTTP status;
* response headers;
* content type;
* response body;
* streaming state;
* correlation identifier.

## 7. Streaming

HTTP streaming MAY be mapped onto a persistent SLIM session.

Implementations SHOULD support incremental transmission rather than requiring the complete HTTP request or response body to be buffered.

For long-lived agent interactions, implementations SHOULD use correlation identifiers that allow multiple concurrent HTTP exchanges to share a single SLIM/libp2p connection.

## 8. Identity Binding

The gateway MUST distinguish between:

* HTTP authentication identity;
* agent identity;
* SLIM identity;
* libp2p Peer ID.

When multiple identities are bound together, the gateway SHOULD expose sufficient authenticated metadata for the receiving party to verify the binding.

For example:

```text
Agent ID
   │
   ├── authenticated by HTTP credential
   │
   ├── bound to SLIM session
   │
   └── associated with libp2p Peer ID
```

A Peer ID alone MUST NOT be interpreted as authorization to perform an application-level agent operation.

## 9. Authorization and Policy

The gateway SHOULD support policy enforcement before forwarding an HTTP request into the SLIM/libp2p network.

Policy MAY consider:

* agent identity;
* destination;
* protocol;
* HTTP method;
* resource;
* message type;
* capability;
* delegation;
* session;
* rate limits;
* resource limits.

A gateway MUST NOT infer authorization solely from network reachability.

## 10. Error Semantics

Transport failures, authentication failures, authorization failures, routing failures, and application errors SHOULD remain distinguishable.

The gateway SHOULD map SLIM and libp2p failures to appropriate HTTP status and error metadata without incorrectly representing a transport failure as an application-level response.

Where possible, implementations SHOULD provide machine-readable error information.

## 11. Security Considerations

The gateway is an explicit trust boundary.

Implementations MUST consider:

* authentication;
* authorization;
* identity binding;
* replay protection;
* message integrity;
* confidentiality;
* capability delegation;
* request smuggling;
* header manipulation;
* resource exhaustion;
* connection flooding;
* unauthorized relaying;
* cross-agent impersonation.

A gateway MUST NOT assume that a trusted HTTP connection implies a trusted downstream agent.

Similarly, possession of a libp2p Peer ID MUST NOT by itself grant application-level authority.

## 12. Resilience Considerations

A primary objective of this gateway architecture is to allow HTTP-native applications to benefit from the resilience properties of decentralized networking.

Implementations SHOULD support:

* reconnect;
* peer migration;
* connection retry;
* multiple routes;
* transport fallback;
* bounded buffering;
* backpressure;
* cancellation;
* idempotency where applicable;
* detection of stale sessions.

Applications SHOULD be able to distinguish between:

```text
application failure
transport failure
peer failure
gateway failure
policy rejection
```

This distinction is particularly important for autonomous agents that may need to retry, reroute, delegate, or select an alternative service.

## 13. AGNTCY Interoperability

The gateway is intended to provide a common transport boundary for heterogeneous agent systems.

An AGNTCY deployment MAY therefore contain:

```text
HTTP Agent
    │
    ▼
HTTP Gateway
    │
    ▼
SLIM
    │
    ▼
libp2p
    │
    ├── SLIM Agent
    ├── libp2p Agent
    └── HTTP Gateway → HTTP Agent
```

This architecture permits incremental adoption.

An existing HTTP agent does not need to become a libp2p implementation merely to participate in a decentralized agent network.

Conversely, a native SLIM/libp2p agent does not need to expose a public HTTP endpoint merely to communicate with HTTP-based applications.

## 14. Conformance

A conforming implementation MUST:

1. expose the defined HTTP gateway semantics;
2. correctly map HTTP requests and responses;
3. preserve correlation between requests and responses;
4. implement the required SLIM session semantics;
5. correctly handle authentication and authorization boundaries;
6. distinguish transport and application failures;
7. prevent unauthorized forwarding or impersonation.

Optional capabilities SHOULD be advertised through protocol discovery.

## 15. Future Extensions

Future versions MAY define standardized mappings for:

* A2A;
* agent discovery;
* capability exchange;
* delegated authorization;
* content-addressed payloads;
* IPFS/IPLD resources;
* offline message delivery;
* durable agent sessions;
* multi-path routing;
* policy-aware routing;
* telemetry and verifiable execution records.

These extensions SHOULD remain independent of the underlying libp2p transport wherever possible.
