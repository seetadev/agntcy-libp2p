### What Is Next: Observability, Trust-Aware Routing, and the Open Frontier for Decentralized Agent Networks

The first two posts in this series explored why a shared networking layer matters for the Internet of Agents, and then went under the hood of AGNTCY's production discovery pipeline to show what that looks like in practice.

This post looks forward.

The foundation is solid, but there is a clear set of open problems that will determine how well decentralized agent networks operate as they scale. Observability, measurement, trust-aware routing, capability discovery, interoperability, and the ability to turn what we learn from production networks into reusable infrastructure are all becoming increasingly important.

These are not problems that any one project can solve alone. They sit at the intersection of the agent ecosystem, peer-to-peer networking, and Internet measurement communities. That is why we have been taking these questions beyond individual implementations and into venues such as the IETF, while continuing to work directly with the libp2p and AGNTCY communities. 

## Observability is the next hard problem

A decentralized network that works is one thing.

A decentralized network that you can actually operate with confidence is another.

Today, teams running agent discovery infrastructure on libp2p need much better answers to basic operational questions. When two peers cannot connect, for example, it should be possible to understand why. Operators need to know whether the DHT is healthy, how long lookups are taking, which transports are being negotiated, whether announcements are propagating as expected, and where routing failures are occurring.

They also need visibility into the effects of relays and NAT traversal, peer reachability, and how network behaviour changes as peers join and leave.

These are not exotic questions. They are the same questions an operations team asks about any production system.

The difference is that decentralized networks do not have a single load balancer, database, service mesh, or control plane from which to collect all the answers. 

At the network layer, useful measurements include connection success and failure rates, peer churn, DHT lookup latency, routing paths, NAT traversal success, relay utilization, transport selection, peer reachability, resource consumption, and topology changes.

But for agent networks, network-level visibility is only half the story.

We also need to understand agent discovery latency, content discovery effectiveness, metadata retrieval performance, RPC performance, publication propagation, federation health, request traces, and ultimately end-to-end task latency. 

Putting these layers together gives us something much more useful than traditional application monitoring: visibility into how the decentralized network and the applications running on top of it behave together.

This is one of the areas we are most actively thinking about because it is the difference between a network that works in a demo and one an enterprise is willing to run production workloads on. 

## From observability to a common measurement framework

The problem is bigger than AGNTCY.

libp2p is already being used across systems such as Ethereum, IPFS, Filecoin, and other decentralized networks. Each ecosystem has developed its own monitoring, crawling, telemetry, benchmarking, and analysis infrastructure.

That has produced a lot of valuable data, but the measurements are often ecosystem-specific. A question such as *"how healthy is this peer-to-peer network?"* can therefore mean something different depending on which network you are looking at. 

There is an opportunity to define common measurement primitives that can be reused across large-scale libp2p deployments.

That means agreeing not only on **what should be measured**, but also on **how those measurements are represented, exchanged, validated, and compared**.

That is the motivation behind our work on verifiable telemetry and our participation in the IETF measurement community. 

## Taking agent network observability to the IETF

At IETF 126, we participated in discussions across MAPRG, IEPG, and the IETF Hackathon around operating and measuring large-scale agent and peer-to-peer networks.

### MAPRG: measuring large-scale decentralized networks

In MAPRG, we are exploring the broader question of how decentralized networks can be measured consistently across deployments.

The relevant materials are:

