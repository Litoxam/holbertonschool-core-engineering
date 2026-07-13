#!/usr/bin/env python3

import asyncio
from websockets.asyncio.server import serve
from websockets.exceptions import ConnectionClosed


# Handle each client connection.
async def connection_handler(websocket):
    try:
        async for message in websocket:
            if len(message.strip()) > 0:
                print(f"OK:{message}")
            else:
                print("ERR:EMPTY")

            await websocket.send(message)

    except ConnectionClosed:
        pass


async def main():
    # Start the WebSocket server on localhost:8765.
    async with serve(connection_handler, "localhost", 8765) as ws:
        print("Server is running on ws://localhost:8765")
        # Keep the server running forever.
        await ws.serve_forever()


if __name__ == "__main__":
    asyncio.run(main())
