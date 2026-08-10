### AGNTCY Builder Spotlight

### Johanna Moran & Manu Sheel Gupta

**Johanna Moran**
*Ops & Strategy Lead, libp2p*

**Manu Sheel Gupta**
*Technical Lead & Maintainer, libp2p*

### Building the foundations for open, interoperable agent infrastructure

---

### 1. Please tell us a bit more about your background.

**Johanna:**
My background is in ecosystem strategy, partnerships, developer programs and helping emerging technologies move from early technical development toward real-world adoption.

I've worked across several Web3 ecosystems, including ConsenSys, Algorand and Venn Network. At Algorand, I helped grow the ecosystem from an early stage to significant traction, including helping grow TVL from $0 to $65M and sourcing approximately 60% of the active projects sustaining that ecosystem.

At Venn Network, I launched the public testnet, onboarded more than 30 partners, integrated 15 dApps and helped drive more than 4 million transactions with a developer community of over 10,000.

I've also created and led global grant and developer programs, funding more than 30 projects and supporting the training of approximately 15,000 developers worldwide.

A consistent theme in my work has been connecting **research, builders, funding, partnerships and real-world use cases** early. I focus heavily on execution—taking complex technologies and helping create the conditions for them to reach real users.

That is also how I approach my work with libp2p and the emerging agent ecosystem.

**Manu:**
My background is in distributed systems, open-source software and decentralized networking. I've been working in technology and open source for more than 20 years, including around 15 years in business and technical architecture roles.

I've worked on open-source projects including EtherCalc and Sugar Labs, including work around mesh networking, and more recently my focus has been heavily centered on **libp2p, IPFS, IPLD and Multiformats**.

Over the past several years I've contributed across multiple libp2p implementations and maintained projects including py-libp2p, py-multiaddr, multihash, multicodec, multibase, py-cid and related IPLD libraries. I've also contributed across JavaScript, Rust, Go and .NET/libp2p ecosystems.

My focus is generally on the layer where **protocol design, implementation, interoperability and real-world infrastructure meet**.

I'm particularly interested in questions such as how decentralized networks discover peers, establish secure connections, operate across NATs and heterogeneous networks, and remain observable and resilient as they scale.

---

### 2. What led you to AGNTCY?

**Manu:**
For me, it started with the networking architecture.

When I began looking at AGNTCY, I immediately recognized many of the distributed-systems primitives that I've worked with through libp2p: **Peer IDs, secure peer-to-peer communication, Kad-DHT, GossipSub, RPC and content addressing**.

What made it especially interesting was that these primitives were being applied to a new workload: **autonomous agents**.

AGNTCY's Directory architecture uses libp2p-based networking, decentralized discovery and content-addressed data to support agent discovery and communication. 

That raised an interesting question for me:

> What happens when the thing we're trying to discover isn't simply a peer or piece of content, but a capability?

That takes traditional P2P networking into a new and very interesting direction.

**Johanna:**
From my perspective, AGNTCY is interesting because of the ecosystem problem surrounding agents.

We're seeing rapid development of AI agents, but there is a real risk of fragmentation. Different platforms could end up creating their own identities, discovery mechanisms, communication protocols and infrastructure.

AGNTCY provides an opportunity to create a more open foundation where different agents, organizations and systems can interact.

That aligns strongly with the work we're doing around libp2p: building open infrastructure that can become a common layer underneath different applications and ecosystems.

---

### 3. Did you have a business problem in mind when you first started looking into AGNTCY?

**Johanna:**
For me, it was primarily an ecosystem problem rather than a conventional business problem.

The question was:

> **How do we prevent the emerging agent ecosystem from becoming fragmented?**

If every organization creates its own agent platform, developers may have to build and maintain separate integrations everywhere.

The opportunity is to create common infrastructure that allows organizations to retain control over their systems while still being able to participate in a broader ecosystem.

That's a pattern we've seen repeatedly in Web3. Strong infrastructure becomes much more valuable when different communities can build on it without having to ask permission from a central platform.

**Manu:**
I approached it from the distributed-systems side.

The question I was interested in was:

> **How do we build a networking foundation for potentially millions of agents that need to discover and communicate with each other across organizational and infrastructure boundaries?**

That requires solving many familiar P2P problems—identity, discovery, routing, secure communication, NAT traversal and observability—but the semantics are different because we're now discovering **capabilities and services**, not just peers.

---

### 4. Please tell us a bit more about this issue.

**Manu:**
There are several layers to the problem.

A simplified agent interaction looks something like:

```text
Agent
  ↓
Identity
  ↓
Capability Discovery
  ↓
Routing
  ↓
Secure Connection
  ↓
Metadata / Content
  ↓
Agent Communication
  ↓
Application
```

Every layer introduces questions around security, reliability and interoperability.

For example:

* Who is the peer?
* What capability does it provide?
* How do I discover it?
* How do I know the information is authentic?
* Can I reach it behind NAT?
* How do I establish a secure connection?
* How do I retrieve its metadata?
* How do I measure the health of the underlying network?

AGNTCY's use of content addressing is particularly interesting because CIDs provide stable, verifiable references to content rather than depending entirely on where that content happens to be hosted. 

