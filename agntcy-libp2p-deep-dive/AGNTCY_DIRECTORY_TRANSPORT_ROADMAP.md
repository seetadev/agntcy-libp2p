# AGNTCY Directory Transport Seam: Roadmap, NAT Traversal, and Integration

## Overview

The `gostream-test` repository provides a useful and timely proof of concept for the **Transport seam** proposed as part of the AGNTCY Directory redesign.

The core idea is simple and powerful:

> **Keep the Directory API/service contract independent from the underlying transport.**

The same generated gRPC service can operate over:

* `bufconn` — local, in-process
* UDS — local, persistent daemon
* TCP + mTLS — remote, enterprise/networked
* libp2p over TCP — remote/federation
* libp2p over QUIC — remote/federation

This creates a clean architectural boundary:

```text
Application / Directory API
            │
            ▼
      gRPC service
            │
            ▼
     Transport seam
            │
    ┌───────┼────────┬──────────┬────────────┐
    ▼       ▼        ▼          ▼            ▼
 bufconn   UDS   TCP + mTLS  libp2p/TCP  libp2p/QUIC
```

The important property is that everything above the seam can use the generated Directory service without needing to know whether the connection is local, enterprise, overlay-based, relayed, or fully P2P.

This is a strong foundation for taking AGNTCY from local development and demos toward **federation, enterprise deployments, edge environments, CGNAT, mobile networks, and real customer applications**.

---

## Why the Transport Seam Matters

The transport abstraction allows us to separate:

1. **Directory/service semantics**
2. **Authentication and authorization**
3. **Application logic**
4. **Network connectivity**
5. **NAT traversal and reachability**
6. **Deployment topology**

The application should ideally be able to say:

```text
I need to communicate with this AGNTCY service.
```

without needing to decide:

```text
Should I use TCP?
QUIC?
libp2p?
Relay?
Hole punching?
Tailscale?
UDS?
```

That decision should be made by the transport/deployment layer.

This becomes particularly important for the Internet of Agents, where an agent can move between a laptop, enterprise VPN, Kubernetes cluster, edge device, home network, CGNAT, or mobile network without the application itself needing to change.

---

# Proposed Roadmap

I would suggest developing this incrementally, with small, independently reviewable PRs.

## Milestone 1 — Transport Seam Validation

### Goals

* Stabilize the proto/service contract.
* Validate `bufconn`, UDS and TCP+mTLS.
* Validate libp2p gostream over TCP.
* Validate libp2p gostream over QUIC.
* Establish common lifecycle and error semantics.
* Add unit and integration tests.

### Outcome

A single Directory service should be demonstrably transport-independent.

```text
DirService
   │
   └── Transport
        ├── bufconn
        ├── UDS
        ├── TCP + mTLS
        ├── libp2p/TCP
        └── libp2p/QUIC
```

---

# Milestone 2 — Production libp2p Transport

The next phase should harden the libp2p implementation for real deployments.

### Areas to cover

* Stable peer identity.
* Protocol ID/version negotiation.
* QUIC as a preferred modern transport where appropriate.
* Connection manager integration.
* Resource manager integration.
* Context cancellation.
* Graceful shutdown.
* Reconnection.
* Transient network failure handling.
* Connection lifecycle management.
* Stream lifecycle management.
* Interoperability testing.

The goal is to move from a runnable proof of concept toward a reusable AGNTCY transport implementation.

---

# Milestone 3 — NAT Traversal and Edge Connectivity

This should be a major milestone rather than an implementation detail.

AGNTCY agents will often **not have globally routable IP addresses**.

We should explicitly validate scenarios such as:

```text
Agent → CGNAT → Internet → Team Server
```

```text
Mobile Agent → Mobile VPN → CGNAT → Relay → AGNTCY Peer
```

```text
Agent A → NAT → DCUtR → Direct Agent B
```

and:

```text
Agent A → NAT
         ↓
      Relay
         ↓
      Agent B
```

The objective is not simply to demonstrate that libp2p can traverse NAT. We should validate the complete connectivity lifecycle:

```text
Reachability detection
        ↓
Relay reservation
        ↓
Hole-punch attempt
        ↓
Direct connection
        ↓
Relay fallback if required
```

This is where **AutoNAT, Circuit Relay v2 and DCUtR** become particularly important.

The proposed team-server architecture is a natural fit for this model: public infrastructure can provide bootstrap, relay, delegated routing and related services while individual agents remain private and outbound-oriented.

---

# CGNAT and Mobile VPN Test Matrix

A dedicated NAT traversal test matrix would be valuable.

| Environment                 | Expected connectivity                |
| --------------------------- | ------------------------------------ |
| Public ↔ Public             | Direct QUIC/TCP                      |
| Private NAT ↔ Public        | Direct outbound                      |
| NAT ↔ NAT                   | DCUtR / hole punching                |
| Difficult NAT ↔ NAT         | Relay fallback                       |
| CGNAT ↔ Public              | Outbound / relay                     |
| CGNAT ↔ CGNAT               | Hole-punch attempt + relay fallback  |
| Mobile network ↔ Enterprise | Relay / policy-dependent direct path |
| Mobile VPN ↔ Internet       | VPN path / libp2p traversal          |
| Mobile VPN + CGNAT          | Relay fallback should remain viable  |
| Edge node ↔ Team server     | Outbound libp2p connection           |

