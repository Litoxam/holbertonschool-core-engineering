# Task 1

## Overview

In this task, a simple WebSocket client is implemented using Python and the `websockets` library.

The client establishes a connection with a WebSocket server, sends a single message, waits for the server response, prints it exactly as received, and then closes the connection cleanly.

This task introduces the basics of asynchronous client-server communication using WebSockets.

---

## How It Works

### 1. Connecting to the Server

The client opens a WebSocket connection to the server.

```python
async with websockets.connect(uri) as ws:
```

The server is expected to be running at:

```text
ws://localhost:8765
```

---

### 2. Sending a Message

Once connected, the client sends a single message.

```python
await ws.send(text)
```

The message is transmitted through the already established WebSocket connection.

---

### 3. Receiving the Response

The client waits for one response from the server.

```python
response = await ws.recv()
```

The received message is returned by the function.

---

### 4. Closing the Connection

The connection is automatically closed when leaving the `async with` block.

This ensures that resources are released correctly without requiring any additional cleanup.

---

## Main Function

The `main()` coroutine connects to the local WebSocket server, sends the message `"demo"`, receives the response, and prints it without adding a newline.

```python
response = await connect_and_send(uri, "demo")
print(response, end="")
```

The server response is the only output produced by the program.

---

## Features

* Asynchronous WebSocket client
* Connects to a WebSocket server
* Sends one message
* Receives one response
* Closes the connection automatically
* Prints only the server response

---

## Running the Client

Make sure a WebSocket server is already running on:

```text
ws://localhost:8765
```

Then execute:

```bash
python3 ws_client.py
```

---

## Concepts Learned

* Asynchronous programming with `async` and `await`
* WebSocket client connections
* Sending and receiving messages
* Using the `websockets` library
* Automatic resource management with `async with`

---

## Next Task

Continue with **Task 2** to learn how to validate incoming WebSocket messages and handle invalid user input.

➡️ [Task 2](task_2.md)