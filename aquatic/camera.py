"""
Contains all code necessary to control camera. Use the methods 
to interact with camera angle, rather than interacting directly 
with camera.camera.angle unless you need to access the value of 
the angle. There are safety checks in place to avoid over turning 
the camera. Module also handles streaming video over FFmpeg.

Note: Importing a module runs all the code inside of it,
however, python modules are also singleton by nature. At 
any given time only one instance can be created. Thus the 
code in this file will run only once, on the first import, 
making it suitable for initialization

See individual functions for more information

Example:
--------
```Python
# intialize camera
import camera

# Automatically starts streaming over FFmpeg
# Change camera angle as needed
camera.set_angle(130)

...
```

Constants:
----------
    MIN_ANGLE (int): Minimum safe angle where camera does not contact enclosure
    MAX_ANGLE (int): Maximum safe angle where camera does not contact enclosure


Functions:
----------
    set_angle(angle) -> angle:
        Sets angle of camera servo

    telemetry():
        Returns a dictionary of telemetry data

"""

from threading import Thread
import atexit
import os

from logger import logger
from adafruit_motor.servo import Servo
from pca9685 import CAMERA_SERVO_CHANNEL

MIN_ANGLE = 40
MAX_ANGLE = 140

logger.info("Initializing Camera Servo")
camera = Servo(CAMERA_SERVO_CHANNEL)
camera.angle = 90

def set_angle(angle):
    """Sets the camera servo angle"""
    # Truncate to make sure it doesn't hit the glass wall
    if angle != (new_angle := max(min(angle, MAX_ANGLE), MIN_ANGLE)):
        logger.warning("Passed in angle to large/ small for enclosure, truncating")
        angle = new_angle
    
    logger.debug(f"Setting camera angle: {angle}")
    camera.angle = angle
    return angle

def telemetry():
    """Returns telemetry data"""
    return { "camera_angle": camera.angle }


logger.info("Starting Camera Stream on new thread")
video_stream = Thread(
    target=os.system,
    args=("ffmpeg -f v4l2 -i /dev/video0 -c:v h264_v4l2m2m -vf scale=1440x900 -b:v 3000k -fflags nobuffer -flags low_delay -preset ultrafast -tune zerolatency -probesize 32 -num_output_buffers 32 -num_capture_buffers 16 -analyzeduration 0 -f mpegts udp://192.168.100.54:1234",)
)
video_stream.start()

def _stop():
    """Gracefully reset camera angle and end video stream"""
    logger.info("Stopping camera stream")
    camera.angle = 90
    video_stream.join()

logger.debug("Registering Camera deinitialitialization")
atexit.register(_stop)


if __name__ == "__main__":
    """Test code for camera servo"""
    logger.info("Testing camera servo")

    from time import sleep

    set_angle(40)
    print(telemetry())

    sleep(1)

    set_angle(140)
    print(telemetry())

    logger.info("Done testing camera servo")