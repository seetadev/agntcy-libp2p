### AGNTCY Contributors Profile — Johanna Moran and Manu Sheel Gupta

Technical Contributions via Github and WG meetings: Manu Sheel Gupta (Github: https://github.com/seetadev)

### 1. Please tell us a bit more about your background.

Manu: My background is in distributed systems, open-source networking, and decentralized infrastructure. I've spent much of my work around **libp2p, IPFS, IPNS, IPLD, and Multiformats**, with a particular focus on peer-to-peer communication, distributed discovery, content addressing, identity, and building resilient infrastructure for the open Internet.

I am particularly interested in the networking problems that tend to sit underneath applications: **How do peers discover each other? How do they establish secure connections? How do we make those connections work across NATs and heterogeneous networks? How do we measure whether a decentralized network is actually healthy? And how do we make different implementations and ecosystems interoperable?**

I've also been increasingly involved in standards and research discussions around large-scale P2P systems. One of the areas I'm exploring is a common measurement and telemetry framework that can be applied across networks such as Ethereum, IPFS, Filecoin and libp2p-based systems.

That perspective naturally led me toward AGNTCY. Agent systems are introducing a new class of distributed applications, but underneath the agent layer are many of the same problems we've been working on in decentralized networking for years: identity, discovery, routing, communication, interoperability and observability.

---

### 2. What led you to AGNTCY?

What initially attracted me to AGNTCY was that it wasn't approaching agents simply as an application-layer problem.

The more I looked at the Directory architecture, the more I saw familiar distributed-systems primitives underneath it: **libp2p peer identity, Kad-DHT, GossipSub, RPC, content addressing and CIDs**.

That made the project particularly interesting from a libp2p perspective. AGNTCY is trying to solve a genuinely difficult problem: how do agents discover and communicate with each other across organizational and infrastructure boundaries without making the entire ecosystem dependent on one centralized service?

The current architecture uses libp2p as part of that networking foundation. The Directory can use the DHT for provider discovery, GossipSub for propagating announcements, and libp2p RPC for retrieving richer metadata after discovery. CIDs provide stable, content-addressed references to agent artifacts and metadata. 

For me, that was a very natural point of entry.

I didn't come to AGNTCY thinking, "I need to find an agent platform." I came to it from the networking side and realized that **agent ecosystems are becoming an important new workload for decentralized networking**.

---

### 3. Did you have a business problem in mind when you first started looking into AGNTCY?

For me, it was less of a traditional business problem and more of a **systems and ecosystem problem**.

The question was:

> **How do we build an open networking foundation for an ecosystem where potentially millions of agents, tools, services and organizations need to discover and communicate with one another?**

If every agent ecosystem builds its own networking stack, identity system, discovery mechanism and communication protocol, we are going to end up with another fragmented Internet.

That is one of the things I found compelling about AGNTCY. It is trying to establish higher-level protocols for agents while being able to leverage existing networking primitives rather than reinventing them.

libp2p provides things like peer identity, secure communication, discovery, routing, Pub/Sub, NAT traversal and connection management. 

So the opportunity I saw was to help make the **networking layer underneath agent systems more interoperable, observable, secure and resilient**.

---

### 4. Please tell us a bit more about this issue.

The Internet has historically solved many of these problems through centralized infrastructure.

You have a DNS provider, cloud provider, API gateway, database, identity provider, load balancer and so on. That works extremely well for many applications, but agent ecosystems are likely to be much more heterogeneous.

Imagine an environment where:

* one agent runs in a cloud environment;
* another runs inside an enterprise;
* another runs locally;
* another is operated by an individual developer;
* agents use different models and frameworks;
* different organizations have different security and trust requirements;
* and agents need to discover capabilities dynamically.

You need common mechanisms for **identity, discovery, communication and interoperability**.

AGNTCY's architecture is interesting because it separates those concerns. For example, a simplified discovery flow can be:

```text
Agent metadata
      ↓
Content Identifier
      ↓
Kad-DHT provider discovery
      ↓
Peer discovery
      ↓
libp2p communication
      ↓
RPC metadata retrieval
```

The DHT doesn't have to carry every piece of metadata. It can help locate the provider, while richer information can subsequently be retrieved from the peer. That separation is important for scalability. 

The bigger challenge is then making this system **observable and operationally understandable at scale**.

Once you have thousands or millions of agents, it isn't enough to know that an agent exists. You need to know:

* Can I reach it?
* How quickly can I discover it?
* Is the DHT healthy?
* Are announcements propagating?
* Which transports are being used?
* Are peers behind NAT?
* Are relays becoming bottlenecks?
* Are particular regions or organizations partitioned?
* Is the problem the application, discovery system or underlying network?

Those questions are where I think AGNTCY and the libp2p community can do some particularly interesting work together.

---

### 5. Where are you in the process of applying AGNTCY — trial, POC, deployment?

I'd describe my involvement as **active technical exploration, contribution and ecosystem collaboration**, rather than positioning it as a production deployment of a commercial AGNTCY application.

I'm looking at AGNTCY from several connected perspectives:

1. **Architecture** — understanding how the Directory uses libp2p, Kad-DHT, GossipSub, RPC and content addressing.
2. **Interoperability** — understanding how AGNTCY can coexist with other emerging agent protocols.
3. **Observability** — exploring how we can measure both the P2P network and the agent-discovery layer.
4. **Testing** — thinking about how different implementations can be tested against common networking behaviours.
5. **Research** — exploring areas such as routing, connectivity, identity and resilient decentralized discovery.

The current AGNTCY architecture already provides a very interesting real-world workload for libp2p. The project uses libp2p for peer identity and communication, Kad-DHT for distributed discovery, GossipSub for announcements and libp2p RPC for metadata retrieval. 

So I see my involvement as sitting at the intersection of **contributing to AGNTCY and bringing lessons from the broader libp2p ecosystem into AGNTCY**.

---

### 6. What do you hope to achieve with AGNTCY? Have you seen any tangible payoff yet?

The biggest thing I hope to achieve is a more **open and interoperable networking foundation for agent systems**.

I don't think the long-term goal should be simply "make agents discoverable." We should eventually be able to discover agents based on capabilities, establish secure communication, understand their network context, and operate these systems reliably across organizational boundaries.

The architecture already points in that direction. AGNTCY can combine centralized services with decentralized discovery, private infrastructure with public networking, and enterprise gateways with peer-to-peer communication. 

For me, the tangible payoff so far has been the ability to take concepts from the libp2p ecosystem and apply them to a rapidly emerging workload.

Agent systems give us a very interesting test case for questions we've been asking in decentralized networking for years.

For example:

> What does discovery look like when the thing you're discovering isn't just a peer, but a capability?

That leads to research around **capability-aware routing, semantic discovery, trust-aware routing, locality-aware peer selection and intelligent caching**. 

That feedback loop between a real application ecosystem and foundational networking research is probably the most valuable payoff for me.

---

### 7. What, if anything, has surprised you about working with or using AGNTCY?

One thing that surprised me positively is **how naturally the agent problem maps onto established distributed-systems concepts**.

AI agents sound like a completely new category of software, but when you start looking underneath, many of the hard problems are familiar:

* identity;
* discovery;
* routing;
* messaging;
* trust;
* connectivity;
* observability;
* interoperability.

What is different is the **semantics of what we're discovering and communicating**.

In traditional P2P systems, we might discover a peer or a content object.

With agents, we increasingly want to discover:

> **"Find me a peer that has this capability, meets these constraints and can securely communicate with me."**

That changes the networking problem quite substantially.

I've also been impressed by how much room there is for collaboration between communities. AGNTCY doesn't need to replace libp2p, and libp2p doesn't need to become an agent framework. The layers can remain separate and complementary. The AGNTCY documentation itself describes this relationship as complementary: libp2p provides networking primitives while AGNTCY builds higher-level agent protocols and services. 

That separation of concerns is something I really value.

---

### 8. Do you have any plans to expand your use of AGNTCY?

Yes. I see several areas where I'd like to continue contributing.

### 1. Network observability

I'd like to explore better visibility into:

* DHT lookup latency;
* connection establishment;
* peer churn;
* relay utilization;
* NAT traversal;
* transport negotiation;
* routing paths;
* resource consumption.

These are important because decentralized networks are difficult to operate without understanding what is happening underneath. 

### 2. End-to-end agent observability

The next layer is connecting those network measurements to agent-level measurements:

```text
Network
   ↓
Peer connectivity
   ↓
DHT discovery
   ↓
Agent discovery
   ↓
Metadata retrieval
   ↓
Agent communication
   ↓
Application outcome
```

This could eventually provide an end-to-end view of agent-network health.

### 3. Interoperability

I am particularly interested in how libp2p can serve as a networking substrate for multiple agent protocols rather than creating another isolated ecosystem.

AGNTCY, A2A, MCP, SLIM and enterprise-specific protocols don't necessarily need to share the same application protocol to benefit from common networking primitives. libp2p is explicitly application-agnostic and can support multiple protocols over the same networking layer. 

### 4. Measurement and testing

I'd like to explore standardized ways of measuring large-scale P2P deployments so that AGNTCY operators and libp2p developers can reason about the same metrics.

### 5. Routing research

Capability-aware and trust-aware routing are particularly interesting to me.

Traditional routing asks:

> "Which peer should I contact?"

Agent networking increasingly needs to ask:

> "Which peer can provide the capability I need, and which path gives me the best security, reliability and performance?"

That is a very interesting research problem.

---

### 9. Tell us specifically about what you've contributed back to AGNTCY.

My contribution has primarily been around **technical analysis, networking architecture, ecosystem collaboration, and identifying concrete areas where the libp2p community can contribute**.

One of the things I worked on was documenting the relationship between AGNTCY and libp2p in detail—looking at how the Directory architecture uses:

* the libp2p Host;
* Peer IDs;
* Kad-DHT;
* GossipSub;
* libp2p RPC;
* IPFS CIDs and content addressing;
* datastore primitives;
* and the interaction between external APIs and P2P communication.

The purpose was not simply to document dependencies. It was to explain **why these layers matter and where the two communities can collaborate**.

For example, the architecture uses the DHT to advertise and discover providers while retrieving richer metadata through libp2p RPC. That gives us a clean separation between discovery and metadata exchange. 

I've also been thinking about the next layer of contribution:

**How do we make this network measurable?**

That includes things like:

* DHT performance;
* discovery latency;
* peer connectivity;
* relay dependence;
* NAT traversal;
* transport selection;
* propagation;
* routing;
* application-level discovery latency.

The AGNTCY architecture gives us a very compelling real-world environment in which to develop and test those ideas. The project itself identifies network and application observability as important future areas. 

So I'd describe my contribution as **connecting AGNTCY's agent-layer requirements with the deeper research, engineering and operational capabilities of the libp2p ecosystem**.

---

### 10. Have you introduced others to AGNTCY? What would you say to other people thinking about contributing to or deploying AGNTCY?

Yes. A major part of my involvement has been bringing the AGNTCY architecture into conversations with people working on **libp2p, IPFS, Filecoin and decentralized networking**.

I think AGNTCY is particularly interesting for people who don't necessarily think of themselves as "AI people."

If you're a networking engineer, distributed-systems researcher, protocol developer, security researcher or infrastructure operator, there are already many familiar problems here.

My advice would be:

> **Don't start by thinking about agents. Start by thinking about the distributed-systems problem underneath agents.**

Look at identity, discovery, routing, communication, observability and interoperability. Then ask what changes when the nodes in your network are autonomous agents with capabilities rather than conventional services.

There are many ways to contribute without building an entire agent platform. The AGNTCY community can benefit from networking expertise, transport improvements, routing research, observability, cross-implementation testing, performance optimization, documentation, security reviews and developer tooling. 

And importantly, contribution works both ways. AGNTCY provides a new and very interesting workload for libp2p. Real-world agent deployments can expose networking requirements that ultimately improve the underlying protocols for everyone. 

---

### 11. Is there a graphic or a URL we can include in your story? Can we link to your LinkedIn profile?

I'd suggest including a simple architecture graphic showing:

```text
                 AGNTCY
        Agent Identity & Discovery
                    │
                    ▼
          Content Addressing / CIDs
                    │
                    ▼
             Kad-DHT Discovery
                    │
                    ▼
              libp2p Network
          ┌─────────┼─────────┐
          ▼         ▼         ▼
       GossipSub   RPC     Peer Identity
          │         │         │
          └─────────┼─────────┘
                    ▼
        Secure Agent Communication
```

The important message in the graphic should be that **AGNTCY operates at the agent/protocol layer while libp2p provides reusable networking primitives underneath it**. That architectural distinction is central to understanding the collaboration. 

For links, I would include:

* **AGNTCY:** [agntcy.org](https://agntcy.org)
* **AGNTCY GitHub:** [AGNTCY on GitHub](https://github.com/agntcy)
* **libp2p:** [libp2p.io](https://libp2p.io)
* **libp2p GitHub:** [libp2p on GitHub](https://github.com/libp2p)
* **IPFS:** [IPFS.tech](https://ipfs.tech)

For the LinkedIn profile, I'd use your preferred public profile URL supplied directly to the AGNTCY team rather than putting an unverified profile URL into the submission.

---

### 12. Looking ahead — what are you most looking forward to, or most excited about, with AGNTCY or this space?

I'm most excited about **what happens when agent ecosystems become large enough that networking itself becomes part of the intelligence and security problem**.

Today, we tend to think of agent discovery as:

> "Can I find an agent?"

Tomorrow, I think the question becomes:

> **"Can I discover the right capability, establish a trustworthy connection, understand the network conditions around it, and communicate with it securely and reliably across organizational boundaries?"**

That brings together agent identity, decentralized discovery, routing, observability, privacy and security.

I'm especially excited about exploring **capability-aware and trust-aware routing, end-to-end observability, and interoperable networking for heterogeneous agent protocols**.

I also think the intersection with decentralized infrastructure is going to be very important. The same principles that have been developed through libp2p, IPFS, Filecoin and Ethereum—open protocols, content addressing, cryptographic identity, decentralized discovery and resilient networking—can become foundational infrastructure for the next generation of autonomous systems.

---

### 13. Could you describe AGNTCY, or your AGNTCY experience, in one word?

**Interoperability.**

If I'm allowed two:

**Open interoperability.**

Because what excites me most is not simply connecting agents. It's creating an ecosystem where **different agents, protocols, organizations and infrastructure providers can communicate without requiring everyone to operate the same stack**.

That is also where I see the strongest connection between AGNTCY and libp2p: both are ultimately trying to make distributed systems work across boundaries while keeping the underlying infrastructure open and composable. The shared vision is explicitly around secure, interoperable and decentralized communication across distributed systems. 

