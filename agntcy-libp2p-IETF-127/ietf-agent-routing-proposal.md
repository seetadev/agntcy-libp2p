### Request for IETF Side Meeting: Decentralized Agent Routing, Discovery, and Transport (DART)

**Proposed Working Group / Discussion Group Focus Area:** Internet Area / Routing Area
**Meeting Type:** IETF Side Meeting (Proposed BoF / Dispatch)
**Estimated Duration:** 1.5 Hours

---

### 1. Abstract
As autonomous Artificial Intelligence (AI) agents scale from single-framework local deployments to global, multi-institutional systems, they present a novel networking paradigm: standardizing how distributed agents discover peers, verify capability claims, and exchange state across administrative boundaries. High-level agentic protocols like the Model Context Protocol (MCP) and Agent-to-Agent (A2A) establish structured JSON-RPC or request-response conventions for tool invocation and high-precision task execution. However, they lack a decentralized network-routing substrate, relying on hard-coded locations and centralized registries.

This proposal outlines an architectural roadmap for standardizing a **Gossip-Enhanced Agentic Coordination Layer (GEACL)** and a topology-independent **Agent Identity URI Scheme (`agent://`)** at the IETF. By decoupling naming from location and layering a stochastic gossip-based metadata substrate beneath structured RPC protocols, the proposed framework establishes a scalable, zero-trust, and transport-agnostic infrastructure for internet-scale agent collaboration.

---

### 2. Problem Statement & IETF Context

### 2.1 The Location-Bound Identity Flaw
Modern multi-agent systems (MAS) rely on URI schemes where agent identity is bound to physical network locations (e.g., `https://agents.acme.com/approver`). This creates immediate fragility:
- **Migration & Churn:** When agents migrate cloud providers, scale horizontally, or redeploy, physical endpoints change, breaking upstream workflows and disrupting auditability.
- **Conflation of Name and Address:** Following Saltzer’s classic name-address separation principle, names should identify entities, addresses should locate them, and routes should specify how to reach them. Present architectures conflate all three.

### 2.2 Centralization & Discovery Bottlenecks
Directory services and discovery systems (e.g., FIPA Directory Facilitator or proprietary index registries) introduce single points of failure, scale poorly across organizations, and create administrative bottlenecks. We require a decentralized discovery mechanism where peer lookup and capability verification can be performed over global overlays without a single central registry.

### 2.3 The Semantic-Relational Substrate Gap
High-level application-layer protocols (MCP, A2A, ACP) operate on a strictly synchronous, directed, point-to-point model. While highly secure and deterministic for direct actions, they are inefficient for ambient context propagation (e.g., background load signaling, discovery of newly evolved agent tools, task advertising, and cooperative failure detection). The network needs a background metadata sync layer that continuously aligns state while minimizing explicit network queries.

---

### 3. Proposed DART Architecture Reference Model

To resolve these boundaries, we propose a four-layer reference stack that cleanly separates application-level reasoning from network-level transport, aligning directly with standard IETF primitives.

```text
+-----------------------------------------------------------------------+
|                               Agent Layer                             |
|    - Autonomous Task Executors, Planners, Tool-Using Clients          |
+-----------------------------------------------------------------------+
                                  │
                                  ▼  (MCP / A2A / ACP Message Schemes)
+-----------------------------------------------------------------------+
|                       Structured Protocol Layer                       |
|    - High-level JSON-RPC, directed messaging, tool registries         |
+-----------------------------------------------------------------------+
                                  │
                                  ▼  (Background Sync, Discovery, URIs)
+-----------------------------------------------------------------------+
|             Gossip-Enhanced Agentic Coordination Layer (GEACL)        |
|    - agent:// URI Naming & DHT Key Derivation                         |
|    - Epidemic Dissemination Engine (G1)                               |
|    - Peer Sampling (G2) & Semantic State Store (G3)                   |
|    - Anti-Entropy Reconciler (G4) & Priority Relevance Filter (G5)     |
+-----------------------------------------------------------------------+
                                  │
                                  ▼  (Transport Bindings: QUIC, WebRTC)
+-----------------------------------------------------------------------+
|                      Transport and Network Layer                      |
|    - P2P Links (libp2p), Local Wireless Mesh, Hybrid Cloud Routing   |
+-----------------------------------------------------------------------+
```

### 3.1 Layer Interactions
The DART stack does not act as a synchronous pipeline; instead, the layers operate concurrently.
1. **Background Metadata State:** The **Gossip-Enhanced Layer (GEACL)** runs a continuous, low-overhead background loop over transport-agnostic overlays (like libp2p Kademlia DHTs or GossipSub). It propagates ambient discovery records, capability updates, and health signals.
2. **Intent & Tools:** When an agent decides to act (informed by the background world-view), it utilizes the **Structured Protocol Layer** (MCP, A2A) to perform a direct, authenticated, high-precision request-response tool call.
3. **Transport Independence:** Standardizing these primitives at the GEACL level ensures they run natively over any transport, including TCP, UDP, QUIC, WebRTC, or ad-hoc local wireless meshes.

---

### 4. Key Standardization Targets

