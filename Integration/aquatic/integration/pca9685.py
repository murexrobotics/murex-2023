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

import atexit
from adafruit_pca9685 import PCA9685
from .i2c import i2c

pca = PCA9685(i2c)

THRUSTER_CHANNELS = pca.channels[:6]
ARM_BLDC_CHANNELS = pca.channels[6:10]
CAMERA_SERVO_CHANNEL = pca.channels[10]

def _stop():
    """Deinitializes PCA9685"""
    pca.deinit()

# Make sure that PCA9685 is gracefully shut off so that other 
# components can also be gracefully stopped.
atexit.register(_stop)
