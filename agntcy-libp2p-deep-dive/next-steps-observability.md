
### What Is Next: Observability, Trust-Aware Routing, and the Open Frontier for Decentralized Agent Networks

The first two posts in this series looked at the foundations of decentralized agent networking. The first made the case for a shared networking layer for the Internet of Agents. The second went under the hood of the AGNTCY Directory to show how those ideas translate into a production discovery system built on libp2p.

The natural question is: **what comes next?**

The basic networking primitives are increasingly well understood. Agents can establish secure peer-to-peer connections, discover peers and content, exchange metadata, and operate across heterogeneous network environments. But as these systems move from experiments into production, a new set of challenges becomes increasingly important.

We need to understand not only whether the network works, but *how* it is behaving. We need to know which peers and capabilities we should trust, how to route requests intelligently, and how to measure decentralized systems in ways that allow different deployments to be compared and improved.

These are not problems that belong exclusively to AGNTCY or libp2p. They are emerging across the broader Internet of Agents ecosystem, and they are increasingly relevant to the Internet engineering community.

That is why our work is now extending beyond the implementation itself into observability, measurement, trust, and routing — including discussions and experimentation through the IETF.

### From connectivity to operability

A decentralized network that works is one thing. A decentralized network that an engineering team can confidently operate at production scale is another.

In a centralized architecture, operators have relatively straightforward places to look when something goes wrong. There may be a load balancer, a database, a service mesh, or a centralized observability platform that provides a relatively complete picture of the system.

A peer-to-peer network has no such single vantage point.

When two agents cannot communicate, for example, the cause could be NAT traversal, relay availability, transport negotiation, peer reachability, routing, DHT state, or simply the state of the remote peer. A slow discovery operation could similarly result from the application, the DHT, the network topology, or the path between peers.

As agent networks grow, operators will need answers to questions such as:

* Why can't these two peers connect?
* Is the DHT healthy?
* How long are discovery lookups taking?
* Which transports are being negotiated?
* Are announcements propagating as expected?
* How much does NAT traversal affect connectivity?
* Which peers are becoming unreachable?
* How much are relays being used?
* Where are requests spending their time?

These are ordinary production questions. What is different is the environment in which they need to be answered.

For agent networks, observability has to span both the application and networking layers. At the networking layer, this means understanding peer churn, connection success rates, DHT latency, routing paths, NAT traversal, relay dependency, transport behavior, and resource consumption. At the application layer, we need to understand agent discovery latency, metadata retrieval, RPC performance, publication propagation, federation health, and end-to-end request execution.

The interesting problem is connecting these two views.

An agent application may report that discovery took five seconds. That number is useful, but it becomes much more useful when we can determine whether those five seconds came from DHT lookup latency, peer connectivity, relay traversal, metadata retrieval, or something else entirely.

That is where a common measurement framework becomes important.

## Measuring decentralized networks as first-class systems

There are already enormous real-world laboratories for studying peer-to-peer networking.

Ethereum, IPFS, Filecoin, Celestia, and other decentralized systems collectively operate large numbers of nodes across different geographic regions, network environments, implementations, and infrastructure providers. AGNTCY and other emerging agent networks add another class of workloads to this landscape.

Each ecosystem has developed valuable monitoring and measurement infrastructure, but much of it remains ecosystem-specific.

We believe there is an opportunity to standardize not only **what should be measured**, but also **how those measurements are represented, exchanged, and verified**.

That is the motivation behind our work on Verifiable Telemetry Objects, or VTOs.

The idea is to turn measurements from ephemeral logs into portable protocol artifacts. A measurement should be something that can be represented consistently across implementations, hashed and signed, stored using content-addressed infrastructure, and reused as an input for independent analysis.

This is particularly relevant for decentralized systems because there is rarely a single organization that everyone trusts to operate the canonical monitoring system.

Instead, measurements themselves can carry provenance and verification information.

## Taking the measurement problem to the IETF

We have started taking these questions into the IETF, where there is an opportunity to discuss them across different peer-to-peer deployments rather than treating agent networking as an isolated problem.

