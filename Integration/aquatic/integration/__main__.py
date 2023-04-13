import os
from logger import logger
import time

from bme680 import bme
import thrusters
import telemetry

# from camera import Camera

logger.info("Starting Camera")
os.system("ffmpeg -f v4l2 -i /dev/video0 -c:v h264_v4l2m2m -vf scale=1440x900 -b:v 3000k -fflags nobuffer -flags low_delay -preset ultrafast -tune zerolatency -probesize 32 -num_output_buffers 32 -num_capture_buffers 16 -analyzeduration 0 -f mpegts udp://192.168.100.54:1234")
telemetry.start(bme, thrusters)

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

