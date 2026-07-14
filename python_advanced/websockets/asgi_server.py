#!/usr/bin/env python3

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute


async def homepage(request):
    print("Hello")
    return HTMLResponse("<h1>WebSocket App</h1>")


async def websocket_endpoint(websocket):
    await websocket.accept()

    while True:
        message = await websocket.receive_text()
        # send back the message the client sent
        await websocket.send_text(message)


app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])
