# Task 3

## Overview

In this task, the WebSocket server is extended to support multiple simultaneous client connections.

Instead of handling only one client at a time, the server keeps track of every connected client. However, each received message is sent back only to the client that originally sent it. This communication model is called **unicast**.

Each response is prefixed with `U:` to indicate that it is a unicast message.

---

## How It Works

### 1. Tracking Connected Clients

A global set stores every active WebSocket connection.

```python
clients = set()
```

When a client connects, its WebSocket object is added to the set.

When the client disconnects, it is removed.

---

### 2. Receiving Messages

Each connected client is handled independently.

```python
async for message in websocket:
```

The server continuously waits for messages from that specific client.

---

### 3. Sending a Unicast Response

When a message is received, the server replies only to the sender.

```python
await websocket.send(f"U:{message}")
```

Other connected clients do not receive anything.

Example:

```text
Client A → Hello
Server → U:Hello
```

If Client B is connected at the same time, it receives no message.

---

### 4. Handling Client Disconnections

If a client disconnects, the connection is removed from the set of active clients.

This prevents the server from keeping invalid connections in memory.

---

## Features

* Supports multiple simultaneous clients
* Tracks active WebSocket connections
* Sends responses only to the sender
* Prefixes every response with `U:`
* Cleans up disconnected clients

---

## Running the Server

Start the unicast server:

```bash
python3 unicast_server.py
```

The server listens on:

```text
ws://localhost:8765
```

Multiple clients can connect simultaneously while communicating independently.

---

## Concepts Learned

* Managing multiple WebSocket clients
* Storing active connections
* Unicast communication
* Connection lifecycle management
* Cleaning up disconnected clients

---

## Next Task

Continue with **Task 4** to learn how to broadcast messages to every connected client.

➡️ [Task 4](task_4.md)
