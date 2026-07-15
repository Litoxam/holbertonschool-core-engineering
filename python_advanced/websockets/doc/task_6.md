# Task 6

## Overview

In this task, a browser-based client is created to communicate with the WebSocket server. Unlike the previous tasks that relied on Python scripts, this client allows users to interact with the server directly from a web browser.

The application provides real-time communication without reloading the page by using the browser's built-in WebSocket API.

---

## Project Structure

```
.
├── asgi_server.py
├── index.html
└── static
    ├── chat.js
    └── style.css
```

---

## How It Works

### 1. Serving the Web Page

When the browser accesses:

```
http://localhost:8000
```

Starlette executes the `homepage()` route and returns `index.html`.

```python
Route("/", homepage)
```

The browser then automatically loads the CSS and JavaScript files from the `static` directory.

---

### 2. Establishing the WebSocket Connection

Once `chat.js` is loaded, it creates a WebSocket connection:

```javascript
const socket = new WebSocket(`ws://${window.location.host}/ws`);
```

This opens a persistent connection to:

```
ws://localhost:8000/ws
```

(or to the current host if accessed from another device).

The server handles this connection with:

```python
WebSocketRoute("/ws", websocket_endpoint)
```

---

### 3. Sending Messages

When the user clicks the **Send** button or presses **Enter**, the message is sent through the WebSocket connection.

Example:

```javascript
socket.send(`${username}: ${input.value}`);
```

No page reload is required.

---

### 4. Receiving Messages

Whenever the server sends data back, the browser immediately receives it.

```javascript
socket.onmessage = (event) => {
    messages.innerHTML += `<p>${event.data}</p>`;
};
```

The interface is updated dynamically.

---

### 5. Keeping the Chat History

The chat history is stored locally using the browser's `localStorage`.

When the page is opened, previous messages are restored:

```javascript
messages.innerHTML = localStorage.getItem("history") || "";
```

Each received message updates the stored history automatically.

---

## Features

* Browser-based WebSocket client
* Real-time communication
* No page refresh required
* Send messages using a button or the Enter key
* Display incoming messages immediately
* Local chat history using `localStorage`
* Username added before each message

---

## Running the Application

Start the ASGI server:

```bash
uvicorn asgi_server:app --host 0.0.0.0 --port 8000 --reload
```

Open the application in a browser:

```
http://localhost:8000
```

If another device is connected to the same local network, it can access the application using the host machine's local IP address, for example:

```
http://192.168.1.xxx:8000
```

---

## Concepts Learned

* Browser WebSocket API
* Client-server communication
* Real-time messaging
* Dynamic DOM manipulation with JavaScript
* Persistent browser storage using `localStorage`
* Serving static files with Starlette
* WebSocket endpoints in an ASGI application