### 4.1 Topology-Independent Identity: The `agent://` URI Scheme
We propose standardizing the `agent://` URI scheme to formalize topology-independent naming and capability-based discovery.

#### 4.1.1 URI Grammar (ABNF)
```abnf
agent-uri       = "agent://" trust-root "/" capability-path "/" agent-id [ "?" query ] [ "#" fragment ]
trust-root      = host [ ":" port ]
capability-path = path-segment *31( "/" path-segment )
path-segment    = 1*64( LOWER / DIGIT / "-" )
agent-id        = agent-prefix "_" type-suffix
agent-prefix    = type-class *( "_" type-modifier )
type-class      = "llm" / "rule" / "human" / "composite" / "sensor" / "actuator" / "hybrid" / extension-class
type-suffix     = first-char 25base32char
```

#### 4.1.2 Key Mechanics
- **Trust Root:** Establishes organizational authority (DNS-based) and serves as the public key publication point (`/.well-known/agent-keys.json`).
- **Capability Path:** Hierarchical categorization enabling prefix matching (e.g., `/workflow/approval/invoice` matches a query for `/workflow/approval`).
- **Agent ID:** A K-sortable TypeID backed by a UUIDv7 suffix, providing creation-time ordering and global uniqueness without central coordination.

### 4.2 Distributed Discovery & DHT Key Derivation
To enable decentralized lookup without central registries, DART leverages a Kademlia-style Distributed Hash Table (DHT). The DHT lookup key is derived deterministically from the canonical trust root and capability path:

```text
$$\text{key} = \text{SHA256}(\text{canonical}(\text{trust\_root}) \parallel \text{"/"} \parallel \text{canonical}(\text{cap\_path}))$$
```

This derivation ensures:
- **Trust-Root Scoping:** Preventing cross-organizational pollution; queries return records explicitly scoped to trusted administrative authorities.
- **Exact & Prefix Routing:** A query at an ancestor path (e.g., `/workflow`) retrieves all descendant registrations materialized on the Kademlia nodes, ensuring efficient capability discovery in $O(\log N)$ hops.

### 4.3 Cryptographically Verifiable Claims (PASETO Attestations)
To prevent DHT poisoning and malicious capability claims, agents must register with the network using cryptographically signed attestation tokens.
- **Format:** Platform-Agnostic SEcurity Tokens (PASETO v4.public) backed by Ed25519 signatures.
- **Verification Constraints:** Verifiers fetch the trust root's public key from the well-known HTTPS endpoint, ensuring that:
  - The token is not expired.
  - The issuer matches the canonical URI authority.
  - Every listed capability matches or is a descendant of the agent's identity path.
  - Optional audience constraints (`aud`) are enforced to restrict token replays during highly sensitive transactions.

```text
  [Issuer (Trust Root)] ──(Issues PASETO)──> [Agent A] ──(Presents Token & URI)──> [Verifier]
          │                                                                           │
          └─────────────────(GET /.well-known/agent-keys.json)────────────────────────┘
```

### 4.4 Epidemic Dissemination and Gossip Mechanics
Standardizing the wire protocols for Gossip-Enhanced Agentic Coordination Layer (GEACL) exchanges:
- **Push-Pull Gossip:** Standardizing how agents stochastically select peers to exchange compressed state vectors, intentions, and capability metadata.
- **Anti-Entropy State Reconciliation:** Specifying CRDT-style merge rules and vector clocks to allow localized representation models to gradually align on global background states without central consensus.
- **Priority and Relevance Filtering:** Defining context-aware suppression mechanisms where critical event signals (high severity) propagate aggressively, while routine telemetry is throttled to prevent network congestion.

---

### 5. Suggested Side Meeting Agenda

**Co-Chairs:** [Proposed: Representatives from AGNTCY Project, libp2p community, and IETF Internet Area]

| Time | Duration | Topic | Speaker |
| :--- | :--- | :--- | :--- |
| 13:00 | 10 Min | **Welcome, Agenda Bashing, and Context Setting** | Co-Chairs |
| 13:10 | 20 Min | **Problem Statement: Decentralized Naming and Routing Gaps in MAS** | Luca Muscariello / Vijoy Pandey |
| 13:30 | 25 Min | **Technical Deep Dive: The `agent://` URI Grammar & DHT Key Derivation** | Roland R. Rodriguez, Jr. |
| 13:55 | 20 Min | **GEACL & Gossip Substrates: Layering Epidemic Protocols Beneath A2A/MCP** | Mansura Habiba / Nafiul I. Khan |
| 14:15 | 15 Min | **Open Floor & Charter Discussion: Is there IETF interest for a DART WG?** | All |

---

### 6. Target Deliverables for a Future Working Group
1. **RFC (Standards Track):** The `agent://` URI Scheme for Multi-Agent Systems.
2. **RFC (Standards Track):** Kademlia-based DHT capability mapping, registration, and key derivation protocols.
3. **RFC (Standards Track):** PASETO Profile for Cryptographic Agent Attestation.
4. **RFC (Informational):** Gossip-Enhanced Agentic Coordination Layer (GEACL) Architecture & Hybrid Stack Integration.