The key success criterion is:

> **AGNTCY should remain usable even when an agent does not have a globally routable IP address.**

---

# Milestone 4 — Directory Federation

Once the transport layer is reliable, we can build toward federation:

```text
Slim node
    ↓
Team server
    ↓
Directory index
    ↓
Provider discovery
    ↓
Direct / relay data path
```

And eventually:

```text
Team A ↔ Team B ↔ Team C
```

This is where delegated routing and federated indexing become increasingly interesting.

The transport layer should allow these components to communicate without coupling the Directory semantics to one particular network topology.

---

# Milestone 5 — Customer and Application Validation

The architecture should be validated against real AGNTCY applications rather than only synthetic transport demos.

Two useful perspectives are:

* **Spellguard.ai** — a customer-oriented deployment perspective.
* **coffee-sdk-app** — a developer/application integration perspective.

## Spellguard.ai

For a customer such as Spellguard.ai, we should consider realistic deployment environments:

* corporate NAT;
* CGNAT;
* Kubernetes;
* outbound-only firewalls;
* corporate VPN;
* mobile VPN;
* edge deployments;
* private networks;
* restricted enterprise environments.

A customer should not necessarily need to expose a public gRPC endpoint for every agent.

Instead, we should be able to support:

```text
Agent
  ↓
libp2p identity
  ↓
Outbound connection / relay / hole punching
  ↓
Authenticated peer
```

while preserving the same Directory API.

## coffee-sdk-app

The `coffee-sdk-app` demo provides an important developer-experience test.

Ideally, an application should be able to interact with the Directory without knowing whether the remote service is reachable through:

* TCP;
* QUIC;
* libp2p;
* relay;
* DCUtR;
* an overlay network;
* or another transport.

The application should simply use the Directory API.

This makes the Transport seam a genuine developer-experience improvement rather than merely an internal abstraction.

---

# Proposed PR Strategy

I would like to contribute **incremental PRs** around this initiative as the design develops.

Rather than introducing one large implementation PR, I suggest keeping the work modular and reviewable.

### PR 1 — Transport seam

* Stabilize `Transport`.
* Clarify lifecycle semantics.
* Clarify cancellation and errors.
* Keep generated Directory APIs transport agnostic.

### PR 2 — libp2p transport

* gostream over TCP.
* gostream over QUIC.
* Peer identity.
* Protocol negotiation.
* Connection lifecycle.

### PR 3 — NAT traversal

* AutoNAT.
* Circuit Relay v2.
* DCUtR.
* Relay fallback.
* Reachability state.

### PR 4 — Federation

* Slim → team server.
* Team server → team server.
* Delegated routing.
* Provider discovery.
* Record retrieval.

### PR 5 — Observability

* Transport metrics.
* Peer lifecycle.
* Connection lifecycle.
* Stream lifecycle.
* Relay/direct-path visibility.
* AGNTCY/OpenTelemetry correlation.

### PR 6 — Interoperability and integration

* Multi-node tests.
* NAT test matrix.
* TCP/QUIC interoperability.
* Reconnect scenarios.
* Customer/application validation.

This incremental approach should allow architectural assumptions to be reviewed continuously rather than attempting to finalize everything upfront.

---

# Tailscale, WireGuard and Overlay Networks

The `tsnet` exploration is also interesting.

I would not frame this as **libp2p versus Tailscale**. They solve overlapping but different problems.

### libp2p

* P2P application networking.
* Peer identity.
* Protocol negotiation.
* Discovery and routing.
* Relay and hole punching.
* Decentralized federation.
* P2P application protocols.

### WireGuard / Tailscale / other overlays

* Managed private networks.
* Organizational identity and ACLs.
* Stable private addressing.
* Enterprise network integration.
* Managed connectivity.

There may be environments where an overlay network provides the underlay and libp2p provides the application-level P2P layer.

For example:

```text
Agent
  ↓
Tailscale / WireGuard overlay
  ↓
libp2p
  ↓
AGNTCY protocol
  ↓
Directory / Agent
```

Or, where an overlay is unavailable:

```text
Agent
  ↓
libp2p QUIC
  ↓
AutoNAT
  ↓
DCUtR
  ↓
Relay
  ↓
Remote Agent
```

Again, the important property is that the **AGNTCY application does not need to care**.

---

# Observability

Another important future area is making the Transport seam observable.

An AGNTCY trace could eventually expose:

```text
coffee-sdk-app
    ↓
Directory lookup
    ↓
Peer discovered
    ↓
QUIC connection attempted
    ↓
AutoNAT state
    ↓
Relay reservation
    ↓
DCUtR attempted
    ↓
Direct connection established
    ↓
gRPC / gostream stream opened
    ↓
Directory operation
    ↓
Response
```

Or, in a more challenging environment:

```text
Spellguard agent
    ↓
CGNAT detected
    ↓
Relay selected
    ↓
Direct upgrade attempted
    ↓
Direct path unavailable
    ↓
Relay maintained
    ↓
Request completed
```

