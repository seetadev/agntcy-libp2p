# Directory (dir) Dependencies & Libraries Breakdown

This document provides an in-depth explanation of the major open-source libraries and dependencies used in the Directory project, categorized by their architectural purpose.

## 1. Core Networking and RPC (gRPC Ecosystem)
The project heavily relies on gRPC for its high-performance, strongly-typed internal and external APIs.
*   **`google.golang.org/grpc`**: The core gRPC framework used to define and serve the API endpoints.
*   **`github.com/grpc-ecosystem/go-grpc-middleware/v2`**: Provides interceptors for gRPC servers and clients. Used for centralized logging, authentication/authorization checks, and panic recovery across all RPC calls.
*   **`github.com/grpc-ecosystem/grpc-gateway/v2`**: A reverse proxy that translates RESTful HTTP API calls into gRPC. This allows the Directory project to provide both a high-performance gRPC API and a standard HTTP JSON API simultaneously.

## 2. Decentralized and Peer-to-Peer Stack (libp2p & IPFS)
Because the Directory is a distributed peer-to-peer network, it relies heavily on the Protocol Labs / IPFS ecosystem.
*   **`github.com/libp2p/go-libp2p`**: The foundational, modular P2P networking stack. It handles secure peer-to-peer communication, connection multiplexing, and NAT traversal.
*   **`github.com/libp2p/go-libp2p-kad-dht`**: Implements the Kademlia Distributed Hash Table (DHT). This is critical for distributed content routing—allowing nodes to find peers and discover agent capabilities across the network without relying on a centralized registry.
*   **`github.com/libp2p/go-libp2p-pubsub`**: Implements decentralized publish-subscribe messaging over the P2P network, allowing nodes to broadcast and subscribe to events (e.g., capability updates).
*   **`github.com/ipfs/go-datastore` & `github.com/ipfs/go-ds-badger`**: Key-value datastore interfaces and the fast BadgerDB implementation. Used for content-addressed storage, caching DHT records, and maintaining local peer state efficiently.

## 3. Database and Persistence (ORM)
*   **`gorm.io/gorm`**: The primary Object-Relational Mapper (ORM) for Go. It abstracts raw SQL, making it easy to define database schemas using Go structs.
*   **`github.com/glebarez/sqlite` & `gorm.io/driver/postgres`**: The database drivers used by GORM. By supporting both, the project can use a lightweight, embedded SQLite database for local daemons (`dirctl daemon start`) and robust PostgreSQL for production, multi-node deployments.

## 4. Security, Identity, and Authorization
*   **`github.com/casbin/casbin/v2`**: A powerful, policy-based access control (RBAC/ABAC) library. It is used to define and enforce authorization (authz) rules, dictating which users or agents can access specific records or APIs.
*   **`github.com/lestrrat-go/jwx/v2`**: Handles JSON Web Tokens (JWT) and JSON Web Signatures (JWS). It is the backbone for authentication (authn) in the system, securely verifying the identities of connecting clients.
*   **`github.com/spiffe/go-spiffe/v2`**: The SPIFFE standard implementation for Go. Used to establish secure, zero-trust service-to-service identities via mutual TLS (mTLS) within the cluster.
*   **`github.com/sigstore/cosign/v3`**: Integrated heavily into the CLI tool to cryptographically sign, verify, and protect the provenance of container images and AI agent artifacts.

## 5. Command-Line Interface and Configuration
*   **`github.com/spf13/cobra`**: The industry-standard library for building robust CLI applications in Go. It powers the `dirctl` command-line tool, handling subcommands, arguments, and help generation.
*   **`github.com/spf13/viper`**: A complete configuration solution. It works alongside Cobra to read configuration from command-line flags, environment variables, and configuration files (e.g., `daemon.config.yaml`).

## 6. AI Agent Models and Data Validation
*   **`github.com/agntcy/oasf-sdk`**: The Open Agent Standard Format (OASF) SDK. This is the domain-specific core of the project, used to define, parse, and structure the functional characteristics and taxonomies of AI agents.
*   **`buf.build/go/protovalidate`**: A library for validating Protocol Buffer messages at runtime based on declarative rules defined in the `.proto` files. This ensures that all incoming API data is strictly validated before processing.

## 7. Artifacts and Container Registries
*   **`oras.land/oras-go/v2`**: OCI Registry As Storage (ORAS). This library allows the Directory to interact with OCI-compliant registries to distribute artifacts, such as OASF definitions or compiled agent modules, exactly like Docker images.
*   **`zotregistry.dev/zot/v2`**: A production-ready, OCI-native container image registry.

## 8. Observability and Testing
*   **`github.com/prometheus/client_golang`**: Exposes internal system metrics to Prometheus, allowing operators to monitor the health, performance, and peer connections of a Directory node.
*   **`github.com/stretchr/testify`**: The primary testing framework used across the codebase for writing clean, readable assertions and creating mock objects in unit tests.
