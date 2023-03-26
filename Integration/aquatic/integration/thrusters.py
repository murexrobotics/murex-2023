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

thrusters.adjust_magnitudes(gamepad)
...
```

Constants:
----------
    THRUSTER_INIT_TIME (int): Time in seconds to wait for thrusters to initialize
    MIN_PLUSE_WIDTH (int): Minimum pulse width for thrusters
    MAX_PLUSE_WIDTH (int): Maximum pulse width for thrusters

    STOP_DUTY_CYCLE (int): Duty cycle for thrusters to stop
    MAX_DUTY_CYCLE (int): Maximum duty cycle for thrusters
    MIN_DUTY_CYCLE (int): Minimum duty cycle for thrusters


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
import time
import atexit

from gamepad import Gamepad
from pca9685 import THRUSTER_CHANNELS
from adafruit_pca9685 import PWMChannel

# Thruster Constants
THRUSTER_INIT_TIME = 7
MIN_PLUSE_WIDTH = 1100
MAX_PLUSE_WIDTH = 1900

STOP_DUTY_CYCLE = 5232
MAX_DUTY_CYCLE = 6880 # IMPORTANT: Subject to change, this was the max achieved in testing but powersupply could not supply sufficient current current
MIN_DUTY_CYCLE = 3600 # IMPORTANT: Subject to change, this was the max achieved in testing but powersupply could not supply sufficient current current

# Actually initialize thrusters

class Thruster():
    def __init__(self, channel: PWMChannel):
        self.pwm_channel = channel
        self.pwm_channel.duty_cycle = STOP_DUTY_CYCLE
        self._throttle = 0

    @property
    def throttle(self):
        return self._throttle

    @throttle.setter
    def throttle(self, throttle: float):
        if throttle > 1 or throttle < -1:
            message = f"Thruster throttle set to {throttle}, which is outside of the range [-1, 1]"
            logging.error(message) # It is bad but not quite critical, still warants a program exit though for testing
            # For competition, errors should be handled differently so that the program does not exit while in the water even if something critical goes wrong
            raise ValueError(message)
        
        self._throttle = throttle
        
        if throttle < 0:
            self.pwm_channel.duty_cycle = STOP_DUTY_CYCLE - int(abs(throttle) * (STOP_DUTY_CYCLE - MIN_DUTY_CYCLE))
        elif throttle > 0:
            self.pwm_channel.duty_cycle = STOP_DUTY_CYCLE + int(throttle * (MAX_DUTY_CYCLE - STOP_DUTY_CYCLE))
        else:
            self.pwm_channel.duty_cycle = STOP_DUTY_CYCLE
        
    def deinit(self):
        self.pwm_channel.duty_cycle = STOP_DUTY_CYCLE

_thrusters = [Thruster(channel) for channel in THRUSTER_CHANNELS]
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
        logging.debug(f"Set Thrusters[{i}] to {thrust}")
        _thrusters[i].throttle = thrust

def adjust_magnitudes(gamepad: Gamepad):
    """Adjusts the thrust of each thruster based on the gamepad state"""
    # TODO: Update this so it uses new thrust vectoring formula and add togglable thrust normalization mode.
    logging.info("Updating thrusters from gamepad")

    # Aidan's Old Thrust Vectoring Formula
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
        "fr": _thrusters[0].throttle,
        "fl": _thrusters[1].throttle,
        "br": _thrusters[2].throttle,
        "bl": _thrusters[3].throttle,
        "v": _thrusters[4].throttle,
    }}

def _stop():
    """Stops all thrusters"""
    logging.info("Stopping thrusters")
    set_thrusts(0, 0, 0, 0, 0, 0)

# Gracefully stop thrusters on exit
atexit.register(_stop)

if __name__ == '__main__':
    """Test Thrusters"""
    logging.basicConfig(level=logging.DEBUG)
    logging.info("Testing thrusters")
    
    from time import sleep
    assert len(_thrusters) == 6, "Thrusters not initialized properly, there should be 6"

    logging.info("Assertions passed, testing thrusters")

    set_thrusts(1, 1, 1, 1, 1, 1)
    sleep(1)
    set_thrusts(-1, -1, -1, -1, -1, -1)
    sleep(1)

    logging.info("Testing complete")