**Johanna:**
There is also an organizational dimension.

Agents won't necessarily live in one environment. One could run inside a large enterprise, another in a cloud environment, another locally on a developer's machine, and another within a decentralized network.

So the infrastructure has to accommodate different trust models, deployment models and operational requirements.

That's why the possibility of **hybrid networking** is so important. An organization shouldn't have to choose between centralized operational control and participation in an open ecosystem.

---

### 5. Where are you in the process of applying AGNTCY — trial, POC, deployment?

**Johanna:**
I'd describe our current involvement as **active ecosystem and technical exploration, contribution and collaboration**, rather than positioning it as a production deployment of an AGNTCY application.

We're exploring how AGNTCY can connect with the broader libp2p ecosystem, how developers and organizations could use it, and what kinds of partnerships and real-world experiments would be useful.

For me, the important next step is getting more developers, researchers and organizations experimenting with these systems and feeding their requirements back into the community.

**Manu:**
On the technical side, I've been studying the architecture and its use of libp2p, Kad-DHT, GossipSub, RPC and content addressing.

I'm particularly interested in:

* interoperability;
* network observability;
* DHT performance;
* connectivity;
* routing;
* testing;
* security;
* and large-scale network measurement.

So I see this as an active collaboration between the AGNTCY and libp2p communities rather than simply consuming AGNTCY as an end user.

---

# 6. What do you hope to achieve with AGNTCY? Have you seen any tangible payoff yet?

**Manu:**
I'd like to see AGNTCY become a strong example of how decentralized networking foundations can support a new class of distributed applications.

One area I'm especially interested in is **network observability**.

Imagine being able to follow an interaction across:

```text
Network Health
      ↓
Peer Connectivity
      ↓
DHT Discovery
      ↓
Agent Discovery
      ↓
Metadata Retrieval
      ↓
Agent Communication
      ↓
Application Outcome
```

That gives us the possibility of connecting infrastructure-level metrics to agent-level behaviour.

AGNTCY provides a very interesting workload for exploring metrics such as DHT latency, peer connectivity, relay utilization, propagation and agent discovery latency. 

**Johanna:**
The payoff I care about is the ecosystem feedback loop.

When developers and organizations actually experiment with infrastructure, they reveal requirements that aren't always obvious during protocol design.

That helps us understand:

* what developers need;
* where integrations are difficult;
* what infrastructure needs to improve;
* which use cases are emerging;
* and where partnerships can accelerate adoption.

That's how I think open ecosystems grow: **build, experiment, measure, learn and iterate together**.

---

### 7. What, if anything, has surprised you about working with or using AGNTCY?

**Manu:**
The biggest surprise has been how familiar the fundamental problems are.

Agents sound like a completely new category of software, but underneath we're still dealing with:

* identity;
* discovery;
* routing;
* messaging;
* trust;
* connectivity;
* security;
* observability.

What's new is the semantic layer.

Traditional P2P networking might ask:

> "Which peer has this content?"

Agent networking increasingly asks:

> **"Which peer has the capability I need?"**

That changes routing and discovery in interesting ways.

**Johanna:**
I've been pleasantly surprised by the breadth of the collaboration opportunity.

AGNTCY isn't just an AI problem. It touches networking, security, identity, infrastructure, enterprise architecture and open-source ecosystems.

That creates an opportunity to bring communities together that don't always interact closely enough.

---

### 8. Do you have any plans to expand your use of AGNTCY?

**Johanna:**
Yes. I'd like to expand the ecosystem around the technology by bringing in more developers, researchers, infrastructure providers and organizations with real workloads.

I'm particularly interested in pilots where we can test agent infrastructure under realistic conditions rather than only in controlled demonstrations.

I also see strong opportunities around AI agents and payments, where reliable and interoperable communication infrastructure could become increasingly important.

**Manu:**
Technically, there are several areas I'd like to explore further.

### Network observability

Including:

* DHT lookup latency;
* peer churn;
* relay utilization;
* NAT traversal;
* connection establishment;
* transport selection;
* routing behaviour.

### Agent-level observability

Connecting network metrics with:

* agent discovery;
* metadata retrieval;
* RPC performance;
* propagation;
* federation health.

### Routing

I'm particularly interested in:

* capability-aware routing;
* semantic discovery;
* trust-aware routing;
* locality-aware peer selection;
* adaptive routing.

These build naturally on existing libp2p routing primitives. 

---

### 9. Tell us specifically about what you've contributed back to AGNTCY.

**Manu:**
My contribution has primarily been around **technical analysis, architecture, documentation and connecting the AGNTCY and libp2p communities**.

I've worked through how the Directory uses:

* go-libp2p;
* Peer IDs;
* Kad-DHT;
* GossipSub;
* libp2p RPC;
* CIDs;
* datastore primitives;
* and P2P communication.

One objective was to make the relationship between AGNTCY and libp2p easier for the broader networking community to understand.

The important point is that libp2p isn't simply a dependency. It provides foundational networking capabilities while AGNTCY operates at a higher layer focused on agents and agent interoperability.

We've also identified potential areas for deeper collaboration around observability, interoperability, routing, performance, testing and security.

