"""
Initializes PCA9685, and defines channels to be used for 
each component. (Deinitializes on program exit)

Note: Importing a module runs all the code inside of it,
however, python modules are also singleton by nature. At 
any given time only one instance can be created. Thus the 
code in this file will run only once, on the first import, 
making it suitable for initialization

Atrributes:
-----------
    pca (I2C): I2C bus

Constants:
----------
    THRUSTER_CHANNELS (PCAChannels): PWM Channels that are designated for the thrusters
    ARM_BLDC_CHANNELS (PCAChannels): PWM Channels that are deisgnated for the BLDC motors that control the arm
    CAMERA_SERVO_CHANNELS (PCAChannels): PWM Channels to control camera angle
"""

from logger import logger
import atexit
from adafruit_pca9685 import PCA9685
from i2c import i2c

logger.info("Initializing PCA9685")
pca = PCA9685(i2c)
pca.frequency = 50

logger.debug("Allocating PWM Channels")

# Thrusters: FR, FL, BL, BR, V1, V2
THRUSTER_CHANNELS = [pca.channels[5], pca.channels[12], pca.channels[4], pca.channels[15], pca.channels[3], pca.channels[14]] # TODO: Fix order
ARM_BLDC_CHANNELS = pca.channels[6:10]
CAMERA_SERVO_CHANNEL = pca.channels[10]
ARM_CLAW_CHANNEL = pca.channels[13] 
ARM_PIVOT_CHANNEL = pca.channels[11]

def _stop():
    """Deinitializes PCA9685"""
    pca.deinit()

# Make sure that PCA9685 is gracefully shut off so that other 
# components can also be gracefully stopped.
logger.debug("Registering PCA9685 deinitialization")
atexit.register(_stop)

if __name__ == '__main__':
    """Tests PCA9685 initialization"""
    logger.info("Testing PCA9685 initialization")
    assert pca is not None, "PCA9685 not initialized"
    assert i2c.scan() != [], "No I2C devices found, PCA Not registered"
    assert len(THRUSTER_CHANNELS) == 6, "Incorrect number of thruster channels"
    assert len(ARM_BLDC_CHANNELS) == 4, "Incorrect number of arm BLDC channels"
    logger.info("PCA9685 initialized successfully")
