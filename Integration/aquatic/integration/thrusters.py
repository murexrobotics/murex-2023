"""
Contains all code nececary to control thrusters. Use the methods 
to interact with thrusters, rather than interacting directly 
with _thrusters, the thrusters are represented with Adafruit Servo 
Class. While this is convenient for PWM, this does not reflect the 
actual usage of the thrusters and can be misleading to someone who 
is not familiar with the codebase.

Note: Importing a module runs all the code inside of it,
however, python modules are also singleton by nature. At 
any given time only one instance can be created. Thus the 
code in this file will run only once, on the first import, 
making it suitable for initialization

See individual functions for more information

Example:
--------
```Python
#intialize thrusters
import thrusters
# initialize gamepad
import gamepad

thrusters.adjust_magnitudes_from_gamepad(gamepad)
...
```

Constants:
----------
    THRUSTER_INIT_TIME (int): Time in seconds to wait for thrusters to initialize
    MIN_PLUSE_WIDTH (int): Minimum pulse width for thrusters
    MAX_PLUSE_WIDTH (int): Maximum pulse width for thrusters

    
Functions:
----------
    set_thrusts(*thrusts):
        Sets the thrust of each thruster

    adjust_magnitudes(gamepad: Gamepad):
        Adjusts the thrust of each thruster based on the gamepad

    telemetry():
        Returns a dictionary of telemetry data

        
Todo:
-----
    * Abstract parts of thruster code to work with BLDC motors
    * More + Better logging
    * Implement set_thrusters from the original integration code
"""

import logging
from adafruit_motor.servo import Servo
import time
import atexit

from .gamepad import Gamepad
from .pca9685 import THRUSTER_CHANNELS

# Thruster Constants
THRUSTER_INIT_TIME = 7
MIN_PLUSE_WIDTH = 1100
MAX_PLUSE_WIDTH = 1900

# Actually initialize thrusters
_thrusters = [Servo(
    pwm_out=channel,
    min_pulse=MIN_PLUSE_WIDTH,
    max_pulse=MAX_PLUSE_WIDTH
) for channel in THRUSTER_CHANNELS]

_thrusters.map(lambda thruster: thruster.fraction(0.5))
time.sleep(THRUSTER_INIT_TIME)
logging.info("Thrusters Initialized")


# Thruster Methods
def set_thrusts(*thrusts: float):
    """Sets the thrust of each thruster, raises error if invalid number of thrusts is passed"""
    if len(thrusts) != len(_thrusters):
        # This is critical because it interferes with the core purpose of the robot
        logging.critical(f"Tried to adjust {len(thrusts)} thrusters with {len(_thrusters)} thrust values")
        raise ValueError("Number of arguments must match number of thrusters")

    for i, thrust in enumerate(thrusts):
        # Sets bounds on thrust
        thrust = min(max(thrust, -1), 1)

        # SPEED/2 + 0.5 is used to translate fraction from -1 <-> 1
        thrust_frac = (thrust / 2) + 0.5
        logging.debug(f"Set Thrusters[{i}] to {thrust_frac}")
        _thrusters[i].fraction(thrust_frac)

def adjust_magnitudes(gamepad: Gamepad):
    """Adjusts the thrust of each thruster based on the gamepad state"""
    logging.info("Updating thrusters from gamepad")
    # Aidan's Thrust Vectoring Formula
    turn_right, turn_left = gamepad.turn
    [left_joystick_x, left_joystick_y] = gamepad.left_joystick

    thruster_fr = ((-left_joystick_y + left_joystick_x) / (2 ** 0.5)) + turn_left
    thruster_fl = ((left_joystick_y + left_joystick_x) / (2 ** 0.5)) + turn_right
    thruster_br = ((left_joystick_y + left_joystick_x) / (2 ** 0.5)) + -turn_left
    thruster_bl = ((-left_joystick_y + left_joystick_x) / (2 ** 0.5)) + -turn_right

    # ± 0.1 Vertical Deadzoning
    [_, right_joystick_y] = gamepad.right_joystick
    thruster_v = right_joystick_y if abs(right_joystick_y) > 0.1 else 0

    set_thrusts(
        thruster_fr,
        thruster_fl,
        thruster_br,
        thruster_bl,
        thruster_v,
        thruster_v
    )

def telemetry():
    return { "thrusters": {
        "fr": _thrusters[0].fraction,
        "fl": _thrusters[1].fraction,
        "br": _thrusters[2].fraction,
        "bl": _thrusters[3].fraction,
        "v": _thrusters[4].fraction
    }}

def _stop():
    """Stops all thrusters"""
    logging.info("Stopping thrusters")
    set_thrusts(0, 0, 0, 0, 0, 0)

# Gracefully stop thrusters on exit
atexit.register(_stop)


