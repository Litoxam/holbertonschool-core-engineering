#!/usr/bin/env python3

import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed

# Stores all connected clients.
clients = set()


# Handle each client connection.
async def connection_handler(websocket):
    # Add the client to the set.
    clients.add(websocket)
    print("Client connected.")

    try:
        async for message in websocket:
            if message.strip():
                # Send the response to all client
                for client in clients:
                    await client.send(f"B:{message}")

    except ConnectionClosed:
        pass

    finally:
        # Remove the client when it disconnects.
        clients.remove(websocket)
        print("Client disconnected.")


async def main():
    # Start the WebSocket server on localhost:8765.
    async with serve(connection_handler, "localhost", 8765) as ws:
        print("Server is running on ws://localhost:8765")
        await ws.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
