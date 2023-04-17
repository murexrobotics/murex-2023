import asyncio
import websockets
import json

IP = "192.168.100.54"
PORT = 6789

async def listen(thrusters):
    uri = f"ws://{IP}:{PORT}"

    if not hasattr(thrusters, "_thrust_targets"):
        raise Exception("Thrusters not initialized")
    
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            data = json.loads(message)

            # TODO: Add proppper interpolation
            thrusters.set_thrusts(data["fr"], data["fl"], data["bl"], data["br"], data["v"], data["v"])

if __name__ == "__main__":
    asyncio.run(listen())