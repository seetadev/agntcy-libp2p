### AGNTCY Kademlia DHT Profile on HyperScalers

### Enterprise Agent Routing over libp2p

### Status

**Early Draft Specification**

Version: 0.1


### Abstract

The AGNTCY Kademlia Profile defines how libp2p's Kademlia Distributed Hash Table should operate inside enterprise agent ecosystems in Agntcy.

Unlike the public IPFS DHT, AGNTCY deployments are expected to operate across:

* enterprise organizations
* sovereign clouds
* government environments
* regulated industries
* hybrid public/private infrastructure

Consequently, routing decisions are governed not only by XOR distance but also by organizational policy, trust, authorization, and privacy constraints.

This specification extends—not replaces—the standard libp2p Kad-DHT.

---

### Design Goals

The AGNTCY DHT should provide:

* scalable peer discovery
* decentralized service discovery
* agent capability advertisement
* secure enterprise federation
* policy-aware routing
* privacy-preserving lookups
* interoperability across vendors

while respecting enterprise governance.

---

### Core Principle

> **The DHT discovers *where* an agent or capability exists, but enterprise policy determines *whether* it may be reached.**

Distance alone never grants access.

---

### Enterprise Boundaries

One of the primary design principles of AGNTCY is **respecting enterprise boundaries**.

Organizations should never be required to expose their internal agents, routing tables, metadata, or infrastructure to the global network merely to participate in decentralized agent discovery.

Instead, each enterprise maintains sovereignty over:

* which agents are publicly discoverable,
* which capabilities remain private,
* which external organizations may resolve or contact internal services,
* what metadata is advertised,
* and which routing information may cross organizational boundaries.

The DHT therefore becomes a **federated discovery layer**, not a globally shared directory.

Every routing decision must respect organizational policy before considering network proximity.

---

### Multi-Domain DHT

Instead of one global DHT:

```
Enterprise A
   │
   ├── Internal DHT
   │
Federation Gateway
   │
──────────────
   │
Enterprise B
   │
Internal DHT
```

Each enterprise may operate:

* internal Kad-DHT
* partner federation DHT
* public discovery DHT

using independent protocol identifiers.

---

### AGNTCY Protocol Prefix

Instead of

```
/ipfs/kad/1.0.0
```

AGNTCY recommends

```
/agntcy/kad/1.0.0
```

or organization-specific namespaces such as:

```
/agntcy/company-a
/agntcy/healthcare
/agntcy/finance
/agntcy/public
```

This prevents accidental participation in the public IPFS DHT while enabling multiple isolated overlays. 

---

### Enterprise Routing Policy

Before any lookup continues:

```
Distance Check
        ↓
Policy Check
        ↓
Authorization
        ↓
Continue Lookup
```

Routing SHOULD verify:

* enterprise membership
* federation agreements
* workload classification
* jurisdiction
* compliance requirements
* trust level
* access policies

before querying another peer.

---

### Agent Capability Records

Rather than storing only peer IDs, AGNTCY introduces **Capability Records** describing the services an agent offers.

Example:

```yaml
PeerID: 12D3KooW...
Organization: ExampleCorp
Capability:
  - Code Generation
  - Knowledge Retrieval
  - Scheduling
TrustLevel: Internal
Region: EU
Visibility:
  Public: false
  Partners: true
TTL: 12h
```

Applications may choose how much metadata to expose, minimizing information disclosure while enabling discovery.

---

### Organizational Trust Domains

Nodes belong to one or more trust domains:

```
Internal

Partner

Vendor

Public

Confidential
```

Lookup behavior depends on the requesting domain.

For example:

Internal → Internal ✓

Partner → Internal (policy)

Public → Internal ✗

---

### Routing Table Admission

Unlike public Kad-DHTs, enterprise deployments SHOULD NOT admit every reachable peer.

Admission SHOULD evaluate:

* enterprise identity
* organizational certificates
* policy engine decisions
* reputation
* workload authorization

before insertion.

This aligns naturally with libp2p's routing table filtering mechanisms while introducing enterprise-aware admission policies. 

---

### Query Peer Filters

Every lookup SHOULD support policy-aware peer selection.

Example filters include:

* same enterprise
* federation members
* region restrictions
* compliance domains
* authenticated peers only
* minimum trust score

Distance remains important but is not the sole criterion.

---

### Private Metadata

The DHT SHOULD avoid exposing sensitive information such as:

* internal topology
* employee identities
* infrastructure addresses
* confidential agent names
* proprietary capabilities
* workload descriptions

Only the minimum metadata required for discovery should be published.

---

### Gateway Federation

Enterprise gateways synchronize selected records between trust domains.

```
Internal DHT
      │
Federation Gateway
      │
Partner DHT
      │
Public DHT
```

Gateways enforce export policies and prevent accidental leakage of internal information.

---

### Suggested Parameter Profile

| Parameter            | Recommendation                               |
| -------------------- | -------------------------------------------- |
| Bucket Size (k)      | 20                                           |
| Parallelism (α)      | 5–10                                         |
| Query Resiliency (β) | 5                                            |
| Auto Refresh         | Enabled                                      |
| Operating Mode       | Server (gateways), Client/Auto (edge agents) |
| Query Peer Filter    | Policy-aware                                 |
| Routing Table Filter | Enterprise-aware                             |
| Protocol Prefix      | `/agntcy/kad/1.0.0`                          |
| Disjoint Query Paths | Enabled for federation gateways              |
| Record Filtering     | Enabled                                      |
| Provider Records     | Capability advertisements                    |
| Value Records        | Agent metadata                               |

These recommendations build upon the operational guidance for libp2p Kademlia while tailoring defaults to enterprise AI deployments. 

---

### Security Considerations

AGNTCY deployments SHOULD additionally support:

* mTLS or authenticated libp2p identities
* organization-issued certificates
* decentralized trust anchors
* signed capability records
* policy-based admission control
* audit logging
* encrypted metadata where appropriate
* rate limiting and abuse detection
* Sybil-resistant peer admission
* optional disjoint query paths for higher-assurance federated deployments

These mechanisms complement libp2p's existing security features rather than replacing them.

---

# Interoperability

The AGNTCY profile is fully interoperable with existing libp2p implementations. It introduces **policy and governance extensions above the standard Kad-DHT protocol**, allowing organizations to adopt enterprise-aware routing without modifying the underlying wire protocol. Public libp2p networks continue to function unchanged, while AGNTCY overlays can selectively federate with one another through controlled gateways and shared trust agreements.
