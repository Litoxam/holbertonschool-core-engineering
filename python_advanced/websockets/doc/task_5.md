# Task 5

## Overview

In this task, the WebSocket server is integrated into a complete **ASGI application** using the **Starlette** framework.

Unlike the previous tasks, which relied only on the `websockets` library, this application supports both traditional HTTP requests and WebSocket connections. The application is served by **Uvicorn**, a production-ready ASGI server.

The server delivers a web page through HTTP while simultaneously handling real-time communication through WebSockets.

---

## How It Works

### 1. Creating the ASGI Application

A Starlette application is created by defining a list of routes.

```python
app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
    Mount("/static", app=StaticFiles(directory="static"), name="static"),
])
```

The application supports:

* an HTTP route (`/`)
* a WebSocket endpoint (`/ws`)
* static files (CSS and JavaScript)

---

### 2. Serving the Web Page

When a browser accesses:

```text
http://localhost:8000
```

Starlette executes the `homepage()` function and returns the main HTML page.

```python
async def homepage(request):
    return FileResponse("index.html")
```

The browser then automatically loads the associated CSS and JavaScript files.

---

### 3. Accepting WebSocket Connections

When JavaScript creates a WebSocket connection to:

```text
ws://localhost:8000/ws
```

Starlette executes:

```python
async def websocket_endpoint(websocket):
    await websocket.accept()
```

The connection must be accepted before any data can be exchanged.

---

### 4. Echoing Messages

The server continuously waits for incoming messages.

```python
while True:
    message = await websocket.receive_text()
```

Each received message is immediately sent back to the same client.

```python
await websocket.send_text(message)
```

This behavior is known as an **echo server**.

Example:

```text
Client → Hello
Server → Hello
```

---

## Features

* ASGI application built with Starlette
* HTTP and WebSocket support
* Serves an HTML page
* Serves static CSS and JavaScript files
* Persistent WebSocket connection
* Echoes every received message

---

## Running the Application

Start the server with Uvicorn:

```bash
uvicorn asgi_server:app --host 0.0.0.0 --port 8000 --reload
```

The application is then available at:

```text
http://localhost:8000
```

The WebSocket endpoint is available at:

```text
ws://localhost:8000/ws
```

---

## Concepts Learned

* ASGI applications
* Starlette routing
* HTTP and WebSocket integration
* Serving static files
* Persistent WebSocket connections
* Running an application with Uvicorn

---

## Next Task

Continue with **Task 6** to build a browser-based WebSocket client that communicates with the ASGI application in real time.

➡️ [Task 6](task_6.md)
