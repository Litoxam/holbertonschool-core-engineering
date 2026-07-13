# Task 00 - WebSocket Echo Server

## Objective

The goal of this task is to build a simple **WebSocket Echo Server** using Python and the `websockets` library.

Unlike a traditional HTTP server, a WebSocket server keeps the connection open, allowing the client and the server to exchange messages in real time. In this task, the server simply sends back every message it receives without modifying it.

---

# New Concepts

## What is a WebSocket?

A **WebSocket** is a communication protocol that provides a persistent, bidirectional connection between a client and a server.

Unlike HTTP, which creates a new connection for every request, a WebSocket connection stays open until either the client or the server closes it.

This makes WebSockets ideal for:

* Chat applications
* Multiplayer games
* Live notifications
* Dashboards
* Collaborative applications

---

## The `websockets` Library

Python's `websockets` library provides everything needed to build WebSocket applications.

To start a server, use:

```python
async with serve(connection_handler, "localhost", 8765):
```

* `connection_handler` is called whenever a client connects.
* `"localhost"` is the server address.
* `8765` is the listening port.

---

## Asynchronous Programming

The server relies on **asyncio**, Python's asynchronous framework.

### `async`

Defines a coroutine that can pause while waiting for an operation to finish.

```python
async def connection_handler(websocket):
```

---

### `await`

Waits for an asynchronous operation without blocking the entire application.

```python
await websocket.send(message)
```

---

## Handling Client Connections

Every time a client connects, the server executes:

```python
async def connection_handler(websocket):
```

The `websocket` object represents the connection between the server and a single client.

---

## Receiving Messages

Incoming messages are processed using:

```python
async for message in websocket:
```

This loop keeps listening for new messages until the client disconnects.

---

## Sending Messages

Messages are sent back using:

```python
await websocket.send(message)
```

Since the outgoing message is identical to the incoming one, this server is called an **Echo Server**.

---

## Keeping the Server Running

Once the server has started, it must continue accepting connections.

```python
await server.serve_forever()
```

This method keeps the server alive indefinitely.

---

# Program Flow

```text
Start the program
        │
        ▼
Create the WebSocket server
        │
        ▼
Wait for a client connection
        │
        ▼
Receive a message
        │
        ▼
Send the exact same message back
        │
        ▼
Wait for the next message
        │
        ▼
Repeat until the client disconnects
```

---

# Key Takeaways

* A WebSocket keeps a connection open for continuous communication.
* `serve()` creates a WebSocket server.
* `connection_handler()` manages communication with one connected client.
* `async for` listens for incoming messages continuously.
* `websocket.send()` sends data back through the same connection.
* `serve_forever()` keeps the server running until it is stopped.

---

## Next Task

➡️ **[Task 01](task_01.md)**
