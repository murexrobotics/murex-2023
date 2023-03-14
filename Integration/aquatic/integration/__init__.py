import i2c
import pca9685
import bme680
import pixel
import gamepad
import thrusters
import camera

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename="DEBUGLOG.log",
    filemode="w",
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
    datefmt='%H:%M:%S'
)