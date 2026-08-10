### AGNTCY, libp2p & Content Addressing (CID) – Frequently Asked Questions

> This FAQ is intended for community, marketing, ecosystem, developer relations, product, and engineering teams. It explains how AGNTCY leverages libp2p and Content Identifiers (CIDs), why these technologies were chosen, and how they support a secure, interoperable agent ecosystem.

---

### What is AGNTCY?

AGNTCY is an open ecosystem for discovering, connecting, and coordinating AI agents across organizations and infrastructure providers.

Rather than operating as a centralized marketplace, AGNTCY provides protocols and infrastructure that enable agents to communicate, discover one another, and exchange capabilities securely.

Its architecture is designed to support deployments ranging from individual developers to enterprise environments while remaining interoperable across different AI frameworks.

---

### What is libp2p?

libp2p is an open-source, modular networking framework for building distributed applications.

It provides reusable networking building blocks such as:

* Peer identity
* Secure encrypted communication
* Peer discovery
* Distributed routing
* Publish/Subscribe messaging
* NAT traversal
* Connection management
* Multiple transport protocols

Instead of every distributed application implementing networking independently, libp2p provides these capabilities as a shared foundation.

Today, libp2p powers many large-scale decentralized systems across storage, blockchain, networking, and distributed computing.

---

### Why does AGNTCY use libp2p?

Building distributed networking infrastructure is difficult.

AGNTCY focuses on agent interoperability, identity, and coordination—not low-level networking.

libp2p already solves many networking challenges, including:

* Secure communication
* Distributed discovery
* Identity management
* Routing
* Messaging
* Connectivity across different network environments

Using libp2p allows AGNTCY to build on mature, battle-tested networking components instead of reinventing them.

---

### What role does libp2p play within AGNTCY?

Within the current architecture, libp2p provides the networking layer that enables participating nodes to discover and communicate with one another.

This includes:

* Creating peer identities
* Connecting peers
* Advertising available content
* Discovering providers
* Retrieving metadata
* Broadcasting updates

In other words, libp2p enables the decentralized communication fabric on which AGNTCY operates.

---

### Is libp2p an AI framework?

No.

libp2p is not an AI framework or an agent protocol.

Instead, it provides networking capabilities that applications—including AI agent platforms—can build upon.

Just as web applications rely on TCP/IP and HTTP, distributed agent platforms can rely on libp2p for secure peer-to-peer networking.

---

### Does AGNTCY replace libp2p?

No.

The two projects operate at different layers.

libp2p provides networking primitives.

AGNTCY builds agent protocols, discovery mechanisms, and higher-level services on top of those networking capabilities.

The relationship is complementary rather than competitive.

---

### What is a Peer ID?

Every libp2p node has a cryptographic identity called a Peer ID.

A Peer ID allows nodes to:

* Authenticate one another
* Build secure encrypted connections
* Establish trusted communication
* Participate in decentralized discovery

Unlike IP addresses, Peer IDs remain stable across changing network environments.

---

### What is the Kad-DHT?

Kad-DHT (Kademlia Distributed Hash Table) is the decentralized discovery protocol used by libp2p.

It enables nodes to locate:

* peers
* providers
* published records

without relying on centralized infrastructure.

Within AGNTCY, the DHT acts as the discovery backbone for distributed agent metadata.

---

### What is GossipSub?

GossipSub is libp2p's Publish/Subscribe protocol.

Instead of every node polling for updates, peers subscribe to topics and receive announcements when new information becomes available.

Within AGNTCY this enables efficient propagation of newly published records.

---

### What is libp2p RPC?

After discovering another peer, additional metadata often needs to be retrieved.

Rather than storing everything inside the DHT, AGNTCY retrieves detailed information directly from peers using libp2p RPC.

This keeps the DHT lightweight while enabling richer metadata exchange.

---

### What is a Content Identifier (CID)?

A Content Identifier (CID) is an immutable identifier that uniquely represents content.

Unlike traditional URLs, which point to a location, CIDs identify the content itself.

If the content changes, its CID changes.

This provides:

* integrity
* reproducibility
* verifiability
* immutability

---

### Why are CIDs important?

Content-addressing offers several important benefits:

* Immutable references
* Content verification
* Efficient caching
* Decentralized retrieval
* Elimination of duplicate content

For distributed agent systems, this means metadata can be verified regardless of where it is retrieved.

---

### Does AGNTCY store everything on IPFS?

Not necessarily.

The current implementation primarily uses IPFS concepts, particularly:

* Content Identifiers (CIDs)
* Multihashes
* Content addressing

Artifacts themselves may reside in OCI registries or other storage systems.

