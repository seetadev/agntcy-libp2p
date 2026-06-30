# Directory (dir) Project Overview

## Brief Summary
The Directory (dir) project is a decentralized platform that allows for the publication, exchange, and discovery of information about records over a distributed peer-to-peer network. It leverages the Open Agent Standard Format (OASF) to describe AI agents and provides a comprehensive set of APIs, SDKs, and tools to store, publish, and discover records across the network based on specific attributes and constraints. Additionally, it integrates with CSIT for continuous system integration and testing across various versions and environments.

## Problems Solved
- **Capability-Based Discovery:** Enables the discovery of agents by matching their structured functional capabilities (via OASF taxonomies) against specific requirements, rather than simple keyword searches.
- **Verifiable Claims:** Provides cryptographic mechanisms for data integrity and provenance tracking, allowing users to trust the subjective capabilities claimed by various AI agents.
- **Semantic Linkage:** Securely links components to form evolutionary version histories, collaborative partnerships between agents with complementary skills, and dependency chains for composite agent workflows.
- **Distributed Content Discovery:** Utilizes content-addressing and distributed hash tables (DHT) for globally unique, scalable content synchronization across decentralized networks.
- **Security & Authenticity:** Incorporates cryptographic signing, secure communication protocols, and strict access controls to maintain the integrity of Directory records.

## Use Cases
- **Agent Discovery & Routing:** Finding the right AI agent for a specific task based on its advertised capabilities and constraints.
- **Composite Agent Workflows:** Building complex chains of agents that depend on each other, tracking their relationships securely.
- **Verifiable Agent Marketplaces:** Establishing a decentralized marketplace where agents' claims are verifiable and tamper-proof.
- **Evolutionary Agent Development:** Tracking version histories and evolutionary improvements of agents over time through semantic linkages.

## Supported Platforms and Usage
The Directory project can be deployed and utilized across several platforms:

1. **Local Daemon (Mac/Linux):**
   The built-in daemon is the fastest way to run a local instance, bundling the gRPC apiserver and reconciler with an embedded SQLite and local OCI store.
   - **Usage:** Run `dirctl daemon start` (State is stored in `~/.agntcy/dir/`).

2. **Docker / Docker Compose:**
   You can deploy the services (apiserver, reconciler, Zot registry, PostgreSQL) as isolated containers.
   - **Usage:** Navigate to `install/docker` and run `docker compose up -d` (or use `task server:start`).

3. **Kubernetes (Helm Charts):**
   The project provides Helm charts to deploy services into existing Kubernetes clusters.
   - **Usage:** 
     ```bash
     helm pull oci://ghcr.io/agntcy/dir/helm-charts/dir --version v1.5.0
     helm upgrade --install dir oci://ghcr.io/agntcy/dir/helm-charts/dir --version v1.5.0
     ```

4. **SDKs (Client Integration):**
   - **Golang:** Available via `github.com/agntcy/dir/client`
   - **Python:** Available via PyPi (`agntcy-dir`)
   - **JavaScript:** Available via NPM (`agntcy-dir`)

## Key Dependencies and Libraries
The project is primarily written in **Go (v1.26)** and depends on several critical libraries for its core functionalities:
- **gRPC Ecosystem (`grpc-ecosystem` / `grpc-gateway`):** For defining and serving the API and data models.
- **libp2p (`github.com/libp2p/go-libp2p`):** The foundational peer-to-peer networking stack for distributed communication.
- **OASF SDK (`github.com/agntcy/oasf-sdk`):** For describing and validating AI agent capabilities.
- **IPFS Datastore (`github.com/ipfs/go-datastore`):** For decentralized data storage and content addressing.
- **Casbin (`github.com/casbin/casbin/v2`):** For robust, policy-based access control (authz).
- **SQLite (`github.com/glebarez/sqlite`) & PostgreSQL:** For database storage of system state and records.
- **JWX (`github.com/lestrrat-go/jwx/v2`):** For parsing and validating JSON Web Tokens (JWT) used in authentication.
- **Protobuf / Protovalidate:** For schema definitions and validation rules.
