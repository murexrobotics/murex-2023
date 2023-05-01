import command
import asyncio
from logger import logger
import os
from threading import Thread
import atexit


logger.info("Starting Camera Stream on new thread")
video_stream = Thread(
    target=os.system,
    args=("ffplay -fflags nobuffer -flags low_delay -framedrop -vf vflip -probesize 32 -strict experimental udp://192.168.100.1:1234",)
)
video_stream.start()

def _stop():
    logger.info("Stopping Camera Stream")
    video_stream.join()
    
atexit.register(_stop)

# emergency.register(
#     telemetry_target="bme680.temperature",
#     min=10,
#     max=20
# )

asyncio.run(command.start())





