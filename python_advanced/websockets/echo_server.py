#!/usr/bin/env python3

import asyncio
from websockets.asyncio.server import serve


# Handle each client connection.
async def connection_handler(websocket):
    async for message in websocket:
        # Message printed everytime we receive a new message
        print(f"Received: {message}")
        await websocket.send(message)
        # Print a message when the client is disconnected
        print("Client disconnected")


async def main():
    # Start the WebSocket server on localhost:8765.
    async with serve(connection_handler, "localhost", 8765) as ws:
        print("Server is running on ws://localhost:8765")
        # Keep the server running forever.
        await ws.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())