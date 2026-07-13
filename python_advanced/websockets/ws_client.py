#!/usr/bin/env python3

import asyncio
import websockets
import os


# Connect to the server, send one message and return the response.
async def connect_and_send(uri: str, text: str) -> str:
    async with websockets.connect(uri) as ws:
        await ws.send(text)
        response = await ws.recv()
        return response


async def main():
    # Connect to the local WebSocket server.
    uri = os.getenv("WS_URI", "ws://localhost:8765/")
    response = await connect_and_send(uri, "demo")

    # Print only the server response.
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