At IETF 126, our participation spanned the Measurement and Analysis for Protocols Research Group (MAPRG), the Internet Engineering and Planning Group (IEPG), and the IETF Hackathon.

Each provides a different perspective on the same underlying challenge.

### MAPRG: toward common measurement practices

Our MAPRG work focuses on the broader measurement problem: how do we develop reusable methodologies for understanding large-scale decentralized networks?

The [IETF 126 MAPRG session](https://datatracker.ietf.org/meeting/126/session/maprg), [agenda](https://datatracker.ietf.org/doc/agenda-126-maprg/), and [meeting minutes](https://ietfminutes.org/minutes/ietf126/maprg.html) provide the broader context.

We also shared a presentation and discussion around a common measurement framework for large-scale libp2p deployments using CBOR-based verifiable telemetry. The [MAPRG presentation recording](https://youtu.be/Rm4XAVJ4Pxs?si=Y3Ck43ttUEJ9oGJK) is available for those who want to follow the discussion directly.

The direction we are exploring is deliberately broader than agent networks. Candidate measurements include peer discovery effectiveness, churn, client diversity, geographic distribution, connectivity patterns, NAT traversal success, relay dependency, routing performance, topology evolution, and protocol interoperability.

The goal is not to impose a single monitoring system.

It is to establish common measurement primitives so that observations from different decentralized networks can be represented in a way that is comparable and reusable.

## IEPG: operating and measuring agent networks over libp2p

The IEPG discussion brings the problem closer to the operational reality of agent networks.

At IETF 126, Johanna Moran and Manu Sheel Gupta presented **Operating and Measuring Agent Networks over libp2p**.

The presentation looks at what it means to actually operate agent networks on a decentralized networking substrate and which measurements become important as those networks scale.

The relevant materials are available through the [IETF 126 IEPG session](https://datatracker.ietf.org/meeting/126/session/iepg), the [presentation](https://datatracker.ietf.org/doc/slides-126-iepg-sessa-iepg-operating-and-measuring-agent-networks-over-libp2p-johanna-manu/), and the [IEPG presentation materials](https://datatracker.ietf.org/meeting/126/materials/slides-126-iepg-sessa-iepg-operating-and-measuring-agent-networks-over-libp2p-johanna-manu-01).

The [IEPG session recording](https://youtu.be/g8q_u19vXzk?si=csIQQprAO1P49D2a) and [Meetecho recording](https://meetecho-player.ietf.org/playout/?session=IETF126-IEPG-20260719-0800) provide additional context.

This work is important because agent networks introduce an interesting combination of application-level and network-level behavior.

An agent may discover another agent through a decentralized directory, establish a connection through NAT traversal or a relay, negotiate a transport, retrieve metadata over RPC, and then invoke a capability that itself triggers additional distributed interactions.

Understanding the performance of that complete chain requires measurements that cross traditional observability boundaries.

## The IETF Hackathon: turning measurement ideas into implementations

Research and operational discussion are only part of the process.

The [IETF 126 Hackathon](https://datatracker.ietf.org/meeting/126/session/hackathon) provides a complementary environment for turning protocol ideas into working implementations and testing interoperability.

For decentralized networking, this matters because many of the hardest problems only become apparent when implementations interact.

A measurement schema may look straightforward until it is generated by multiple implementations. A routing signal may look useful until it is exposed to real network conditions. A telemetry record may look deterministic until different languages encode the same measurement differently.

Implementation and interoperability testing therefore become an important part of the standards process.

The combination of MAPRG, IEPG, and the Hackathon gives us a useful progression: discuss the measurement problem, understand it from an operational perspective, and then test the resulting ideas in implementations.

## Verifiable telemetry: making measurements portable

A central question is what happens after a measurement is collected.

Traditional observability systems tend to treat telemetry as something that is sent to a monitoring backend and then consumed within the same administrative domain.

That model becomes less effective when the network itself spans independent organizations.

Consider a federated agent network involving multiple enterprises. Each organization may be willing to share evidence that a particular peer was reachable, an artifact passed a security check, or a routing operation succeeded. But it may not be willing to expose its complete internal logs.

A portable telemetry object provides a different model.

The measurement can contain the information necessary to establish what was measured, when it was measured, where it came from, and how it can be verified, without requiring the underlying organization to expose its entire internal observability system.

This is where VTO and deterministic CBOR encoding become particularly interesting.

## CBOR-42 and the path toward reproducible telemetry

CBOR provides a compact, language-independent representation that is well suited to protocol-level telemetry.

Deterministic encoding adds another important property: the same logical object can be represented by the same canonical bytes across implementations.

That becomes important when measurements need to be hashed, signed, content-addressed, or compared.

Our work around [CBOR-42](https://github.com/ipfs/specs/tree/main/block-layer/cbor-42) explores this deterministic encoding layer in the context of content-addressed systems.

There is also ongoing work to make the relationship between VTO and deterministic CBOR more concrete.

A recent review identified that the provisional VTO registry entry currently points to `jcs-n`, while VTO telemetry is encoded using CBOR-42 and includes floating-point measurements. Rather than treating floating-point values as something that must simply be prohibited, the proposed work is to define a CBOR-side digest context that matches what the implementation actually produces.

The immediate engineering work is deliberately narrow: align the digest context with the bytes produced by the libp2p implementation, define appropriate float handling, and provide an informative multihash/CID mapping.

That work illustrates an important principle for interoperable protocol design: standards should be grounded in real implementations and real interoperability requirements.

## A common substrate under a growing protocol landscape

Observability is only one part of the larger picture.

The agent protocol landscape is evolving quickly. MCP, A2A, SLIM, AGNTCY protocols, OpenTelemetry integrations, identity systems, and other standards are developing in parallel.

libp2p does not need to choose among them.

That is one of the strengths of a general-purpose networking substrate. Different protocols can run over the same underlying transport, identity, discovery, routing, and messaging primitives.

This becomes particularly important as the ecosystem becomes more fragmented.

If every new agent project implements its own networking layer, interoperability becomes difficult even when the application protocols themselves are compatible.

If multiple projects instead share a common substrate, the networking differences largely disappear. Projects can focus on the semantics of agent interaction while relying on common infrastructure for connectivity and decentralized communication.

That is the same architectural principle we see in AGNTCY's Directory: decentralize the parts where centralization introduces meaningful constraints, while continuing to use proven infrastructure where it makes sense.

## Routing gets more interesting from here

The current discovery model answers questions such as:

> Who has this CID?

and increasingly:

> What content is available for this skill, domain, module, or locator type?

The next question is harder:

> Which peer should I actually use?

That moves us from discovery toward intelligent routing.

A future routing system could take capability into account, selecting peers based not simply on their existence but on what they can do.

It could incorporate trust signals, selecting a verified or appropriately trusted peer rather than an arbitrary provider.

It could consider locality, choosing a peer based on latency, geography, data residency, or organizational boundaries.

And it could adapt to network conditions, changing its routing decisions as peers become unavailable, connectivity changes, or the network experiences congestion.

These capabilities are not available as a complete off-the-shelf system today.

That is precisely why they are interesting.

They represent an open research and engineering frontier where the requirements emerging from agent networks can directly inform improvements to the underlying peer-to-peer networking stack.

## From provider discovery to capability discovery

The evolution of discovery is particularly important here.

The initial problem is finding a peer that has a particular piece of content.

But an autonomous agent often does not care about the content identifier itself. It cares about what another agent can do.

It may need a climate-risk model, a payment service, a verification capability, a particular API, or an agent with expertise in a specific domain.

This changes discovery from:

> Who is out there?

to:

> Who can do what I need?

AGNTCY's Directory already provides a foundation for this through metadata associated with discovered content, including skills, domains, modules, and locator types.

The opportunity ahead is to connect that richer content discovery model with routing and trust.

Once an agent can discover capabilities, evaluate trust signals, and select the appropriate peer based on network conditions and policy, discovery begins to look much more like an actual decentralized service layer for autonomous systems.

## Trust travels with the record

Discovery is only half the problem.

The other half is deciding whether what you discovered is trustworthy.

In a centralized registry, users may implicitly rely on the registry operator to provide some level of assurance about the artifacts or services being discovered.

A decentralized system cannot assume that guarantee exists.

AGNTCY's Directory addresses this by allowing trust information to travel with the record. A peer can retrieve the relevant signature, public key, and security scan information over the same RPC channel used to retrieve metadata.

The important distinction is that the consumer can verify the artifact itself rather than simply trusting the peer that served it.

That makes decentralized discovery safe to act on rather than merely possible.

As these networks grow beyond organizations that already know and trust each other, this becomes increasingly important.

The next step is to understand how these verifiable trust signals can participate in routing decisions.

Trust does not necessarily have to become one universal reputation score. Different applications may have different policies and trust domains.

Instead, the networking layer should provide mechanisms that allow applications to incorporate verifiable signals into their own decisions.

## Federated observability and partial visibility

The same principle applies to observability.

A global agent workflow may cross several independent organizations. A developer, insurer, cloud provider, model operator, and municipal system may all participate in the same workflow without sharing an administrative domain.

It is unrealistic to expect each participant to expose all of its internal logs.

What is more realistic is federated context propagation.

Each participant can maintain its own internal observability system while exposing the subset of information required to reconstruct the broader execution graph.

This creates an important distinction between **visibility** and **disclosure**.

A system can provide enough verifiable context to establish that a particular operation happened, that a particular identity initiated it, or that a particular artifact passed a verification step, without revealing proprietary internal telemetry.

This is one of the areas where agent networking, distributed tracing, privacy, and protocol design increasingly intersect.

## From individual projects to shared infrastructure

The pieces are starting to connect.

AGNTCY provides a real production environment in which decentralized discovery and agent coordination can be studied.

libp2p provides the networking substrate and a community with experience operating decentralized systems at scale.

The IETF provides venues where measurement, interoperability, and operational requirements can be discussed across ecosystems.

VTO and deterministic CBOR provide a potential mechanism for turning network observations into portable and verifiable artifacts.

These do not need to become one giant framework.

In fact, they are more useful if they remain composable.

Production systems generate real problems.

Measurement gives us evidence about those problems.

Standardized telemetry makes the evidence portable.

Cryptographic verification makes it trustworthy.

Routing uses those signals to make better decisions.

And the resulting improvements feed back into the networking layer.

That is the kind of virtuous cycle we want to encourage.

## What this means for builders

For teams building on AGNTCY today, these open questions are not blockers.

The core networking and discovery infrastructure is already being used in real systems, as the previous post in this series described.

But the next generation of decentralized agent networks will need to move beyond simply connecting agents.

They will need networks that can explain themselves, measure themselves, and make better decisions based on what they observe.

That means building toward a world where an agent network can answer questions such as:

* What is happening in the network?
* Why did this request take so long?
* Which peers are reachable?
* Which capabilities are available?
* Which providers can be trusted?
* Which route is best for this request?
* Can another organization independently verify the measurements?
* Can the same telemetry be compared with observations from another deployment?

Answering these questions is as much an infrastructure problem as an AI problem.

## An open frontier for libp2p contributors

There is also a very practical opportunity here for developers working on libp2p.

As agent networks mature, the requirements are moving beyond basic connectivity toward better routing, measurement, diagnostics, and operational tooling.

Some of the most interesting work will likely happen at the boundary between application requirements and core networking primitives: improving DHT behavior and routing, making connectivity failures easier to diagnose, exposing useful transport and GossipSub measurements, improving RPC observability, understanding relay and NAT behavior, and making telemetry generation consistent across implementations.

These are not theoretical extensions.

They are being driven by real operational requirements emerging from AGNTCY and other decentralized deployments.

For a libp2p contributor, that creates a concrete feedback loop: an operational problem observed in an agent network can become a reusable networking primitive that benefits many other decentralized systems.

## The broader opportunity

There is a larger strategic opportunity behind all of this.

As AI systems become more autonomous, computation and decision-making are becoming increasingly distributed. An agent may run in one organization, discover a capability operated by another, retrieve data from a third, invoke a model hosted by a fourth, and produce an outcome that needs to be independently verified.

The resulting system is not simply an application.

It is a distributed system composed of independent actors.

That means the infrastructure underneath it needs the same properties we have learned to value in the Internet itself: open protocols, interoperability, resilience, verifiable identity, decentralized discovery, and the ability to operate across administrative boundaries.

libp2p provides many of the foundational networking primitives for that world.

AGNTCY demonstrates how those primitives can be assembled into a practical agent discovery and coordination architecture.

The work now is to make the resulting networks easier to observe, measure, trust, and route.

## Where we go next

The interesting thing about decentralized agent networking is that the foundational pieces are increasingly real.

The next frontier is making those systems **measurable, understandable, trustworthy, and adaptable**.

Our participation in MAPRG, IEPG, and the IETF Hackathon is part of that broader effort. So is the work around VTO, deterministic CBOR, CBOR-42, and the operational requirements emerging from AGNTCY.

We do not expect one project or one standards group to solve all of these problems.

Instead, we see an opportunity for the AGNTCY, libp2p, IETF, and broader Internet engineering communities to build the foundations together.

The goal is not another isolated agent stack.

The goal is a common networking foundation that different agent ecosystems can build on, measure, verify, and improve together.

And that is where the next stage of the Internet of Agents gets interesting.

## References and further reading

### AGNTCY Directory

* [AGNTCY Directory on GitHub](https://github.com/agntcy/dir)
* [AGNTCY Directory](https://dir.agntcy.org/)
* [Directory Quick Start Guide](https://dir.agntcy.org/dir/dir-quickstart/)
* [Distributed Announce and Discovery](https://blogs.agntcy.org/technical/2026/02/19/dir-v1.html)
* [AI Catalog over Directory / Multispec](https://blogs.agntcy.org/technical/2026/06/17/ai-catalog-over-directory.html)
* [AGNTCY ADS IETF Draft](https://datatracker.ietf.org/doc/draft-mp-agntcy-ads)

### IETF 126 — MAPRG

* [IETF 126 MAPRG session](https://datatracker.ietf.org/meeting/126/session/maprg)
* [MAPRG agenda](https://datatracker.ietf.org/doc/agenda-126-maprg/)
* [MAPRG meeting minutes](https://ietfminutes.org/minutes/ietf126/maprg.html)
* [MAPRG presentation / recording](https://youtu.be/Rm4XAVJ4Pxs?si=Y3Ck43ttUEJ9oGJK)

### IETF 126 — IEPG

* [IETF 126 IEPG session](https://datatracker.ietf.org/meeting/126/session/iepg)
* [Operating and Measuring Agent Networks over libp2p — IETF presentation](https://datatracker.ietf.org/doc/slides-126-iepg-sessa-iepg-operating-and-measuring-agent-networks-over-libp2p-johanna-manu/)
* [IEPG presentation materials](https://datatracker.ietf.org/meeting/126/materials/slides-126-iepg-sessa-iepg-operating-and-measuring-agent-networks-over-libp2p-johanna-manu-01)
* [IEPG session recording](https://youtu.be/g8q_u19vXzk?si=csIQQprAO1P49D2a)
* [IEPG Meetecho recording](https://meetecho-player.ietf.org/playout/?session=IETF126-IEPG-20260719-0800)

### IETF 126 — Hackathon

* [IETF 126 Hackathon](https://datatracker.ietf.org/meeting/126/session/hackathon)

### Verifiable Telemetry and CBOR

* [CBOR-42](https://github.com/ipfs/specs/tree/main/block-layer/cbor-42)
* [AGNTCY ADS IETF Draft](https://datatracker.ietf.org/doc/draft-mp-agntcy-ads)

### Related work

* [AGNTCY Distributed Announce and Discovery](https://blogs.agntcy.org/technical/2026/02/19/dir-v1.html)
* [AI Catalog over Directory / Multispec](https://blogs.agntcy.org/technical/2026/06/17/ai-catalog-over-directory.html)
* [libp2p](https://libp2p.io/)
* [IPFS](https://ipfs.tech/)
