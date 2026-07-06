# AWS Observability Stack for AGNTCY × libp2p

A lightweight application-level observability stack for monitoring distributed AGNTCY and libp2p deployments across AWS or on-premise infrastructure. The system collects real-time host metrics using **psutil**, exposes them through **Tornado**, and stores historical telemetry in **MongoDB** for visualization and analysis.

## Features

- 📊 Real-time monitoring of local and remote nodes
- 🖥️ CPU, memory, disk, and network interface metrics
- 🌐 Monitor multiple AWS instances or on-premise servers
- 📈 Historical performance analytics
- 🚀 Lightweight deployment with minimal dependencies

## Tech Stack

- **psutil** – System resource monitoring
- **Tornado** – High-performance web and TCP server
- **MongoDB** – Metrics storage and historical analytics

---

# Getting Started

## 1. Start the Root Server

Launch the central monitoring server on the machine that will aggregate metrics.

```bash
bash run-root.sh
```

This starts:

- TCP Listener (receives metrics from remote agents)
- HTTP Dashboard Server

---

## 2. Start Remote Monitoring Agents

Run the monitoring agent on each machine you want to observe (including the root server if desired).

```bash
bash run-remote.sh
```

Example configuration:

```text
Observer remote running at port 8888

Destination IP:
54.179.143.69

Destination Port:
8889

Remote Name:
foobar-production

Preferred Network Interface:
eth0
```

The agent continuously collects system metrics and streams them to the root server.

---

# Dashboard

After deployment, the following dashboards are available:

| Endpoint | Description |
|----------|-------------|
| `/live` | Live system metrics and health monitoring |
| `/stats` | Historical statistics and resource utilization |
| `/perf` | Performance benchmarks and diagnostic tests |

Example:

```
http://<ROOT_IP>:9000/live
http://<ROOT_IP>:9000/stats
http://<ROOT_IP>:9000/perf
```

---

## Architecture

```
Remote Server A ─┐
                 │
Remote Server B ─┼──► Root Observer (Tornado)
                 │           │
Remote Server C ─┘           ▼
                        MongoDB Storage
                               │
                               ▼
                      Web Dashboard (:9000)
```

This architecture provides a simple, scalable observability layer for monitoring AGNTCY agents, libp2p services, and distributed infrastructure across cloud and edge environments.
