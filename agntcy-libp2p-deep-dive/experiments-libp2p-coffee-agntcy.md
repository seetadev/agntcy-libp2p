### How libp2p could improve AGNTCY outcomes for prospective customers

The CoffeeAGNTCY reference application is a useful way to demonstrate how A2A, SLIM, NATS, MCP, LangGraph, Identity, Observe, and Directory can work together in a multi-agent system.

One area where we think libp2p could add significant value is **the network layer underneath these application-level protocols**.

The important question we wish to uncover with agntcy deployments:

> **Can libp2p provide an open, resilient, interoperable connectivity substrate that allows AGNTCY deployments to move from controlled/reference environments toward large-scale, independently operated agent networks?**

This could be particularly valuable for prospective customers who will eventually need to connect agents running across different organizations, clouds, regions, networks, security domains, and infrastructure providers.

---

### 1. From "agent communication" to "agent connectivity"

CoffeeAGNTCY currently provides excellent examples of request/reply, unicast, group communication, pub/sub, streaming, A2A, and protocol-agnostic transports.

For production customers, however, the problem becomes broader:

* How does an agent discover another agent?
* How does it determine whether that agent is reachable?
* What happens when the agent is behind NAT?
* What happens when direct connectivity fails?
* How does an agent select the best transport?
* How does it maintain connectivity while network conditions change?
* How does it communicate across organizational boundaries?
* How can an operator understand why communication failed?
* How can the system continue operating when part of the network disappears?
* How can customers avoid creating a centralized dependency for every interaction?

This is where libp2p can complement the existing AGNTCY stack.

A useful architectural separation could therefore be:

**Application semantics**
→ A2A / MCP / agent protocols

**Agent orchestration**
→ LangGraph / AGNTCY application SDK

**Messaging**
→ SLIM / NATS / other messaging systems

**Discovery / identity / metadata**
→ AGNTCY Directory + identity mechanisms

**Connectivity substrate**
→ libp2p

**Network observability**
→ AGNTCY Observe + libp2p network telemetry

The goal would be to allow the application layer to remain protocol-agnostic while giving deployments a substantially stronger connectivity layer.

---

### 2. Customer outcome: "my agents can actually reach each other"

For a prospective enterprise customer, connectivity reliability is likely to matter more than the underlying transport technology.

A customer does not necessarily care whether the underlying connection uses TCP, QUIC, WebTransport, WebRTC, or a relay.

They care about:

> "When Agent A needs Agent B, can the system establish a connection and complete the interaction?"

libp2p already has primitives for:

* Peer IDs
* multiaddresses
* transport negotiation
* QUIC
* TCP
* WebSockets
* WebTransport
* WebRTC
* NAT traversal
* hole punching
* relays
* connection management
* multiplexed streams
* peer routing
* DHT-based discovery
* pub/sub
* connection lifecycle management

This provides an opportunity to expose a higher-level concept to AGNTCY:

### Agent Connectivity

Instead of applications having to understand network topology, an agent could ask:

```text
connect(agent_id)
```

and libp2p would determine the appropriate path.

Conceptually:

```text
Agent A
   |
   v
AGNTCY Agent SDK
   |
   v
Connectivity Adapter
   |
   v
libp2p Host
   |
   +---- direct QUIC
   |
   +---- WebTransport
   |
   +---- WebRTC
   |
   +---- NAT hole punch
   |
   +---- relay
   |
   v
Agent B
```

This could significantly simplify the deployment story.

---

### 3. NAT traversal is especially relevant for real-world agents

Many agent deployments will not run in public cloud environments with directly reachable addresses.

Agents may run:

* on laptops
* inside corporate networks
* behind enterprise firewalls
* inside Kubernetes clusters
* on edge devices
* in private data centers
* behind CGNAT
* on mobile networks
* in home networks
* inside customer-controlled infrastructure

This is a natural problem space for libp2p.

Rather than requiring customers to expose every agent through publicly accessible endpoints, libp2p could provide:

**Discovery → address observation → hole punching → relay fallback → connection establishment**

This creates a much better customer experience.

For example:

```text
Customer A Agent
      |
   private NAT
      |
      |  libp2p hole punch
      |
      +--------------------+
                           |
                       Customer B
                           |
                      private network
                           |
                       Agent B
```

If direct connectivity fails:

```text
Agent A
   |
   | encrypted stream
   v
Relay
   |
   v
Agent B
```

This is particularly interesting for enterprise deployments where exposing inbound ports is undesirable or impossible.

---

### 4. Directory + libp2p could become a powerful discovery combination

AGNTCY Directory provides a natural place to discover agents and their capabilities.

