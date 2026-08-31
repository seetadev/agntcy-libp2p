### Internet-Draft: Naming and Routing Substrate for Agentic AI
**Network Working Group**  
**Internet-Draft**  
**Intended Status:** Standards Track  
**Expires:** March 5, 2027  
**Date:** September 1, 2026  

---

### Naming and Routing Substrate for Agentic AI: The agent:// URI Scheme and Gossip-Enhanced Coordination Layer (GEACL)
**draft-ietf-dart-agent-routing-00**

### Abstract
This document defines a topology-independent naming and routing substrate for decentralized multi-agent systems (MAS) [5, 9, 66]. It introduces the standard format for the `agent://` Uniform Resource Identifier (URI) scheme, which cryptographically decouples an agent's logical identity from its volatile physical network address [78, 87]. To scale discovery without relying on centralized coordination, this draft specifies a deterministic key derivation method for mapping capabilities directly into standard Kademlia-based Distributed Hash Tables (DHTs) [55, 77, 85]. Finally, this document outlines the architecture of the Gossip-Enhanced Agentic Coordination Layer (GEACL), defining how stochastic push-pull gossip, anti-entropy state reconciliation, and verifiable cryptographic delegation tokens enable resilient, zero-trust coordination across independent administrative domains [74, 80, 83].

---

### 1. Introduction
Traditional Internet routing and service discovery are tightly coupled to physical or logical endpoints (IP addresses, hostnames, and domain names) [19, 71]. While sufficient for static client-server models, this location-bound identity model fails when applied to large-scale, autonomous, and highly dynamic multi-agent systems (MAS) [19, 71]. In these emerging cognitive networks, agents undergo rapid horizontal scaling, frequent containerized redeployments, physical migrations across cloud providers, and temporary offline states [19, 71].

Furthermore, as artificial intelligence matures from a localized application feature into an active, multi-hop participant in distributed industry workflows—such as site selection, pre-feasibility analysis, and underwriting in the Milken Institute's Infrastructure-Specific Cognition framework—the network must support dynamic, cross-boundary machine-to-machine collaboration [17, 18, 69, 70]. 

This document proposes a standardized framework that decoupling naming from routing for agentic systems, addressing three core interoperability challenges [21, 73]:
1. **Network Interoperability:** Enabling agents to communicate across heterogeneous network environments (including NATs, firewalls, and private subnets) without requiring centralized proxies [21, 24, 73, 76].
2. **Semantic Interoperability:** Establishing machine-readable capability expressions and identity schemas that survive delegation across multiple system boundaries [21, 27, 73, 79].
3. **Operational Interoperability:** Providing an open, federated telemetry and trace-context propagation protocol to observe and troubleshoot multi-hop agent execution paths without requiring a single centralized monitoring provider [21, 32, 73, 84].

---

### 2. Terminology and Conventions
The key words "MUST", "MUST NOT", "REQUIRED", "SHALL", "SHALL NOT", "SHOULD", "SHOULD NOT", "RECOMMENDED", "NOT RECOMMENDED", "MAY", and "OPTIONAL" in this document are to be interpreted as described in BCP 14 [RFC2119] [RFC8174] when, and only when, they appear in all capitals, as shown here.

* **Agent:** An autonomous software entity capable of executing tasks, calling tools, reasoning, and coordinating workflows [14, 66].
* **Gossip-Enhanced Agentic Coordination Layer (GEACL):** The background synchronization layer that runs stochastic epidemic protocols over P2P transport overlays to distribute ambient discovery and health signals [23, 75, 80].
* **Capability Path:** A hierarchical, slash-separated semantic string describing a specific function, tool, or domain authority that an agent is certified to perform [78, 87].
* **Trust Root:** The DNS authority or organizational endpoint responsible for issuing and cryptographically verifying agent credentials [5, 9].
* **TypeID:** A K-sortable, globally unique, typed identifier used to uniquely distinguish individual agent instances without requiring a central authority [5, 9].

---

### 3. Reference Architecture Model
The Naming and Routing Substrate for Agentic AI operates as a modular, transport-agnostic coordination layer. The reference architecture separates high-level cognitive workflows from lower-level network routing [34, 86].

