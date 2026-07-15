# Task 2

## Overview

In this task, the WebSocket server is improved by validating incoming messages before processing them.

Instead of assuming that every message is valid, the server checks whether the received text contains actual content. Messages that are empty or contain only whitespace are rejected, while valid messages receive a confirmation response.

The connection remains open regardless of whether the message is valid or invalid.

---

## How It Works

### 1. Accepting Client Connections

The server starts listening for incoming WebSocket connections.

Each connected client is handled independently by the connection handler.

---

### 2. Receiving Messages

The server continuously waits for messages from the connected client.

```python
async for message in websocket:
```

This allows the same connection to be reused for multiple messages.

---

### 3. Validating Messages

Before responding, the server removes leading and trailing whitespace using `strip()`.

```python
if len(message.strip()) > 0:
```

If the resulting string is empty, the message is considered invalid.

---

### 4. Sending the Appropriate Response

If the message is valid, the server responds with:

```text
OK:<message>
```

Example:

```text
Client: Hello
Server: OK:Hello
```

If the message is empty or contains only spaces, the server responds with:

```text
ERR:EMPTY
```

The original connection remains active so the client can continue sending messages.

---

### 5. Handling Disconnections

If the client disconnects unexpectedly, the `ConnectionClosed` exception is caught.

This prevents the server from crashing and allows it to continue accepting new client connections.

---

## Features

* Continuous WebSocket communication
* Message validation
* Detection of empty messages
* Error handling for disconnected clients
* Persistent client connection

---

## Running the Server

Start the validation server:

```bash
python3 validation_server.py
```

The server listens on:

```text
ws://localhost:8765
```

Clients can then connect and exchange multiple messages over the same WebSocket connection.

---

## Concepts Learned

* Continuous WebSocket communication
* Message validation
* String manipulation with `strip()`
* Error handling using `ConnectionClosed`
* Maintaining persistent client connections

---

## Next Task

Continue with **Task 3** to learn how to manage multiple clients and implement unicast communication.

➡️ [Task 3](task_3.md)
