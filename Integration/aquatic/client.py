import asyncio
import websockets

IP = "192.168.100.1"
# IP = "192.168.100.54"
PORT = 5678
# PORT = 6789

async def hello():
    uri = f"ws://{IP}:{PORT}"
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            print(f"<<< {message}")

if __name__ == "__main__":
    asyncio.run(hello())