```text
+-----------------------------------------------------------------------+
|                       Cognitive / Application Layer                   |
|  - Reasoning Loops, Local Tools, LLM Planning, Decision Logic        |
+-----------------------------------------------------------------------+
                                   │
                                   ▼ (Task Requests / Tool Invocations)
+-----------------------------------------------------------------------+
|                    Structured Interoperability Layer                  |
|  - Model Context Protocol (MCP), Agent-to-Agent (A2A) Protocols       |
+-----------------------------------------------------------------------+
                                   │
                                   ▼ (Discovery, Identity & Routing)
+-----------------------------------------------------------------------+
|             Gossip-Enhanced Agentic Coordination Layer (GEACL)        |
|  - agent:// URI Naming               - Kademlia DHT Key Derivation    |
|  - Epidemic State Synchronization    - Cryptographic Attestation      |
+-----------------------------------------------------------------------+
                                   │
                                   ▼ (Multiaddress Stream Transport)
+-----------------------------------------------------------------------+
|                      Decentralized Transport Substrate                |
|  - Modular P2P Layer (libp2p), NAT Traversal, Relay, Encrypted Links  |
+-----------------------------------------------------------------------+
                                   │
                                   ▼ (Network Transport protocols)
+-----------------------------------------------------------------------+
|                          Standard Internet Layers                     |
|  - QUIC, TCP, WebRTC, UDP, IP Core, Wireless Local Meshes             |
+-----------------------------------------------------------------------+
```

---

### 4. The agent:// URI Scheme

### 4.1. Syntax and ABNF Grammar
The `agent://` URI scheme defines a standard, topology-independent identifier for agents. The formal syntax is defined using Augmented Backus-Naur Form (ABNF) as specified in [RFC5234]:

```abnf
agent-uri       = "agent://" trust-root "/" capability-path "/" agent-id [ "?" query ] [ "#" fragment ]
trust-root      = host [ ":" port ]
capability-path = path-segment *31( "/" path-segment )
path-segment    = 1*64( LOWER / DIGIT / "-" )
agent-id        = agent-prefix "_" type-suffix
agent-prefix    = type-class *( "_" type-modifier )
type-class      = "llm" / "rule" / "human" / "composite" / "sensor" / "actuator" / "hybrid" / extension-class
extension-class = "x-" 1*15( LOWER )
type-modifier   = 1*15( LOWER )
type-suffix     = first-char 25base32char
first-char      = "0" / "1" / "2" / "3" / "4" / "5" / "6" / "7"
base32char      = LOWER / %x32-37 ; base32 alphabet (a-z, 2-7) excluding 'o', 'l', 'i'
LOWER           = %x61-7A         ; a-z
DIGIT           = %x30-39         ; 0-9
```

### 4.2. Scheme Components
* **Trust Root:** Specifies the canonical organizational administrative domain (e.g., `milkeninstitute.org` or `lenders.agntcy.net`) [5, 9]. The domain MUST host a standard public key directory at the HTTPS well-known endpoint: `https://<trust-root>/.well-known/agent-keys.json`.
* **Capability Path:** A hierarchical, slash-separated categorization of what the agent does (e.g., `site-selection/deepmind-v0` or `underwriting/bond-pricing`) [5, 9]. This enables prefix-based sub-tree matching during discovery [78, 87].
* **Agent ID:** A K-sortable TypeID. The prefix indicates the architectural class (e.g., `llm` or `composite`), and the suffix contains a 130-bit, Base32-encoded value [5, 9]. The suffix MUST be derived from a cryptographically secure UUIDv7 to ensure collision-free local generation and chronological sorting [5, 9].

---

### 5. DHT-Based Service Discovery and Key Derivation

### 5.1. Decentralized DHT-Kademlia Overlays
To discover an agent's current network address (such as a libp2p multiaddress) without relying on a central database, nodes MUST support a decentralized lookup protocol over a Kademlia-based Distributed Hash Table (DHT) [52, 55, 77, 85].