* [IETF 126 MAPRG session](https://datatracker.ietf.org/meeting/126/session/maprg)
* [MAPRG agenda](https://datatracker.ietf.org/doc/agenda-126-maprg/)
* [IETF 126 MAPRG meeting minutes](https://ietfminutes.org/minutes/ietf126/maprg.html)
* [MAPRG presentation recording](https://youtu.be/Rm4XAVJ4Pxs?si=Y3Ck43ttUEJ9oGJK)

Our proposed direction is a common measurement framework for large-scale libp2p deployments, with measurements represented as portable, verifiable telemetry objects.

The candidate dimensions span peer discovery effectiveness, peer churn, client diversity, geographic distribution, connectivity patterns, NAT traversal success, relay dependency, routing performance, topology evolution, and protocol interoperability. 

The important idea is that these measurements should be useful beyond a single deployment.

Instead of treating measurements as application-specific logs, we can treat them as structured artifacts that can be stored, exchanged, compared, and independently verified. 

## Verifiable Telemetry Objects

One of the pieces we are developing toward this goal is the concept of **Verifiable Telemetry Objects (VTOs)**.

The idea is straightforward: measurements should not have to remain ephemeral observability data.

A measurement can become a portable protocol artifact with a defined schema, deterministic encoding, content addressing, cryptographic verification, provenance, and reproducible representation. 

This opens up interesting possibilities for decentralized networks.

A measurement collected from one network could be shared with another system, stored using content-addressed infrastructure, or used as an input to independent research and analysis. 

### Why CBOR?

For decentralized telemetry, representation matters.

CBOR provides a compact, language-independent serialization format that is well suited to protocol-level telemetry. With deterministic serialization, the same logical measurement can produce the same bytes across implementations.

That matters when telemetry itself needs to be hashed, signed, referenced, or compared.

Our work is also exploring how deterministic serialization profiles such as [CBOR-42](https://github.com/ipfs/specs/tree/main/block-layer/cbor-42) can provide the foundation for verifiable telemetry. 

The longer-term goal is to move from:

> **"Here is a log of what happened."**

to:

> **"Here is a verifiable, content-addressed record of what happened."**

That shift could make telemetry itself part of the infrastructure of decentralized networks rather than something that disappears into an observability backend after the fact. 

## The CBOR digest context and the VTO work

There is also an important piece of engineering work underway around the relationship between VTO and deterministic CBOR serialization.

A recent review identified an issue with the provisional VTO registry entry: it currently points to `jcs-n`, while VTO telemetry uses CBOR-42 and includes floating-point measurements.

Rather than treating this as a reason to prohibit floats, the work is being used to define a digest context that reflects what the libp2p telemetry implementation actually produces.

The scope is deliberately narrow: align the CBOR digest context with the bytes produced by the current libp2p implementation, define how floating-point measurements are handled, provide an informative multihash/CID mapping, and keep the existing Composable Trust Blueprint unchanged at the normative level. 

This is an important principle for protocol design: serialization and digest rules should be driven by real interoperability requirements and real implementation output, rather than by an abstract registry slot.

The immediate inputs required from the libp2p side are therefore concrete: the actual VTO schema or CDDL definition, one real encoded VTO instance as bytes, the digest computed over that instance, and details about the float-bearing fields, their precision, and whether they are derived measurements. 

This is the kind of work where having an actual implementation and actual bytes is more useful than another architecture diagram.

## IEPG: operating and measuring agent networks over libp2p

The same questions become more concrete when looking specifically at agent networks.

At IETF 126 IEPG, we presented work on operating and measuring agent networks over libp2p. The presentation connects the operational realities of agent networks with the broader peer-to-peer measurement problem. 

The relevant materials include:

* [IETF 126 IEPG session](https://datatracker.ietf.org/meeting/126/session/iepg)
* [Operating and Measuring Agent Networks over libp2p — presentation](https://datatracker.ietf.org/doc/slides-126-iepg-sessa-iepg-operating-and-measuring-agent-networks-over-libp2p-johanna-manu/)
* [IEPG presentation materials](https://datatracker.ietf.org/meeting/126/materials/slides-126-iepg-sessa-iepg-operating-and-measuring-agent-networks-over-libp2p-johanna-manu-01)
* [IEPG session recording](https://youtu.be/g8q_u19vXzk?si=csIQQprAO1P49D2a)
* [IEPG Meetecho recording](https://meetecho-player.ietf.org/playout/?session=IETF126-IEPG-20260719-0800)

The objective is not to create an observability system specific to one agent framework. It is to understand which measurements become important when large numbers of agents operate over decentralized infrastructure, and how those measurements can become reusable building blocks for the wider ecosystem.

## IETF Hackathon: turning ideas into implementations

The IETF Hackathon provides a different but complementary environment.

The focus there is on taking protocol ideas and turning them into working implementations that can be tested across real systems.

We also participated in the [IETF 126 Hackathon](https://datatracker.ietf.org/meeting/126/session/hackathon), using it as an opportunity to explore the practical side of operating and measuring peer-to-peer and agent networking systems. 

The combination of MAPRG, IEPG, and the Hackathon is particularly useful. MAPRG gives us a place to discuss measurement methodology; IEPG connects that work to operational experience; and the Hackathon provides an environment for implementation and interoperability testing.

Together, they create a path from research questions to operational measurements to working code. 

## A common substrate under a growing protocol landscape

The agent protocol landscape is moving quickly.

SLIM, MCP, A2A, AGNTCY's own protocols, OpenTelemetry integrations, identity systems, and other standards are evolving in parallel.

libp2p's role is not to pick a winner.

It is application agnostic by design.

Multiple protocols can run over the same networking layer, sharing common primitives for identity, connectivity, transport, discovery, routing, and messaging. 

That matters as the ecosystem becomes more diverse.

Every new Internet of Agents project should not need to implement its own transport and discovery layer simply to communicate with another project.

If enough projects share a common networking substrate, protocol-level differences become a much smaller barrier to interoperability than they would be if every project also had a completely different networking stack underneath.

This is one of the strongest arguments for investing in shared infrastructure rather than rebuilding the same primitives inside every agent project. 

## Routing gets more interesting from here

The current discovery model can find peers, providers, and content.

The next challenge is finding the **right** peer.

That is a much more interesting routing problem.

Imagine moving beyond a simple question such as:

> **Who has this content?**

and instead asking:

> **Which peer can perform this capability?**

That is the direction capability-aware routing points toward. Discovery should increasingly account for what an agent can actually do, rather than treating peers simply as endpoints or providers. 

Trust introduces another dimension.

A routing decision could eventually incorporate artifact signatures, verification status, security scan results, reputation, historical behaviour, and policy requirements. This does not necessarily mean creating one global reputation score. Different applications may have very different trust models.

The networking layer should instead make it possible to incorporate verifiable signals into routing decisions. 

Locality matters too.

Latency, geography, data residency, and regulatory requirements can all influence which peer is appropriate. The closest peer is not always the best peer. For some workloads, the correct peer may be the one in a particular jurisdiction, organization, network region, or trust domain. 

And then there is the network itself.

Conditions change. Peers become unavailable, congestion increases, latency shifts, churn occurs, relay utilization changes, and connectivity failures appear.

Routing algorithms should eventually be able to respond to those conditions rather than treating routing as a static decision. 

None of this is available as a complete off-the-shelf solution today.

It is a genuine research and engineering opportunity, and exactly the kind of problem that benefits from collaboration between people who understand libp2p's routing internals and people who understand what agent ecosystems need operationally. 

## Discovery is going to mean more than finding a peer

Today, discovery in many decentralized systems starts with finding a peer that advertises a particular piece of content.

The more interesting evolution is to make capabilities themselves first-class discoverable objects.

That could include skills, services, APIs, tools, models, domains, modules, and other capabilities.

The question changes from:

> **Who is out there?**

to:

> **Who can do what I need?**

For autonomous agents, that is a much more useful question.

AGNTCY's Directory is already moving in this direction through content discovery based on metadata such as skills, domains, modules, and locator types. The next challenge is connecting that richer discovery model with routing and trust. 

## Trust and reputation as a missing layer

Another gap becomes increasingly visible as decentralized agent networks grow.

Peer identity is well understood.

Content addressing is well understood.

Provider discovery is increasingly well understood.

But knowing whether you should trust what you find is a different problem.

The [AGNTCY Directory Trust Model](https://docs.agntcy.org/dir/dir-component-trust-model/) demonstrates one important approach: trust information can travel with the record, allowing consumers to verify an artifact rather than simply trusting the peer that served it. 

The next step is understanding how those verifiable signals can influence routing and decision-making.

A network may eventually need to answer questions such as whether an artifact is authentic, whether it has been verified, whether it has passed a security scan, who signed it, which trust domain it belongs to, what its operational history looks like, and which policies it satisfies.

There is unlikely to be one universal answer.

Different agent networks will have different trust models. The opportunity is to build interoperable primitives that allow those models to coexist. 

## From individual projects to shared infrastructure

This is where the work becomes particularly interesting for the libp2p community.

AGNTCY provides a real production environment in which these problems can be observed. libp2p provides a mature networking foundation and a community with experience operating decentralized systems at scale. The IETF provides a venue where measurement methodologies, interoperability requirements, and protocol abstractions can be discussed across ecosystems.

Projects such as VTO and CBOR-42 provide a path toward making measurements themselves portable and verifiable.

These pieces reinforce each other.

Production networks give us real operational problems. Measurement gives us evidence. Standardized telemetry gives us interoperable data. Cryptographic verification gives us confidence in that data. And shared networking primitives give us a place to apply the resulting insights. 

That feedback loop is important.

Instead of developing abstractions in isolation and hoping they eventually match production requirements, we can use real deployments to identify problems, develop measurements around those problems, turn useful measurements into reusable protocol artifacts, and then feed those learnings back into the underlying networking layer.

## Where this leaves builders

If you are building on AGNTCY today or evaluating infrastructure for a new agent network, these open questions are not blockers.

The core networking and discovery layer is already being used in production, as the previous post in this series showed. But the next generation of decentralized agent networks will need more than connectivity and discovery. 

They will need observability to understand what the network is doing, measurement to compare and improve deployments, trust to establish whether discovered information is safe to act on, routing intelligence to select the right peer rather than simply any peer, capability discovery to connect agents based on what they can actually do, interoperability so different agent protocols can share common infrastructure, and verifiable telemetry so network measurements can become reusable protocol artifacts. 

These are the areas where we see the most opportunity for collaboration between AGNTCY, libp2p, and the wider Internet engineering community.

## An open frontier for libp2p contributors

There is also a very practical opportunity for developers interested in contributing to libp2p.

As these agent networks mature, the work is moving beyond simply making a connection. There are opportunities to improve the underlying networking stack around DHT routing and performance, peer discovery, connectivity diagnostics, NAT traversal, relay behaviour, transport observability, RPC performance, GossipSub measurements, routing telemetry, network health metrics, interoperability testing, and verifiable telemetry generation. 

These are not theoretical extensions.

They are driven by real operational requirements emerging from systems such as AGNTCY and other large-scale decentralized deployments.

For contributors who want to work closer to the protocol layer, this provides a concrete path from an agent ecosystem requirement to a reusable libp2p primitive. 

## Where we go next

The interesting thing about decentralized agent networking is that the foundational pieces are now increasingly real.

The next frontier is making them measurable, understandable, trustworthy, and adaptable.

We are continuing to work across these layers — from production AGNTCY deployments and libp2p implementation work, to IETF discussions around measurement and interoperability, and research into verifiable telemetry and trust-aware networking.

The goal is not to build another isolated agent stack.

It is to help create a common networking foundation that different agent ecosystems can build on, measure, and improve together. 

If your team is working on production observability, decentralized routing, agent discovery, trust models, peer-to-peer measurement, or the underlying libp2p infrastructure, we would love to compare notes and collaborate.

---

# References and further reading

## AGNTCY Directory

* [AGNTCY DIR on GitHub](https://github.com/agntcy/dir)
* [AGNTCY Directory](https://dir.agntcy.org/)
* [DIR Quick Start Guide](https://dir.agntcy.org/dir/dir-quickstart/)
* [Directory Routing](https://docs.agntcy.org/dir/dir-component-routing/)
* [Choosing a Directory Setup](https://docs.agntcy.org/dir/dir-choosing-a-setup/)
* [Directory Trust Model](https://docs.agntcy.org/dir/dir-component-trust-model/)
* [OIDC Authentication](https://docs.agntcy.org/dir/dir-component-oidc-authentication/)
* [Distributed Announce and Discovery](https://blogs.agntcy.org/technical/2026/02/19/dir-v1.html)
* [AI Catalog over Directory / Multispec](https://blogs.agntcy.org/technical/2026/06/17/ai-catalog-over-directory.html)
* [AGNTCY ADS IETF Draft](https://datatracker.ietf.org/doc/draft-mp-agntcy-ads)

## IETF 126

### MAPRG

* [IETF 126 MAPRG session](https://datatracker.ietf.org/meeting/126/session/maprg)
* [MAPRG agenda](https://datatracker.ietf.org/doc/agenda-126-maprg/)
* [MAPRG meeting minutes](https://ietfminutes.org/minutes/ietf126/maprg.html)
* [MAPRG presentation recording](https://youtu.be/Rm4XAVJ4Pxs?si=Y3Ck43ttUEJ9oGJK)

### IEPG

* [IETF 126 IEPG session](https://datatracker.ietf.org/meeting/126/session/iepg)
* [Operating and Measuring Agent Networks over libp2p — presentation](https://datatracker.ietf.org/doc/slides-126-iepg-sessa-iepg-operating-and-measuring-agent-networks-over-libp2p-johanna-manu/)
* [IEPG presentation materials](https://datatracker.ietf.org/meeting/126/materials/slides-126-iepg-sessa-iepg-operating-and-measuring-agent-networks-over-libp2p-johanna-manu-01)
* [IEPG session recording](https://youtu.be/g8q_u19vXzk?si=csIQQprAO1P49D2a)
* [IEPG Meetecho recording](https://meetecho-player.ietf.org/playout/?session=IETF126-IEPG-20260719-0800)

### IETF Hackathon

* [IETF 126 Hackathon](https://datatracker.ietf.org/meeting/126/session/hackathon)

## Verifiable Telemetry and CBOR

* [CBOR-42](https://github.com/ipfs/specs/tree/main/block-layer/cbor-42)
* [AGNTCY ADS IETF Draft](https://datatracker.ietf.org/doc/draft-mp-agntcy-ads)
* [Distributed Announce and Discovery](https://blogs.agntcy.org/technical/2026/02/19/dir-v1.html)

## Closing thought

The next generation of decentralized agent networks will not be defined only by how well agents connect.

It will be defined by how well we can **measure the network, understand its behaviour, verify what we discover, and route intelligently through it**.

That is the open frontier — and it is a problem that is bigger than any single project.

It is an opportunity for the AGNTCY, libp2p, IETF, and broader Internet engineering communities to build the foundations together.

This version keeps the **technical depth and all the references from the original**, but makes the argument flow more naturally: **production → observability → measurement → verifiable telemetry → IETF → routing → trust → shared infrastructure → contributor opportunities**. It should read much more like a published technical blog than a structured project note.
