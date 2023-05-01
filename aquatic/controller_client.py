"""
Handes websocket connection to the topside for control data.
Currently only supports thruster, camera and arm control but 
can be exapnded for emergency backup signals and other 
components. (Gracefully terminates on program exit)

Note: Importing a module runs all the code inside of it,
however, python modules are also singleton by nature. At 
any given time only one instance can be created. Thus the 
code in this file will run only once, on the first import, 
making it suitable for initialization

Example:
--------
```Python
from controller_client import listen
import asyncio

# Initialize components
import thrusters
import camera
import arm

# Start listening
asyncio.run(listen(thrusters, camera, arm))
...
```

Constants:
----------
    IP (str): IP address of control server
    PORT (int): Port of control server

Functions:
----------
    listen(thrusters, camera, arm): Starts listening for controller data, updates components accordingly
"""

import asyncio
import websockets
import json
import logger

IP = "192.168.100.54"
PORT = 6789

async def listen(thrusters, camera, arm):
    uri = f"ws://{IP}:{PORT}"

    if not hasattr(thrusters, "_thrust_targets"):
        logger.error("Uninitialized Thruster Passed")
        # raise Exception("Thrusters not initialized")
    
    if not hasattr(camera, "camera"):
        logger.error("Unintialized Camera Passed")
        # raise Exception("Camera not initialized")
    
    if not hasattr(camera, "pivot"):
        logger.error("Unintialized Camera Passed")
        # raise Exception("Camera not initialized")
    
    async with websockets.connect(uri) as websocket:
        while True:
            message = await websocket.recv()
            data = json.loads(message)
            thrusters.set_thrust_targets(data["fr"], data["fl"], data["bl"], data["br"], data["v"], data["v"])
            camera.set_angle(camera.camera.angle + data["camera"])

            # TODO: Test this code
            arm.set_pivot(arm.pivot.angle + data["arm_angle"])
            arm.set_claw_position(arm.claw.angle + data["claw"]) # Will go out of bounds, function will truncate but give warnings

if __name__ == "__main__":
    asyncio.run(listen())