### 5.2. Hash Key Derivation Formula
The lookup key on the DHT MUST be generated deterministically from the canonicalized components of the `agent://` URI. This ensures that lookup keys are tied directly to administrative authorities and specific capabilities, preventing arbitrary namespace pollution [78, 87, 89]:

$$\text{DHT\_Key} = \text{SHA256}\left(\text{normalize}(\text{trust\_root}) \parallel \text{"/"} \parallel \text{normalize}(\text{capability\_path})\right)$$

### 5.3. Prefix-Matching Routing Mechanics
To search for any sub-specialized agent, a querying client calculates the DHT keys at various depths of the capability path tree:
* A client seeking *any* underwriting agent queries: `SHA256("milkeninstitute.org/underwriting")`.
* A client seeking a *specific* bond-pricing underwriting agent queries: `SHA256("milkeninstitute.org/underwriting/bond-pricing")`.

The Kademlia nodes routing these keys return the matching multiaddresses, ensuring that lookups are localized, scoped by trust root, and completed in $O(\log N)$ network hops [55, 78, 87, 89].

---

### 6. Cryptographic Capability Attestations

### 6.1. PASETO Token Profile
Every agent registering its capability and multiaddress location inside the DHT MUST sign its registration using a Platform-Agnostic SEcurity Token (PASETO v4.public) [5, 9]. This prevents DHT poisoning and identity hijacking [56, 89, 90].

The token payload MUST contain the following claims:
```json
{
  "iss": "https://milkeninstitute.org",
  "sub": "agent://milkeninstitute.org/underwriting/bond-pricing/llm_01hq7z1xb5v78a239cd45e6fg",
  "aud": "urn:agntcy:dht:register",
  "exp": "2026-09-01T15:19:40Z",
  "nbf": "2026-08-31T13:19:40Z",
  "cap": [
    "underwriting/bond-pricing",
    "underwriting/risk-modeling"
  ],
  "loc": [
    "/ip4/192.0.2.1/tcp/4001/p2p/QmYyQ2E...",
    "/dns4/agents.milkeninstitute.org/tcp/443/wss"
  ]
}
```

### 6.2. Validation Rules
A DHT storing node or a querying client MUST validate the PASETO attestation before accepting a routing record [56, 89, 90]:
1. **Fetch Trust Key:** Perform a secure HTTPS request to fetch the public key array from `https://<iss>/.well-known/agent-keys.json`.
2. **Signature Verification:** Cryptographically verify the Ed25519 signature of the PASETO v4.public token using the verified public key.
3. **Temporal Bounds Check:** Validate that the current system time is between `nbf` (Not Before) and `exp` (Expiration).
4. **Authority Alignment:** Ensure that the `sub` URI authority matches the `iss` domain authority.
5. **Path Validation:** Verify that every path string in the `cap` array is equal to or a hierarchical descendant of the capability-path declared in the `sub` URI.

---

## 7. The Gossip-Enhanced Agentic Coordination Layer (GEACL)

### 7.1. Ambient Synchronization Engine
The GEACL does not replace high-precision, direct transactional connection protocols (like MCP or A2A via SLIM) [23, 74]. Instead, it establishes an offline, stochastic background sync layer to maintain ambient situational awareness across P2P overlays (using protocols like GossipSub) [56, 75, 80].

### 7.2. State Reconciliation and CRDT Merge Rules
To reconcile capability health states and network status across independent administrative boundaries without requiring central consensus, GEACL nodes use Conflict-Free Replicated Data Types (LWW-Element-Set CRDTs) [29, 32, 80, 85].
* Every state update contains a monotonically increasing Vector Clock or nanosecond timestamp [29, 80].
* If conflicting state records are gossiped, the node resolves the state by choosing the record with the highest logical timestamp [29, 80].
* Deleted registration states propagate using cryptographically signed tombstone markers to ensure garbage collection across the network [80, 85].

### 7.3. Priority Relevance Filtering
To avoid network flooding in massive deployments, nodes MUST implement priority relevance filtering [80, 88]:
- **High-Priority Events:** Real-time health revocations, task cancellations, and critical error indicators bypass normal aggregation windows and are disseminated immediately [80, 88].
- **Low-Priority Events:** Routine capability telemetry, historical trace records, and background performance updates are aggregated and throttled using token-bucket rate limits before being gossiped [80, 88].