This would make it much easier for developers and customers to understand **why an agent interaction is slow or failing**.

It also creates a natural bridge into AGNTCY observability and OpenTelemetry.

A future goal could be a common **Agent + Network Observability model** that correlates:

```text
Agent
  +
Peer
  +
Protocol
  +
Connection
  +
Transport
  +
Relay / NAT traversal
  +
Tool / API invocation
```

into a single end-to-end trace.

---

# Proposed Success Criteria

I suggest measuring the initiative against concrete outcomes.

### Transport

* [ ] Same Directory API works across local, enterprise and P2P transports.
* [ ] Applications do not depend on a specific transport.
* [ ] libp2p TCP and QUIC federation works reliably.
* [ ] Transport implementations remain independently testable.

### NAT / Connectivity

* [ ] Common NAT configurations are tested.
* [ ] Relay fallback works when direct connectivity fails.
* [ ] CGNAT scenarios are tested.
* [ ] Mobile network scenarios are tested.
* [ ] Mobile VPN scenarios are tested.
* [ ] Mobile VPN + CGNAT scenarios are tested.
* [ ] AutoNAT reachability is observable.
* [ ] DCUtR/hole punching is validated.
* [ ] Connections recover cleanly after network changes.

### Security

* [ ] Stable peer identity is maintained.
* [ ] Communication is authenticated.
* [ ] Protocol versioning is explicit.
* [ ] Authorization is implemented above the transport layer.
* [ ] Resource limits and abuse controls are considered.

### Applications / Customers

* [ ] `coffee-sdk-app` works without transport-specific application logic.
* [ ] A realistic Spellguard.ai scenario can operate without exposing a public endpoint for every agent.
* [ ] Enterprise/VPN deployment scenarios are validated.
* [ ] Edge deployment scenarios are validated.

### Observability

* [ ] Transport events are measurable.
* [ ] Peer/connection/stream lifecycle is observable.
* [ ] Direct vs relay connectivity is visible.
* [ ] NAT traversal state is observable.
* [ ] Network events can be correlated with AGNTCY/OpenTelemetry traces.

---

# Longer-Term Direction

The Transport seam could eventually become more than an implementation detail.

It could provide the foundation for:

1. **Agent-native peer networking**
   Agent capabilities becoming inputs to peer selection and connection establishment.

2. **Federated Directory + federated routing**
   Multiple organizational directories exchanging signed records without requiring one global registry.

3. **Network-aware agent scheduling**
   Selecting agents based on capability, latency, locality, reachability, resource availability and network cost.

4. **Edge-first agents**
   Agents running behind NAT/firewalls on devices, clusters and private networks while remaining discoverable and reachable.

5. **Network-level policy**
   Policies such as:

   * only communicate with agents from a particular organization;
   * prefer local/edge agents;
   * avoid public relays for sensitive workloads;
   * require specific transport/security properties.

6. **Agent-aware observability**
   Correlating application traces, agent/tool calls and libp2p network events.

7. **Adaptive transport selection**
   Selecting QUIC, TCP, relay, WebRTC, overlay or other connectivity based on the environment.

8. **Agent networking trust/reputation**
   Combining peer identity, signed capabilities, provider records, historical behaviour and policy.

9. **Privacy-preserving discovery**
   Discovering capabilities without unnecessarily exposing organizational metadata or network topology.

10. **Standards and edge collaboration**
    Using implementation experience from AGNTCY and libp2p to inform emerging networking and edge requirements.

---

# Review and Collaboration

I would suggest an iterative process for this initiative:

```text
Design
  ↓
Small implementation PR
  ↓
Integration test
  ↓
Review
  ↓
Benchmark / validation
  ↓
Merge
  ↓
Next milestone
```

I would be happy to contribute PRs and participate in reviews, particularly around:

* libp2p protocol boundaries;
* gostream;
* QUIC;
* peer identity;
* AutoNAT;
* Circuit Relay v2;
* DCUtR;
* resource and connection management;
* protocol versioning;
* stream lifecycle;
* NAT/CGNAT behaviour;
* interoperability;
* observability.

---

# Conclusion

The combination of the **Transport seam + libp2p + NAT traversal + federation + observability** can provide AGNTCY with a strong networking foundation for both current demos and real customer deployments.

The key architectural property is that AGNTCY applications should not have to choose between **local, enterprise, overlay, edge and P2P networking**.

Instead, we should provide a common service contract and allow the deployment environment to determine the appropriate transport.

That becomes particularly powerful for the Internet of Agents, where the same agent may move between a laptop, corporate VPN, Kubernetes cluster, edge environment, CGNAT or mobile network — without requiring the application to be redesigned around its current network topology.

I would be happy to **share PRs incrementally, help define and refine the milestones and roadmap, and participate in reviews and interoperability testing**, particularly around the libp2p transport and NAT traversal pieces.

The goal should be a transport layer that is **simple for application developers, robust for enterprise and edge deployments, and genuinely P2P when the environment allows it**.

Excited about this direction and looking forward to developing it further. 🚀