The CID provides a stable, verifiable reference to that content.

---

### How does discovery work?

A simplified discovery flow is:

```text
Agent publishes metadata
        │
        ▼
Metadata receives a CID
        │
        ▼
CID advertised via Kad-DHT
        │
        ▼
Peers discover provider
        │
        ▼
RPC retrieves metadata
        │
        ▼
Secure communication begins
```

This separates discovery from metadata retrieval, improving scalability.

---

### Why not use a centralized database?

Centralized systems introduce challenges such as:

* Single points of failure
* Vendor lock-in
* Limited federation
* Operational bottlenecks

Decentralized discovery enables multiple organizations to participate while retaining control of their own infrastructure.

---

### Can AGNTCY support enterprise deployments?

Yes.

The architecture supports hybrid deployments combining:

* cloud infrastructure
* private data centers
* on-premises deployments
* decentralized peer-to-peer networking

Organizations can choose the deployment model that best meets their operational requirements.

---

### What is meant by hybrid networking?

Hybrid networking combines centralized services with decentralized communication.

For example:

* centralized authentication
* decentralized discovery
* private infrastructure
* public networking
* enterprise gateways
* peer-to-peer messaging

This allows organizations to adopt decentralized technologies incrementally.

---

### How does libp2p improve interoperability?

Many agent ecosystems are emerging simultaneously.

Rather than every ecosystem implementing a different networking protocol, libp2p provides a common transport layer beneath higher-level protocols.

This allows different ecosystems to communicate without requiring identical implementations.

---

### Can libp2p support multiple agent protocols?

Yes.

libp2p is application agnostic.

Multiple protocols can operate simultaneously over the same networking layer, including:

* AGNTCY protocols
* SLIM
* MCP
* A2A
* custom enterprise protocols

This enables protocol innovation without replacing the networking infrastructure.

---

### Why is observability important?

Distributed systems are difficult to operate without visibility into network behavior.

Observability helps answer questions such as:

* Why can't peers connect?
* Is the DHT healthy?
* How long do lookups take?
* Which transports are being negotiated?
* Are announcements propagating?
* Are peers reachable?

These insights improve both reliability and operational efficiency.

---

### What kinds of observability could be explored?

Potential areas include:

### Network Layer

* Connection success rate
* Peer churn
* Relay utilization
* DHT latency
* Routing paths
* NAT diagnostics
* Resource consumption

### Application Layer

* Agent discovery latency
* Metadata retrieval
* RPC performance
* Publication propagation
* Federation health
* Request tracing

Together these provide end-to-end visibility across the agent network.

---

### What research opportunities exist?

Potential collaboration areas include:

* Semantic discovery
* Capability-aware routing
* Trust-aware routing
* Locality-aware peer selection
* Intelligent caching
* Identity interoperability
* Cross-network federation
* Network observability
* Developer tooling
* Performance benchmarking

These represent opportunities for continued collaboration between the AGNTCY and libp2p communities.

---

### How can the libp2p community contribute?

There are many opportunities for collaboration, including:

* Networking expertise
* Transport improvements
* Routing research
* Observability tooling
* Cross-implementation testing
* Performance optimization
* Documentation
* Developer experience
* Security reviews
* Community support

As AGNTCY continues to evolve, collaboration with the broader libp2p ecosystem can help strengthen both projects.

---

### How can the AGNTCY community contribute to libp2p?

AGNTCY provides valuable real-world workloads for libp2p.

Feedback from production deployments can help improve:

* discovery protocols
* routing efficiency
* messaging performance
* operational tooling
* deployment practices
* interoperability testing

Open collaboration benefits both communities.

---

### Where can I learn more?

### AGNTCY

* [https://github.com/agntcy](https://github.com/agntcy)
* [https://agntcy.org](https://agntcy.org)

### libp2p

* [https://libp2p.io](https://libp2p.io)
* [https://github.com/libp2p](https://github.com/libp2p)

### IPFS

* [https://ipfs.tech](https://ipfs.tech)

### Custom Specifications

* libp2p Specifications
* Kademlia DHT
* GossipSub
* Multiaddresses
* Multiformats
* Content Identifiers (CID)

---

### A Shared Vision

The AGNTCY and libp2p communities share a common goal: enabling secure, interoperable, and decentralized communication across distributed systems.

By combining robust networking primitives from libp2p with AGNTCY's work on agent identity, discovery, and coordination, developers can build AI systems that are scalable, resilient, and capable of operating across organizational and infrastructure boundaries. Together, these technologies help lay the foundation for an open, federated ecosystem for autonomous agents.
