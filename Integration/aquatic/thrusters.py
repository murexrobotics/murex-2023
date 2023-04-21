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
    
    set_thrust_targets(*thrusts):
        Sets the target thrust value for each thruster

    simple_interpolate(target, duration):
        Interpolates all thrusters to the target thrust over the duration
    
    complex_interpolate(targets, durations):
        Every time it is called it gradually brings thrusters closer to actual thrust target

    start_listening():
        Starts a thread that listens for gamepad input and updates thrusters accordingly

    telemetry():
        Returns a dictionary of telemetry data
"""

from logger import logger
import time
import atexit
import math
import threading

from pca9685 import THRUSTER_CHANNELS
from adafruit_pca9685 import PWMChannel

# Thruster Constants
THRUSTER_INIT_TIME = 7
MIN_PLUSE_WIDTH = 1100
MAX_PLUSE_WIDTH = 1900

STOP_DUTY_CYCLE = 5232
MAX_DUTY_CYCLE = 6880 # IMPORTANT: Subject to change, this was the max achieved in testing but powersupply could not supply sufficient current current
MIN_DUTY_CYCLE = 3600 # IMPORTANT: Subject to change, this was the max achieved in testing but powersupply could not supply sufficient current current

SPEED_UP_TIME = 5 # Time it takes to go from 0 to 1 in seconds

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
            logger.error(message) # It is bad but not quite critical, still warants a program exit though for testing
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
_thrust_targets = [0] * len(_thrusters)
thruster_thread = None
time.sleep(THRUSTER_INIT_TIME)
logger.info("Thrusters Initialized")

def set_thrusts(*thrusts: float):
    """Sets the thrust of each thruster, raises error if invalid number of thrusts is passed"""
    if len(thrusts) != len(_thrusters):
        # This is critical because it interferes with the core purpose of the robot
        logger.error(f"Tried to adjust {len(thrusts)} thrusters with {len(_thrusters)} thrust values")
        raise ValueError("Number of arguments must match number of thrusters")

    for i, thrust in enumerate(thrusts):
        logger.debug(f"Set Thrusters[{i}] to {thrust}")
        _thrusters[i].throttle = thrust

def set_thrust_targets(*thrusts: float):
    """Sets the thrust targets of each thruster, raises error if invalid number of thrusts is passed"""
    if len(thrusts) != len(_thrusters):
        # This is critical because it interferes with the core purpose of the robot
        logger.error(f"Tried to adjust {len(thrusts)} thrusters with {len(_thrusters)} thrust values")
        raise ValueError("Number of arguments must match number of thrusters")

    for i, thrust in enumerate(thrusts):
        logger.debug(f"Set Thrusters[{i}] Target to {thrust}")
        _thrust_targets[i] = thrust

def simple_interpolate(target, duration):
    """Interpolates between min_value and max_value in steps steps over time time"""
    steps = duration * 10
    current = _thrusters[0].throttle
    step_size = (target - current) / steps

    ds = current
    for _ in range(steps):
        set_thrusts(*([ds] * 6))
        ds += step_size
        time.sleep(duration / steps)

def complex_interpolation_step(*targets):
    """Brings each thruster closer to its target"""
    for i, target in enumerate(targets):
        current_thrust = _thrusters[i].throttle
        logger.debug(f"Current Thrust[{i}]: {current_thrust}")
        _thrusters[i].throttle += math.copysign(1, target - current_thrust) * (0.05 / SPEED_UP_TIME)
        _thrusters[i].throttle = min(max(_thrusters[i].throttle, -1), 1)

def telemetry():
    return { 
        "thruster": {
            "fr": _thrusters[0].throttle,
            "fl": _thrusters[1].throttle,
            "br": _thrusters[2].throttle,
            "bl": _thrusters[3].throttle,
            "v1": _thrusters[4].throttle,
            "v2": _thrusters[5].throttle
        }
    }

def start_listening():
    global thruster_thread

    def _thruster_event_loop():
        # TODO: Expand further
        while True:
            complex_interpolation_step(*_thrust_targets)
            logger.debug(_thrust_targets)
            time.sleep(0.05)

    thruster_thread = threading.Thread(target=_thruster_event_loop)
    thruster_thread.start()

def _stop():
    """Stops all thrusters"""
    logger.info("Stopping thrusters")
    set_thrusts(0, 0, 0, 0, 0, 0)
    time.sleep(0.3) # Give time for all thrusters to stop

    try:
        thruster_thread.join()
    except:
        logger.warning("Thruster update thread was not started")
        exit()

# Gracefully stop thrusters on exit
atexit.register(_stop)

if __name__ == '__main__':
    """Test Thrusters"""
    logger.info("Testing thrusters")
    
    from time import sleep
    assert len(_thrusters) == 6, "Thrusters not initialized properly, there should be 6"

    logger.info("Assertions passed, testing thrusters")


    start_listening()

    set_thrust_targets(1, 1, 1, 1, 1, 1)
    time.sleep(6)
    set_thrust_targets(-1, -1, -1, -1, -1,- 1)
    time.sleep(6)
    set_thrust_targets(0, 0, 0, 0, 0, 0)
    time.sleep(6)

    # time.sleep(1)
    # simple_interpolate(
    #     target=0.5, 
    #     duration=5
    # )
    # time.sleep(1)
    # simple_interpolate(
    #     target=0, 
    #     duration=5
    # )
    # time.sleep(1)


    logger.info("Testing complete")