libp2p can complement that with **network-level reachability**.

This creates an important distinction:

### Semantic discovery

"What agent can perform this task?"

versus

### Network discovery

"How can I actually reach that agent?"

A customer might search the Directory for:

```text
capability = invoice-processing
region = EU
trust-domain = company-x
protocol = A2A
```

and receive an agent identity.

libp2p can then resolve that identity into usable network connectivity:

```text
AgentID
   ↓
PeerID
   ↓
provider/address discovery
   ↓
reachable addresses
   ↓
transport negotiation
   ↓
NAT traversal / relay
   ↓
secure connection
```

This separation could be very useful as AGNTCY evolves toward larger agent ecosystems.

---

### 5. Capability-aware and locality-aware routing

There is another opportunity beyond basic connectivity.

Once the network has information about peers and their connectivity characteristics, routing decisions could incorporate:

* latency
* geographic locality
* network reliability
* observed availability
* transport support
* relay dependency
* bandwidth
* historical success rate
* organizational trust domain
* privacy requirements
* cost

For example, an agent could discover three equivalent agents:

```text
Agent A
Latency: 40 ms
Reliability: 99.9%
Direct: yes

Agent B
Latency: 180 ms
Reliability: 98.1%
Relay: yes

Agent C
Latency: 70 ms
Reliability: 99.5%
Direct: yes
```

The AGNTCY routing layer could select Agent A.

This becomes particularly interesting when combined with semantic agent discovery.

The future query could effectively become:

> "Find me an agent capable of performing X, within my trust policy, preferably in this region, with low latency and high observed availability."

Directory answers **who can do it**.

libp2p telemetry answers **who can I reach efficiently and reliably**.

Together they provide a much more complete agent discovery model.

---

### 6. Resilience against infrastructure failures

A centralized messaging architecture can work extremely well within a controlled environment.

But prospective customers may eventually ask:

> What happens when the messaging service is unavailable?

or:

> What happens when one region, cloud provider, relay cluster, or network path fails?

libp2p's decentralized connectivity model allows multiple paths to exist.

For example:

```text
                +--- Agent B
                |
Agent A --------+--- Relay 1
                |
                +--- Relay 2
                |
                +--- Agent C
```

If one path fails, the connectivity layer can attempt another.

This provides a useful resilience property:

**application-level availability does not necessarily have to equal availability of a single messaging infrastructure component.**

This could be particularly valuable for:

* critical enterprise workflows
* financial agents
* infrastructure automation
* edge agents
* disaster-response systems
* cross-cloud deployments
* decentralized applications

---

### 7. Multiplexing can reduce operational complexity

A multi-agent system can produce a large number of logical communication relationships.

Instead of creating independent network connections for every interaction, libp2p's stream multiplexing can provide multiple logical streams over a connection.

Conceptually:

```text
                 libp2p connection
                       |
          +------------+-------------+
          |            |             |
       A2A stream   MCP stream   control stream
          |            |             |
       workflow      tools       metadata
```

This can reduce connection-management overhead and provide a cleaner abstraction for applications.

It also opens the door to prioritization.

For example:

```text
Priority 1: control / security
Priority 2: workflow messages
Priority 3: streaming responses
Priority 4: telemetry
```

This is worth exploring for large multi-agent workflows.

---

### 8. A2A over libp2p

I think one of the most interesting experiments would be a native A2A transport binding over libp2p.

The goal would not be to modify A2A semantics.

Instead:

```text
A2A
 |
 +--- HTTP
 |
 +--- existing transports
 |
 +--- libp2p stream
```

A2A messages could be carried over authenticated libp2p streams.

This gives applications:

* peer identity
* encrypted connections
* multiplexing
* NAT traversal
* relay fallback
* transport agility
* connection reuse
* peer-level telemetry

without requiring A2A applications to understand the underlying network.

This could make an excellent CoffeeAGNTCY experiment.

For example:

```text
Corto / Lungo
     |
     v
A2A client
     |
     v
AGNTCY transport abstraction
     |
     v
libp2p stream
     |
     v
remote A2A agent
```

The same application workflow could then run with:

```text
A2A + SLIM
A2A + NATS
A2A + libp2p
```

This would make the comparison much more meaningful.

---

### 9. SLIM + libp2p rather than SLIM versus libp2p

I would avoid positioning this as a replacement discussion.

There is potentially a more interesting architecture:

**SLIM provides agent messaging semantics while libp2p provides connectivity.**

For example:

```text
Agent
 |
 v
SLIM
 |
 v
libp2p
 |
 +--- direct connection
 +--- QUIC
 +--- WebRTC
 +--- relay
 +--- NAT traversal
 |
 v
Remote SLIM
 |
 v
Agent
```

