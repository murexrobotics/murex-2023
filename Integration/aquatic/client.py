import asyncio
import websockets

async def hello():
    uri = "ws://192.168.100.1:1234"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print(f"<<< {message}")

if __name__ == "__main__":
    asyncio.run(hello())