# Deep Dive: Architecture and Core Technologies

This document provides an in-depth look at **when**, **where**, and **how** the four core pillars of the Directory project are utilized: `go-libp2p`, `Kademlia DHT`, `IPFS (go-datastore)`, and `gRPC`. It also covers the special use cases and edge cases for each.

---

## 1. go-libp2p (The Networking Layer)

### When and Where is it used?
*   **Location:** Found primarily in `server/routing/internal/p2p/host.go` and throughout the `server/routing/` package.
*   **Purpose:** It acts as the foundational transport layer. Instead of nodes connecting to a central server, `go-libp2p` is used to establish secure, encrypted, and multiplexed connections directly between Directory nodes. It handles peer identities (Peer IDs derived from cryptographic keys).

### Special / Edge Cases:
*   **NAT Traversal & Relays:** One of the most powerful edge cases solved by libp2p is connecting agents that are sitting behind strict corporate firewalls or home NATs. Through libp2p's `autorelay` and STUN/TURN integration, nodes that cannot expose a public IP can still participate in the Directory network, publish capabilities, and be discovered.
*   **Connection Multiplexing:** `go-libp2p` allows multiple discrete streams (like pubsub, DHT queries, and custom RPC calls) to share a single TCP/QUIC connection, greatly reducing overhead and port exhaustion.

---

## 2. Kademlia DHT (`go-libp2p-kad-dht`)

### When and Where is it used?
*   **Location:** Initialized in `server/routing/internal/p2p/dht.go` and utilized heavily in `server/routing/routing_remote.go`.
*   **Purpose:** The Kademlia Distributed Hash Table is the brain behind the "search" functionality. It is used to distribute and discover "Provider Records." 

### Special / Edge Cases:
*   **Capability-to-Peer Mapping:** When an AI agent announces "I can summarize text" (using the OASF format), this capability is hashed. The DHT stores a mapping of that `Hash(Capability) -> Peer ID`. If Node A wants to find an agent for summarizing text, it queries the DHT for that hash. The DHT routes the query through the network, hopping to nodes whose IDs are mathematically closer to the hash, until it finds the record.
*   **Network Partitioning:** In edge cases where a subset of nodes gets disconnected from the wider internet (e.g., an air-gapped corporate network), Kademlia DHT naturally degrades gracefully. The partitioned nodes will form their own localized DHT and continue to discover each other, merging back automatically when the connection is restored.

---

## 3. IPFS Datastore (`go-datastore` & `go-ds-badger`)

### When and Where is it used?
*   **Location:** Bootstrapped in `server/datastore/datastore.go` and utilized by the routing subsystem (e.g., `server/routing/routing_local.go`).
*   **Purpose:** While the project doesn't run a full IPFS node, it heavily utilizes IPFS's storage primitives. The `go-datastore` provides an abstract interface for content-addressed key-value storage. By default, it runs in memory (`MapDatastore`), but when provided a local directory, it spins up `go-ds-badger`.

### Special / Edge Cases:
*   **Lightweight Persistence (Daemon Mode):** When a user runs `dirctl daemon start`, the node uses the BadgerDB implementation (`go-ds-badger`). Badger is a highly performant, embedded key-value store. This edge case allows a node to retain its DHT routing tables, cached peer records, and capabilities across reboots without the heavy operational burden of running a PostgreSQL cluster.

---

## 4. gRPC and `go-libp2p-gorpc`

### When and Where is it used?
*   **Location:** Standard gRPC is used in the external API layer (`server/server.go`, `api/`). The specialized libp2p integration is found in `server/routing/rpc/rpc.go`.
*   **Purpose:** gRPC serves as the strict, schema-driven API definition (via Protobuf) for the entire project. It defines exactly how a client talks to the Directory.

### Special / Edge Cases:
*   **gRPC over Libp2p Streams (The Edge Case):** The most fascinating edge case in this architecture is the use of `go-libp2p-gorpc`. Normally, a gRPC server opens a TCP port (like 50051) and listens for HTTP/2 traffic. However, for node-to-node communication, this project passes gRPC traffic *directly over the existing libp2p P2P streams*. 
    *   **Why?** This means Directory nodes do not need to open extra firewall ports for internal gRPC traffic. The gRPC requests bypass standard TCP dialing and flow through the encrypted, NAT-traversed P2P tunnels already established by libp2p. This allows seamless, highly secure RPC calls between nodes that might otherwise be completely hidden from the public internet.
