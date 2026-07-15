# Task 4

## Overview

In this task, the WebSocket server is modified to implement **broadcast communication**.

Unlike the previous task, where messages were sent only to the sender, every message received by the server is now forwarded to all connected clients.

Each broadcasted message is prefixed with `B:` to indicate that it was sent to every active client.

---

## How It Works

### 1. Tracking Connected Clients

A global set stores every active WebSocket connection.

```python
clients = set()
```

Each client is added to the set when it connects and removed when it disconnects.

---

### 2. Receiving Messages

Each client connection is handled independently.

```python
async for message in websocket:
```

The server continuously waits for incoming messages.

---

### 3. Broadcasting Messages

When a message is received, the server iterates through every connected client and sends the message to each one.

```python
for client in clients:
    await client.send(f"B:{message}")
```

Example:

```text
Client A → Hello

Client A receives → B:Hello
Client B receives → B:Hello
Client C receives → B:Hello
```

Every connected client receives the same message, including the sender.

---

### 4. Handling Client Disconnections

When a client disconnects, its WebSocket connection is removed from the set.

This prevents the server from attempting to send messages to inactive connections.

---

## Features

* Supports multiple simultaneous clients
* Tracks active WebSocket connections
* Broadcasts messages to every connected client
* Prefixes every message with `B:`
* Removes disconnected clients automatically

---

## Running the Server

Start the broadcast server:

```bash
python3 broadcast_server.py
```

The server listens on:

```text
ws://localhost:8765
```

Any message sent by one client is immediately broadcast to every connected client.

---

## Concepts Learned

* Broadcast communication
* Managing multiple WebSocket clients
* Iterating through active connections
* Sending the same message to multiple clients
* Connection lifecycle management

---

## Next Task

Continue with **Task 5** to learn how to build an ASGI application using Starlette and WebSockets.

➡️ [Task 5](task_5.md)
