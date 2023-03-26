import websockets
import atexit
import json
import logging

IP = "192.168.100.1"
PORT = 1234

async def echo(websocket):
    async for message in websocket:
        await websocket.send(message)

connection = websockets.serve(echo, IP, PORT)

def send(*components):
    telemetry_data = dict()

    for component in components:
        if hasattr(component, "telemetry") and callable(component.telemetry):
            temp_telemetry = component.telemetry()
            telemetry_data.update(temp_telemetry)
        else:
            raise TypeError(f"Object {component} does not have a telemetry method")
        
    connection.send(str(json.dumps(telemetry_data)))

def _stop():
    connection.close()

# Gracefully close the connection when the program exits
atexit.register(_stop)

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logging.warn("No tests written for telemetry data, exiting...")
        
    