---

### 8. N-Hop Context Delegation and Provenance

### 8.1. Causal Context Propagation
In multi-agent systems, workflows involve long chains of delegation (e.g., Human -> Agent A -> Agent B -> Tool C) [27, 79]. Standardizing how context propagates ensures that downstream execution systems can determine the precise origin of any request [29, 80, 81].

### 8.2. Cryptographic Delegation Chains
Every n-hop request MUST carry a cryptographic delegation chain block containing nested, signed authorization tokens:

```text
+------------------------------------------------------------------------+
|                      DELEGATION CONTEXT BLOCK                          |
|                                                                        |
|  [Root Authorization]                                                  |
|   - Issuer: human://milkeninstitute.org/analyst_01j6                   |
|   - Subject: agent://milkeninstitute.org/site-selection/llm_01h        |
|   - Action: ALLOW "execute-feasibility"                                |
|   - Signature: Ed25519 (Signed by human_key_01)                        |
|                                                                        |
|  [First-Hop Delegation]                                                |
|   - Issuer: agent://milkeninstitute.org/site-selection/llm_01h         |
|   - Subject: agent://lenders.agntcy.net/underwriting/composite_02k     |
|   - Action: DELEGATE "evaluate-debt-risk"                              |
|   - Parent Signature Hash: SHA256(Root Authorization)                  |
|   - Signature: Ed25519 (Signed by agent_llm_01h_key)                   |
+------------------------------------------------------------------------+
```

Each downstream hop MUST verify the validity of all parent signatures up to the trust root, ensuring continuous accountability across organizational and protocol boundaries [79, 88].

---

### 9. Security Considerations

### 9.1. DHT Poisoning and Spoofing
Attackers could try to publish fraudulent routing records to hijack traffic aimed at critical business agents. The verification rules in Section 6.2 (requiring PASETO validation against DNS-anchored HTTPS `.well-known` endpoints) MUST be strictly enforced by all routing peers [56, 89, 90].

### 9.2. Context and Metadata Leakage
Stochastic gossip protocols naturally broadcast metadata across a wide network of peers [80, 88]. If left unencrypted, this leaks proprietary corporate logic, transaction volume, and operational dependencies. 
* GEACL messages belonging to private consortiums MUST use transport-layer encryption (such as Noise or TLS 1.3 over multiplexed libp2p streams) [51, 53, 56, 88].
* Group-based gossip channels MUST implement cryptographic link-layer payload encryption using pre-shared consortium keys or localized multi-party session keys.

---

### 10. IANA Considerations

### 10.1. URI Scheme Registration
This section registers the `agent://` URI scheme in accordance with [RFC7595].
* **Scheme Name:** agent
* **Status:** Permanent
* **Applications/Protocols:** Decentralized Multi-Agent Systems, AGNTCY, libp2p routing substrates.
* **Contact:** IETF DART Working Group.

### 10.2. Capability Namespace Registry
IANA is requested to establish a registry for canonical high-level agent capability prefix namespaces, with initial values:
* `site-selection`
* `underwriting`
* `permitting`
* `risk-modeling`
* `data-retrieval`
* `computation`

---

## 11. Informative References
* [RFC2119] Bradner, S., "Key words for use in RFCs to Indicate Requirement Levels", BCP 14, RFC 2119, March 1997.
* [RFC8174] Leiba, B., "Ambiguity of Uppercase vs Lowercase in RFC 2119 Key Words", BCP 14, RFC 8174, May 2017.
* [RFC5234] Crocker, D., Ed. and P. Overell, "Augmented ABNF for Syntax Specifications: ABNF", STD 68, RFC 5234, January 2008.
* [RFC7595] Thaler, D., Ed., "Guidelines and Registration Procedures for New URI Schemes", BCP 35, RFC 7595, June 2015.
* [RFC7991] Hoffman, P., "The "xml2rfc" Version 3 Vocabulary", RFC 7991, December 2016.
