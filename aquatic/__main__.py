import os
import time
import asyncio
import threading

# IMPORTANT: Initialization Order is important
# IMPORTANT: Do not remove any imports, intialization is done when module is imported
import i2c
import pca9685
import bme680
import camera
import thrusters
import telemetry
import controller_client

from logger import logger

logger.info("Starting auto thruster updater")
thrusters.start_listening()

logger.info("Entering Event Loop")
asyncio.run(controller_client.listen(thrusters, camera))
    



