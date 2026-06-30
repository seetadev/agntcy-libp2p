# The Python SDK (`agntcy-dir`)

While the heavy Directory Node runs in Go, AI developers interact with it using their preferred language. The `agntcy-dir` Python SDK is the official bridge for Python-based AI applications to connect to the decentralized network.

You can install it directly from PyPi:
```bash
pip install agntcy-dir
```

## What does the SDK actually do?
Under the hood, the Python SDK is essentially a strongly-typed **gRPC Client**. Because the Directory Node exposes its APIs using Protocol Buffers (protobuf) and gRPC, the Python SDK is auto-generated to perfectly map to the Node's endpoints. 

It handles:
1. **Connection Management:** Opening and maintaining secure HTTP/2 gRPC channels to your local Directory Node (`dirctl daemon`).
2. **Serialization:** Converting your Python objects and dictionaries into Protocol Buffer binaries.
3. **Authentication:** Attaching JWT tokens or API keys (handled by JWX in the server) securely to your request headers.
4. **OASF Integration:** It deeply integrates with the Open Agent Standard Format to ensure you are formatting your AI's capabilities according to the network standard.

## Core API Capabilities Exposed to Python
If you explore the `proto` files in the core Directory project, you'll see the exact services the Python SDK wraps:

### 1. The `Routing` API
This is how your Python code hooks into the DHT.
*   **Use Case:** You can call methods to resolve a capability to a specific peer on the decentralized network or advertise your own peer ID to the Kademlia DHT.

### 2. The `Search` API
This acts as your "Yellow Pages" lookup.
*   **Use Case:** Your Python script can query the node using specific metadata, constraints, or capability requirements to find a matching agent. The node handles the complex distributed search and simply returns the results to Python.

### 3. The `Store` API
This is for registering records.
*   **Use Case:** When you want to publish your AI agent's profile, you pass the OASF metadata object to the `Store` service, and the node commits it to the datastore (IPFS BadgerDB) and gossips it to the network.

## Example Workflow in Python
Using the SDK hides all the P2P networking complexity from your AI logic:

```python
from agntcy_dir.client import DirectoryClient
from agntcy.oasf.v1 import AgentProfile, Capability

# 1. Connect to the local Daemon
client = DirectoryClient("localhost:8888")

# 2. Define your AI Agent using standard OASF types
my_agent = AgentProfile(
    name="Python Summarization Bot",
    capabilities=[Capability.TEXT_SUMMARY],
    endpoint="http://api.mybot.internal/v1/summarize"
)

# 3. Publish to the network via the Store API
client.store.publish_record(my_agent)

# 4. Or search the network for another agent via the Search API
lawyer_agent = client.search.find_agent_by_capability(Capability.LEGAL_ANALYSIS)
print(f"Found a legal agent at: {lawyer_agent.endpoint}")
```
*(Note: Code is pseudo-code for architectural illustration based on the grpc proto structure)*

## Summary
The `agntcy-dir` Python package turns complex decentralized networking, gRPC connection handling, and cryptographic protobuf serialization into simple, standard Python function calls.
