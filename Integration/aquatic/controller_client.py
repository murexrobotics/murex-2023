import asyncio
import websockets
import json

async def listen(thrusters):
    uri = "ws://localhost:6789" # TODO: CHANGE TO COMPUTER IP

    if not hasattr(thrusters, "_thruster_targets"):
        raise Exception("Thrusters not initialized")
    
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            data = json.loads(message)
            thrusters._thruster_targets = [data["fr"], data["fl"], data["bl"], data["br"], data["v"], data["v"]]

if __name__ == "__main__":
    asyncio.run(listen())