**Johanna:**
My contribution has been more focused on **ecosystem development, partnerships, strategy and creating pathways toward adoption**.

A lot of ecosystem work is about creating the conditions for technical contributors to succeed.

That means helping researchers find builders, builders find users, projects find funding, and different communities find each other.

For AGNTCY and libp2p, I see that as helping build a bridge between the agent ecosystem and the broader decentralized networking ecosystem.

---

# 10. Have you introduced others to AGNTCY? What would you say to other people thinking about contributing to or deploying AGNTCY?

**Johanna:**
Yes, and my advice would be: **start experimenting early**.

You don't need to have the entire agent architecture figured out before participating.

Build a small experiment. Connect an agent. Test discovery. Try an integration. Identify what doesn't work. Then bring those findings back to the community.

Open ecosystems become strong through that feedback loop between developers, researchers, users and protocol designers.

And contribution isn't limited to code. Documentation, testing, security research, developer experience, use cases and ecosystem building are all valuable.

**Manu:**
For networking and distributed-systems engineers, I'd say:

> **You don't need to become an AI expert to contribute to agent infrastructure.**

If you understand peer discovery, routing, secure communication, distributed identity, Pub/Sub or network observability, you already have expertise that is directly relevant.

AGNTCY is an opportunity to apply many of those established networking concepts to a new workload.

And importantly, the relationship works in both directions. Agent workloads can expose new requirements that ultimately improve the underlying networking infrastructure for everyone.

---

### 11. Is there a graphic or a URL we can include in your story? Can we link to your LinkedIn profiles?

**Johanna:**
We'd suggest a simple architecture graphic showing how the ecosystem layers connect.

**Manu:**

```text
                    AGNTCY
          Agent Identity & Discovery
                       │
                       ▼
              Content Addressing
                    / CIDs
                       │
                       ▼
                   Kad-DHT
              Provider Discovery
                       │
                       ▼
                    libp2p
        ┌──────────────┼──────────────┐
        │              │              │
   Peer Identity   GossipSub         RPC
        │              │              │
        └──────────────┼──────────────┘
                       ▼
              Secure P2P Network
                       │
                       ▼
             Agent Communication
```

The key message is that the two projects operate at complementary layers: **libp2p provides reusable networking primitives, while AGNTCY builds higher-level agent discovery, identity and coordination capabilities.** 

**Johanna:**
For public links, we'd suggest:

* [AGNTCY](https://agntcy.org)
* [AGNTCY GitHub](https://github.com/agntcy)
* [libp2p](https://libp2p.io)
* [libp2p GitHub](https://github.com/libp2p)
* [IPFS](https://ipfs.tech)

We'd provide our preferred LinkedIn URLs directly to the AGNTCY team for inclusion.

---

### 12. Looking ahead — what are you most looking forward to, or most excited about?

**Manu:**
I'm most excited about the point where **agent networking becomes a first-class distributed-systems problem**.

Today we might ask:

> "Can I find an agent?"

Tomorrow we need to ask:

> **Can I find the right capability, verify its identity and metadata, establish a trustworthy connection, understand the network conditions around it, and communicate with it securely and reliably?**

That brings together decentralized discovery, routing, identity, security, observability and interoperability.

I'm particularly excited about capability-aware routing, network measurement, interoperable agent protocols and resilient P2P infrastructure.

**Johanna:**
I'm excited about seeing these technologies move from interesting architecture into **real ecosystems and real usage**.

Agents are likely to become an important interface through which people and organizations interact with software and services.

If we can help ensure that the infrastructure underneath those agents remains open and interoperable rather than becoming controlled by a small number of platforms, that could have a very significant long-term impact.

For me, the exciting part is connecting the right researchers, developers, enterprises and communities so that we can actually make that vision happen.

---

### 13. Could you describe AGNTCY, or your AGNTCY experience, in one word?

**Johanna:**
**Connection.**

Because I think about AGNTCY not only as connecting agents, but as connecting **people, organizations, protocols and ecosystems**.

**Manu:**
**Interoperability.**

Because the technical opportunity is to allow different agents, capabilities and organizations to communicate without requiring everyone to run exactly the same infrastructure.

**Johanna & Manu:**
If we can use two words:

> **Open interoperability.**

That's probably the best description of what excites us about AGNTCY.

The opportunity is to create an ecosystem where agent infrastructure remains **open, composable and interoperable**, while benefiting from mature decentralized networking foundations such as libp2p and content-addressing technologies. AGNTCY's broader vision similarly emphasizes secure, interoperable and decentralized communication across distributed systems. 

---

### Closing statement

**Johanna:**

> "The opportunity with AGNTCY is bigger than building another agent platform. It's about creating the ecosystem conditions for agents, developers, organizations and protocols to work together."

**Manu:**

> "And underneath that ecosystem, we need open networking foundations that make discovery, identity, communication, interoperability and security work reliably at scale."

**Johanna, Manu and core contributors in Libp2p Community**

> **"That's what makes the intersection of AGNTCY and libp2p so exciting: connecting an emerging agent ecosystem with proven open infrastructure for decentralized communication."**