This gives AGNTCY the ability to retain its existing communication abstraction while gaining a more flexible network substrate.

The same idea could potentially apply to other messaging systems.

---

### 10. Protocol-agnostic connectivity

CoffeeAGNTCY already emphasizes protocol-agnostic bridges and reusable transports.

libp2p fits naturally into that philosophy.

Instead of defining connectivity around a single application protocol:

```text
A2A → Network
```

we could have:

```text
             +--- A2A
             |
Application -+--- MCP
             |
             +--- SLIM
             |
             +--- custom protocol
                     |
                     v
               libp2p streams
                     |
                     v
                  Network
```

This means AGNTCY components can evolve independently from the underlying networking stack.

That could become particularly important as agent protocols continue to evolve.

---

### 11. Stronger observability: from application traces to network traces

The existing Observe SDK gives AGNTCY application-level observability.

libp2p can add another layer:

### Application observability

* agent invocation
* workflow duration
* tool calls
* A2A messages
* LLM latency
* workflow failures

### Network observability

* peer discovery latency
* connection establishment latency
* transport selected
* NAT traversal success
* relay usage
* connection churn
* stream failures
* packet loss indicators
* RTT
* peer availability
* DHT lookup latency
* provider discovery latency
* message propagation
* connection retries

Combining the two creates a much more powerful diagnostic model.

For example:

```text
Workflow took 8 seconds
        |
        +--- LLM: 3.2s
        +--- Tool: 1.1s
        +--- A2A: 0.7s
        +--- connection establishment: 2.3s
                |
                +--- NAT traversal failed
                +--- relay fallback: 1.8s
```

Without network observability, the customer may simply see:

> "Agent response was slow."

With combined observability:

> "Agent response was slow because direct connectivity failed and the connection fell back to a relay."

That distinction has substantial operational value.

---

### 12. A Universal Agent Connectivity Observatory

This could potentially become a concrete AGNTCY/libp2p collaboration.

A common telemetry schema could capture:

```text
agent_id
peer_id
timestamp
transport
source_region
destination_region

discovery_latency
connection_latency
handshake_latency

nat_traversal
relay_used

rtt
stream_duration
connection_success
connection_failure

protocol
a2a_version
```

The data could feed the existing AGNTCY Observe infrastructure.

This would make it possible to build dashboards such as:

### Agent Connectivity Health

```text
Agent availability        99.94%
Direct connectivity        87.2%
Relay fallback             12.8%
Median connection time     84 ms
P95 connection time        420 ms
NAT traversal success      91.4%
```

This moves observability from:

**"what did my agent do?"**

toward:

**"why did my agent network behave this way?"**

---

### 13. Connectivity scoring for agent selection

A further extension could be a **Connectivity Score** associated with a PeerID.

For example:

```text
PeerID: 12D3Koo...
Capability: invoice-processing

Connectivity score: 96/100

Availability:       99.97%
Direct success:     94%
Median RTT:          42ms
Relay dependency:    3%
Recent failures:     0.4%
```

This could become one input into agent selection.

The Directory could provide:

```text
semantic capability
identity
metadata
```

while the connectivity layer provides:

```text
network health
reachability
performance
```

Together:

```text
Agent suitability =
capability
+ identity/trust
+ policy
+ connectivity
+ performance
```

That is potentially much more useful to an enterprise than semantic discovery alone.

---

### 14. Security benefits

libp2p can also contribute to the security model.

A PeerID gives the network a stable cryptographic identity independent of an IP address.

This is useful because network location and identity become separate concepts.

For example:

```text
Agent identity
      |
    PeerID
      |
 +----+----+
 |         |
IP addr   relay
 |         |
network   network
location  location
```

An agent can move between networks without necessarily changing its cryptographic identity.

This is especially valuable for mobile, edge, cloud, and multi-region deployments.

It can also provide a useful foundation for policy:

```text
Allow PeerID X
Allow trust domain Y
Deny peer Z
Require authenticated protocol
Require encrypted transport
```

This can complement AGNTCY Identity rather than compete with it.

---

### 15. Identity layering

It may be useful to explicitly distinguish:

### Human / organizational identity

Who owns or operates this agent?

### Agent identity

What logical agent is this?

### Network identity

What cryptographic peer is currently participating in the network?

libp2p can provide the network identity layer.

AGNTCY Identity can provide higher-level identity and authorization.

Directory can associate identities with capabilities and metadata.

Conceptually:

```text
Organization
     |
     v
AGNTCY Identity
     |
     v
Agent identity
     |
     v
PeerID
     |
     v
Network connectivity
```

