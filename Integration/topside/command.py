import asyncio
import websockets
import json
import logging
from controller import decode_controller_input

IP = "localhost" # TODO: CHANGE TO COMPUTER IP
PORT = 6789
PERIOD = 0.05 # Adjust as needed, controls how often telemetry is sent


async def send(websocket):
    """Sends controller data to client"""
    while True:
        controller_data_raw = decode_controller_input()
        controller_data = {
            "fr": controller_data_raw[0],
            "fl": controller_data_raw[1],
            "bl": controller_data_raw[2],
            "br": controller_data_raw[3],
            "v": controller_data_raw[4]
        }

        logging.debug(f"Telemetry Payload Sent: {controller_data}")
        await websocket.send(str(json.dumps(controller_data))) # Send telemetry data to client
        await asyncio.sleep(PERIOD)

async def start():
    """Starts telemetry websocket server"""
    async with websockets.serve(send, IP, PORT):
        logging.info(f"Telemetry server started on {IP}:{PORT}")
        await asyncio.Future() # TODO: Swap for something else if there is time
