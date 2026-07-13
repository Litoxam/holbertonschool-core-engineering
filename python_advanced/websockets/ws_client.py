#!/usr/bin/env python3

import asyncio
from websockets.asyncio.client import connect


# Connect to the server, send one message and return the response.
async def connect_and_send(uri: str, text: str) -> str:
    async with connect(uri) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return response


async def main():
    # Connect to the local WebSocket server.
    response = await connect_and_send("ws://localhost:8765/", "demo")

    # Print only the server response.
    print(response, end="")
