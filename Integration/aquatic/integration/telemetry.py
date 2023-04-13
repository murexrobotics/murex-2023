"""
Initializes PCA9685, and defines channels to be used for 
each component. (Deinitializes on program exit)

Note: Importing a module runs all the code inside of it,
however, python modules are also singleton by nature. At 
any given time only one instance can be created. Thus the 
code in this file will run only once, on the first import, 
making it suitable for initialization

Example:
--------
```Python
# Import telemetry
import telemetry

# Initialize components
import thrusters
import gamepad
import bme680

# Start telemetry server
telemetry.start(gamepad, thrusters, bme680)
...
```

Constants:
----------
    IP (str): IP address of telemetry server
    PORT (int): Port of telemetry server
    PERIOD (float): Period between each transmission of telemetry data

Functions:
----------
    start(*components): Starts telemetry server that send updated from components
"""

import asyncio
import websockets
import json
from logger import logger

IP = "192.168.100.1"
PORT = 1234
PERIOD = 1 # Adjust as needed, controls how often telemetry is sent


def _handler(*components):
    """Returns handler function for telemetry websocket server"""
    async def send(websocket):
        """Sends telemetry data to client"""
        while True:
            telemetry_data = dict()

            for component in components:
                if hasattr(component, "telemetry") and callable(component.telemetry):
                    temp_telemetry = component.telemetry() # Aggregate telemetry data from component
                    telemetry_data.update(temp_telemetry) # Store findings
                else:
                    # If object does not have associated telemetry method something wrong has been passed in
                    logger.error(f"Object {component} does not have a telemetry method")
                    raise TypeError(f"Object {component} does not have a telemetry method")
            
            logger.debug(f"Telemetry Payload Sent: {telemetry_data}")
            await websocket.send(str(json.dumps(telemetry_data))) # Send telemetry data to client
            await asyncio.sleep(PERIOD)
            
    return send

async def start(*components):
    """Starts telemetry websocket server"""
    async with websockets.serve(_handler(*components), IP, PORT):
        logger.info(f"Telemetry server started on {IP}:{PORT}")
        await asyncio.Future() # TODO: Swap for something else if there is time

async def _test():
    """Setup mock telemetry server for testing"""
    from i2c import i2c
    from bme680 import BME680
    bme = BME680(i2c) # BME is easiest to test with, but any component can be used

    await start(bme)


if __name__ == "__main__":
    # Running this as server is the test, functionality should be tested manually
    asyncio.run(_test())