This separation could be useful for enterprise security architectures.

---

### 16. Privacy-preserving networking

There is also a strong privacy angle.

An enterprise may not want every agent interaction to reveal:

* internal IP addresses
* infrastructure topology
* cloud region
* network architecture
* direct connectivity relationships

Relay-based connectivity can provide a useful privacy boundary.

For example:

```text
Customer A
   |
 private network
   |
 Agent A
   |
 encrypted relay
   |
 Agent B
   |
 private network
   |
Customer B
```

Neither customer necessarily needs to expose its internal network topology.

This becomes increasingly relevant as agents interact across organizational boundaries.

---

### 17. Federated agent networks

A particularly interesting future architecture is a federation of independently operated agent networks.

For example:

```text
Enterprise A
    |
  agents
    |
 libp2p
    |
    +----------------+
                     |
                  federation
                     |
    +----------------+
    |
 libp2p
    |
  agents
    |
Enterprise B
```

AGNTCY can provide common application protocols and discovery semantics.

libp2p can provide the underlying peer connectivity.

This allows customers to retain operational control over their own infrastructure while still participating in a larger agent ecosystem.

That could be a strong answer to the question:

> "How do we participate in an Internet of Agents without putting all of our agent traffic through one centralized provider?"

---

### 18. Edge and intermittently connected agents

Not every agent will be a cloud microservice.

Some could run on:

* factories
* vehicles
* robotics systems
* gateways
* IoT devices
* branch offices
* research infrastructure
* personal computers

These environments have very different connectivity characteristics.

libp2p's transport and connection-management model is well suited to environments where:

* addresses change
* connectivity is intermittent
* NAT is common
* peers appear/disappear
* direct connectivity is not guaranteed

This could make CoffeeAGNTCY more representative of the broader "Internet of Agents" vision.

---

### 19. Multi-cloud and cross-cloud deployments

Another concrete customer scenario:

```text
AWS
 ├── Agent A
 └── Agent B

Azure
 ├── Agent C
 └── Agent D

GCP
 ├── Agent E
 └── Agent F

On-prem
 └── Agent G
```

Customers should ideally not have to build bespoke networking between every environment.

A common libp2p connectivity layer could provide a uniform abstraction across these environments.

The application sees:

```text
PeerID → connect
```

rather than:

```text
AWS endpoint
Azure endpoint
VPN
firewall rule
load balancer
service mesh
NAT rule
```

This could significantly reduce integration complexity.

---

### 20. Connection migration and transport agility

Agents may change networks during their lifetime.

For example:

```text
WiFi
  ↓
5G
  ↓
corporate VPN
  ↓
cloud network
```

A peer-oriented connectivity model makes it possible to reason about the agent independently from its current network location.

This is potentially useful for mobile or edge agents.

It also allows AGNTCY deployments to support different transport requirements without changing application semantics.

---

### 21. DHT and decentralized discovery as an optional capability

AGNTCY Directory is likely to remain important for semantic and application-level discovery.

libp2p's DHT can provide an additional decentralized discovery mechanism for network-level information.

For example:

```text
Directory
   |
   +-- "Which agent provides capability X?"
   |
   v
Agent / PeerID
   |
   v
DHT
   |
   +-- addresses
   +-- providers
   +-- reachability
   |
   v
Connection
```

This does not require making every part of AGNTCY decentralized.

Instead, decentralized discovery can be introduced where it provides concrete value.

---

### 22. A practical CoffeeAGNTCY experiment

I think this could be tested without making a large architectural commitment.

Take the existing Corto or Lungo setup and introduce a libp2p transport adapter.

### Experiment 1: A2A over libp2p

Run:

```text
Agent A
  |
 A2A
  |
libp2p
  |
Agent B
```

Compare it against the current transport.

Measure:

* connection establishment
* message latency
* streaming performance
* reconnection behavior
* NAT traversal
* relay fallback

---

### Experiment 2: Hybrid transport

Allow:

```text
A2A
 |
 +-- SLIM
 +-- NATS
 +-- libp2p
```

Select the transport through configuration.

This would preserve the current architecture and allow empirical comparison.

---

### Experiment 3: Failure injection

Introduce:

* network partitions
* NAT
* relay-only connectivity
* peer churn
* packet loss
* high latency
* temporary agent disappearance

Measure:

```text
workflow success rate
recovery time
connection success rate
relay dependency
end-to-end latency
```

This would demonstrate whether libp2p improves actual customer outcomes rather than simply adding another technology.

---

### 23. A "Production Readiness" benchmark

It could also be useful to define an AGNTCY Agent Network benchmark.

