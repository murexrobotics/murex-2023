import os
from logger import logger
import time
import asyncio
import threading

from bme680 import bme
import thrusters
import telemetry
import atexit

# from camera import Camera

logger.info("Starting Camera")
video_stream = threading.Thread(
    target=os.system,
    args=("ffmpeg -f v4l2 -i /dev/video0 -c:v h264_v4l2m2m -vf scale=1440x900 -b:v 3000k -fflags nobuffer -flags low_delay -preset ultrafast -tune zerolatency -probesize 32 -num_output_buffers 32 -num_capture_buffers 16 -analyzeduration 0 -f mpegts udp://192.168.100.54:1234",)
)
video_stream.start()

logger.info("Starting Telemetry Server")
telemetry_server = threading.Thread(
    target=asyncio.run,
    args=(telemetry.start(bme, thrusters),)
)
telemetry_server.start()

def _stop():
    telemetry_server.join()
    video_stream.join()

atexit.register(_stop)


logger.info("Entering Event Loop")
while True:
    time.sleep(1)
    thrusters.interpolate(
        target=0.5, 
        duration=5
    )

    time.sleep(1)
    thrusters.interpolate(
        target=0, 
        duration=5
    )



