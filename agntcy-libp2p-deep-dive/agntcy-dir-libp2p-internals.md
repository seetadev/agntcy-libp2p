### Inside a Production Agent Discovery Pipeline: How AGNTCY Built Its Directory on libp2p

In the last post, we made the case for a shared networking layer across Internet of Agents projects. This one is the proof.

We are going under the hood of [AGNTCY's Agent Directory Service (ADS)](https://github.com/agntcy/dir) and walking through how it uses libp2p to publish, discover, verify, and retrieve agent metadata across a decentralized network.

This is not a theoretical architecture. It is running today, and it provides a useful reference for teams evaluating whether to build agent discovery on a decentralized networking layer.

If you want to jump straight into the implementation, visit the [AGNTCY DIR GitHub repository](https://github.com/agntcy/dir), the [Directory service](https://dir.agntcy.org/), or the [DIR Quick Start Guide](https://dir.agntcy.org/dir/dir-quickstart/).

## The architecture at a glance

AGNTCY's Directory service combines several libp2p components, each responsible for a specific part of the discovery problem.

| Component | Purpose |
| --- | --- |
| libp2p Host | Peer identity and secure networking |
| Kademlia DHT | Distributed peer and content discovery |
| GossipSub | Announcement propagation |
| RPC | Metadata and trust information retrieval |
| Peer IDs | Cryptographic node identity |
| Multiaddresses | Reachable network addresses |
| CID | Immutable content identifier |

Each component does one job well, and together they form a complete discovery pipeline.

One important clarification: AGNTCY uses the CID format from the multiformats ecosystem, but Directory nodes do **not** participate in the public IPFS DHT. Directory nodes form their own DHT network.

This distinction matters when thinking about who can discover or resolve records in the Directory network.

We also generally refer to these as **Directory nodes** or **Agent Directory Service (ADS) nodes**, rather than "DIR nodes."

## The discovery flow, end to end

At a high level, the pipeline looks like this:

```text
OCI Registry
      │
      ▼
   Artifact
      │
      ▼
     CID
      │
      ├─────────────────────────────┐
      │                             │
      ▼                             ▼
Provider Discovery             Content Discovery
"Who has this CID?"            "What CIDs match
                                these attributes?"
      │                             │
      └──────────────┬──────────────┘
                     ▼
               Kademlia DHT
                     │
                     ▼
              Peer Discovery
                     │
                     ▼
                 libp2p RPC
                     │
          ┌──────────┴──────────┐
          ▼                     ▼
   Metadata Retrieval     Trust Information
                              │
                    Signature / Public Key /
                     Security Scan Results
```

Let's walk through it step by step.

## Peer identity

Every Directory node is a libp2p peer with a cryptographic identity, a Peer ID, transport configuration, and multiaddresses.

This is the foundation everything else builds on.

Unlike an IP address, a Peer ID provides a stable identity even as a node moves across different network environments. That matters for a network where nodes can come and go and operate across different organizations and infrastructure.

## Content addressing

Agent artifacts live in OCI registries, using infrastructure that engineering teams already understand and operate.

Rather than identifying artifacts by where they are stored, AGNTCY uses a CID to identify the content itself.

The CID provides an immutable, content-derived reference. If the content changes, the CID changes.

This gives the network a stable way to refer to an artifact regardless of where it is stored.

Importantly, using CIDs does not mean that Directory nodes participate in the public IPFS network. The CID comes from the multiformats ecosystem, while Directory nodes form their own DHT network.

## Two-stage discovery

The Directory discovery process happens in two related stages.

### 1. Provider discovery

A standalone CID can be announced to the network and used to answer:

> **Who has this CID?**

This allows a consumer to discover which peers can provide a particular artifact or record.

### 2. Content discovery

The Directory also announces `(CID, metadata)` pairs containing information such as:

- Skills
- Domains
- Modules
- Locator types

This allows consumers to ask a different question:

> **What CIDs are available for this skill, domain, module, or locator type?**

This distinction is important because agent discovery is not only about finding a known artifact.

Often, a consumer does not know the CID in advance. Instead, it knows what capability or domain it is looking for and needs to discover the relevant records.

The DHT therefore supports both **provider discovery** and **content discovery**.

For more detail, see [Distributed Announce and Discovery](https://blogs.agntcy.org/technical/2026/02/19/dir-v1.html) and the [AGNTCY ADS IETF draft](https://datatracker.ietf.org/doc/draft-mp-agntcy-ads).

## Distributed discovery

The CID and associated discovery information are announced through the Kademlia DHT.

This removes the need for a centralized lookup service.

Instead of every participant depending on a single database or API, the DHT distributes discovery information across participating Directory nodes.

Multiple organizations can therefore participate in the same discovery network while retaining control over their own infrastructure.

You can read more about this in the [AGNTCY routing documentation](https://dir.agntcy.org/latest/dir-component-routing/).

## Metadata retrieval

The DHT is intentionally kept lightweight.

Once a peer has been discovered, AGNTCY uses libp2p RPC to communicate directly with that peer and retrieve the associated metadata.

This can include labels, routing information, and other details needed by the consumer.

The basic principle is:

**Use the DHT for discovery. Use direct peer connections for the heavier data exchange.**

This keeps the DHT efficient while allowing richer metadata to be retrieved when it is actually needed.

## Trust travels with the record

Discovery is only half of the problem.

Once you discover an artifact or agent, you also need to know whether you can trust what you found.

AGNTCY addresses this by making trust information available alongside the discovered record.

Through the same RPC path, a peer can retrieve information such as:

- The artifact's signature
- Public key
- Security scan results

This means a consumer can verify the artifact itself rather than simply trusting the peer that served it.

That distinction is particularly important in a decentralized system.

There is no central registry acting as the ultimate authority saying, "this artifact is trusted." Instead, the information needed to establish that trust travels with the record and can be independently verified.

In other words:

**Discovery tells you what exists. Verification tells you whether you should act on it.**

See the [AGNTCY Directory Trust Model](https://dir.agntcy.org/latest/dir/dir-component-trust-model/) for more detail.

## Event distribution

New publications and updates also need to reach the network quickly.

Rather than requiring every node to continuously poll for changes, GossipSub allows Directory nodes to subscribe to topics and receive announcements as new information is published.

This provides an efficient publish-subscribe mechanism for propagating updates across the network while keeping discovery and retrieval separate.

## Discovery is decentralized; content transfer remains familiar

A natural assumption for a libp2p-based architecture is that everything must move peer-to-peer.

That is not the goal here.

The peer-to-peer layer handles:

- Announcement
- Lookup
- Discovery
- Metadata exchange

Bulk catalog replication between organizations can continue to use standard OCI registry synchronization.

This is deliberate.

The principle is simple: **decentralize where centralization creates risk, while continuing to use proven infrastructure where it already works well.**

Organizations do not need to abandon their existing OCI registry operations to participate in decentralized discovery.

This also lowers the adoption barrier. Teams can continue using familiar registry infrastructure for artifact distribution while adding a decentralized discovery layer.

The [AGNTCY multispec work](https://blogs.agntcy.org/technical/2026/06/17/ai-catalog-over-directory.html) provides additional context on this model.

## Why decentralized discovery instead of a database?

It is a fair question.

A central database with an API would certainly be simpler to reason about on day one. The tradeoffs become more apparent as the ecosystem grows.

A centralized lookup service can:

- Become a single point of failure
- Create vendor lock-in
- Make federation between independent organizations more difficult
- Become an operational bottleneck as the network scales

Decentralized discovery avoids these constraints by allowing multiple organizations to participate in the same network while retaining control over their own infrastructure.

This is particularly valuable in an agent ecosystem where competitors, partners, and independent developers may all need to discover one another's agents without requiring a single organization to operate or control the global directory.

The Directory architecture also supports different deployment models rather than requiring every organization to operate the same way.

See [Choosing a Directory Setup](https://dir.agntcy.org/latest/dir-choosing-a-setup/) for more detail on private, networked, and federated topologies.

## Hybrid deployment in practice

None of this requires going fully decentralized on day one.

AGNTCY's architecture supports hybrid deployments that combine:

- Cloud infrastructure
- Private data centers
- On-premises deployments
- Peer-to-peer networking

A common pattern is to combine centralized authentication with decentralized discovery.

Enterprise requirements around identity and access control can therefore coexist with a discovery layer that does not depend on any single party's uptime.

This is particularly important for enterprise environments.

Organizations do not need to throw out their existing identity and access infrastructure. The decentralized components can be focused specifically on discovery and routing, where centralization can create operational and architectural risks.

The Directory's authentication model is documented in the [OIDC Gateway documentation](https://dir.agntcy.org/latest/dir/dir-component-oidc-authentication/).

## Try the public testbed

For developers who want to experiment with the Directory, joining the public testbed can be as simple as configuring a bootstrap peer:

```text
/dns4/routing.ads.outshift.io/tcp/5555/p2p/12D3KooWLf9p3cedc86xGQBaqak6rAFmQk1HxKAK1yh7umHE3amu
```

You can also start with the [DIR Quick Start Guide](https://dir.agntcy.org/latest/dir/dir-quickstart/), explore the [Directory documentation](https://dir.agntcy.org/), or dive directly into the [source code on GitHub](https://github.com/agntcy/dir).

## Why this is a useful reference point

If you are building or evaluating an agent network — whether it looks like AGNTCY or something entirely new — the Directory provides a concrete example of what a production implementation can look like when built on a shared networking layer such as libp2p.

The important part is not simply that the system is decentralized.

It is that the architecture is deliberately decomposed:

- **libp2p** provides peer identity and secure networking.
- **The DHT** provides decentralized discovery.
- **GossipSub** propagates announcements.
- **RPC** retrieves richer metadata and trust information.
- **CIDs** provide content identity.
- **OCI registries** continue to handle bulk artifact distribution and synchronization.
- **Existing authentication infrastructure** can remain in place where enterprises need it.

Each layer has a focused responsibility, allowing the system to combine decentralized networking with infrastructure organizations already use.

That composition is what makes the architecture interesting beyond AGNTCY itself.

Teams building agent ecosystems do not necessarily need to reinvent identity, discovery, messaging, content addressing, or data distribution independently. They can compose existing protocols and infrastructure into a system that fits their particular deployment model.

## Where we go next

The current Directory implementation also raises interesting questions around observability, routing, network performance, and operating decentralized agent infrastructure at scale.

These are areas where the libp2p and agent ecosystem communities can learn from each other.

AGNTCY already has operational experience running this architecture in practice, while the broader libp2p community brings experience from operating decentralized networks across many different environments.

In the next post, we will look more closely at those open questions — and at where collaboration between the AGNTCY Directory team and the wider libp2p community could help shape the next generation of agent networking infrastructure.

## Learn more

- [AGNTCY DIR on GitHub](https://github.com/agntcy/dir)
- [AGNTCY Directory](https://dir.agntcy.org/)
- [DIR Quick Start Guide](https://dir.agntcy.org/dir/dir-quickstart/)
- [Directory Routing](https://dir.agntcy.org/latest/dir-component-routing/)
- [Choosing a Directory Setup](https://dir.agntcy.org/latest/dir-choosing-a-setup/)
- [Directory Trust Model](https://dir.agntcy.org/latest/dir/dir-component-trust-model/)
- [OIDC Authentication](https://dir.agntcy.org/latest/dir/dir-component-oidc-authentication/)
- [Distributed Announce and Discovery](https://blogs.agntcy.org/technical/2026/02/19/dir-v1.html)
- [AI Catalog over Directory / Multispec](https://blogs.agntcy.org/technical/2026/06/17/ai-catalog-over-directory.html)
- [AGNTCY ADS IETF Draft](https://datatracker.ietf.org/doc/draft-mp-agntcy-ads)