For example:

| Dimension        | Metric                            |
| ---------------- | --------------------------------- |
| Discovery        | Time to discover suitable agent   |
| Connectivity     | Connection success rate           |
| NAT              | Hole-punch success                |
| Resilience       | Recovery after path failure       |
| Performance      | P50/P95 connection latency        |
| Availability     | Successful interactions over time |
| Routing          | Optimal peer/path selection       |
| Privacy          | Direct-address exposure           |
| Scalability      | Peers supported                   |
| Operations       | Time to diagnose failure          |
| Interoperability | A2A/SLIM/NATS compatibility       |

This could become a reusable evaluation framework for prospective customers.

Rather than telling a customer that a system is "distributed" or "resilient", AGNTCY could demonstrate measurable properties.

---

### 24. Customer-facing value propositions

I think the technical work becomes much easier to communicate if mapped directly to customer outcomes.

### "Agents work across network boundaries"

Enabled by:

* NAT traversal
* relays
* transport agility
* peer addressing

### "Agents remain reachable without exposing your infrastructure"

Enabled by:

* encrypted peer connections
* relays
* peer identity
* private-network-friendly connectivity

### "Agents can communicate across clouds"

Enabled by:

* common connectivity abstraction
* QUIC/TCP/WebRTC/WebTransport
* peer addressing

### "Failures do not automatically become workflow failures"

Enabled by:

* connection management
* retries
* multiple paths
* relay fallback
* peer routing

### "We can understand why agents are slow"

Enabled by:

* libp2p network telemetry
* AGNTCY Observe
* end-to-end tracing

### "We can choose the best agent, not just a capable agent"

Enabled by:

* Directory capability discovery
* connectivity measurements
* latency/reliability information
* policy-aware routing

### "We don't have to centralize all agent communication"

Enabled by:

* peer-to-peer connectivity
* decentralized discovery options
* federation

---

### 25. Potential AGNTCY/libp2p architecture

A longer-term architecture could look approximately like:

```text
                         AGNTCY
                            |
       +--------------------+---------------------+
       |                    |                     |
   Directory             Identity             Observe
       |                    |                     |
       +--------------------+---------------------+
                            |
                       Agent SDK
                            |
              +-------------+-------------+
              |                           |
          A2A / MCP                   SLIM/NATS
              |                           |
              +-------------+-------------+
                            |
                    Connectivity API
                            |
                         libp2p
                            |
        +---------+---------+---------+---------+
        |         |         |         |         |
       QUIC     WebRTC     WebTrans   TCP     Relay
        |         |         |         |         |
        +---------+---------+---------+---------+
                            |
                    Internet / Edge
                            |
                    Other Agent Peers
```

The key abstraction would be:

> **AGNTCY defines what agents know and do; libp2p helps them reliably find and reach one another.**

---

### 26. What I would prioritize first

I would not try to integrate every libp2p capability immediately.

A pragmatic roadmap could be:

### Phase 1 - Connectivity proof

* libp2p transport adapter
* PeerID mapping
* A2A over libp2p streams
* QUIC
* connection metrics
* basic CoffeeAGNTCY integration

### Phase 2 - Real-world networking

* NAT traversal
* hole punching
* relay fallback
* connection recovery
* multi-address handling

### Phase 3 - Discovery

* Directory ↔ PeerID mapping
* network address discovery
* DHT/provider discovery where appropriate
* capability + connectivity-aware selection

### Phase 4 - Observability

Integrate network telemetry with Observe:

* discovery latency
* connection latency
* transport
* NAT success
* relay usage
* RTT
* failures
* churn

### Phase 5 - Resilience evaluation

Build failure-injection scenarios and benchmark:

* direct connectivity
* NAT
* relay
* network partition
* peer churn
* cross-region deployment
* multi-cloud deployment

This would produce evidence that can be shown to prospective customers.

---

### 27. The bigger opportunity

The most interesting outcome may not be "CoffeeAGNTCY supports libp2p."

The larger opportunity is to establish a common **Agent Connectivity Layer**.

As the Internet of Agents grows, we will probably need to separate several concerns:

```text
Who is the agent?
        ↓
Identity

What can the agent do?
        ↓
Directory / capabilities

How should agents communicate?
        ↓
A2A / MCP / messaging protocols

How do they actually reach one another?
        ↓
Connectivity

Can we trust and measure the connection?
        ↓
Identity + Observability
```

libp2p has a particularly strong fit for the fourth layer.

This would allow AGNTCY to remain focused on agent interoperability while leveraging a mature peer-to-peer networking stack for the difficult realities of Internet connectivity.

---

