"""
Contains all code nececary to control arm. Use the methods 
to interact with arm, rather than interacting directly 
with claw and pivot. Using claw and pivot might lead to 
situations where an angle not suitable for the claw is 
passed in potentially damaging the ROV.

Note: Importing a module runs all the code inside of it,
however, python modules are also singleton by nature. At 
any given time only one instance can be created. Thus the 
code in this file will run only once, on the first import, 
making it suitable for initialization

See individual functions for more information

Example:
--------
```Python
import arm
import time

arm.set_pivot(90)

# Open Claw
arm.set_claw_position(1)
time.sleep(1)
# Close Claw
arm.set_claw_position(0)
...
```

Constants:
----------
    MAX_PIVOT (int): Maximum angle for arm pivot
    MIN_PIVOT (int): Minimum angle for arm pivot

    MAX_CLAW (int): Maximum angle for arm claw
    MIN_CLAW (int): Minimum angle for arm claw


Functions:
----------
    set_pivot(angle): 
        Sets the arm pivot angle

    change_pivot(angle): 
        Change the arm pivot angle

    set_claw_position(fraction: float): 
        Sets the arm claw position

    change_claw_position(fraction: float): 
        Change the arm claw position
"""

from adafruit_motor.servo import Servo
from pca9685 import ARM_CLAW_CHANNEL, ARM_PIVOT_CHANNEL
from logger import logger
import time

claw = Servo(ARM_CLAW_CHANNEL)
pivot = Servo(ARM_PIVOT_CHANNEL)

MAX_PIVOT = 180
MIN_PIVOT = 0

MAX_CLAW = 180
MIN_CLAW = 85

def set_pivot(angle):
    """Sets the arm pivot angle"""
    # Truncate to make sure it doesn't hit the glass wall
    if angle != (new_angle := max(min(angle, MAX_PIVOT), MIN_PIVOT)):
        logger.warning("Passed in angle to large/ small for enclosure, truncating")
        angle = new_angle
    
    logger.debug(f"Setting arm pivot angle: {angle}")
    pivot.angle = angle
    return angle

def change_pivot(angle):
    """Change the arm pivot angle"""
    # Truncate to make sure it doesn't hit the glass wall
    angle += pivot.angle
    if angle != (new_angle := max(min(angle, MIN_PIVOT), MIN_PIVOT)):
        logger.warning("Passed in change makes angle to large/ small, truncating")
        angle = new_angle

    logger.debug(f"Setting arm pivot angle: {angle}")
    pivot.angle = angle
    return angle

def set_claw_position(fraction: float):
    """Sets the arm pivot angle"""
    if fraction != (new_fraction := max(min(fraction, 0), 1)):
        logger.warning("Fraction passed in must be between 0-1, truncating")
        fraction = new_fraction
    
    logger.debug(f"Setting claw fraction: {fraction}")
    pivot.angle = (fraction * (MAX_CLAW - MIN_CLAW)) + MIN_CLAW
    return fraction

def change_claw_position(fraction: float):
    """Change the arm pivot angle"""
    fraction += (pivot.angle - MIN_CLAW) / (MAX_CLAW - MAX_CLAW)
    if fraction != (new_fraction := max(min(fraction, 0), 1)):
        logger.warning("Fraction passed makes net fraction too large/ small, truncating")
        fraction = new_fraction

    logger.debug(f"Setting claw fraction: {fraction}")
    pivot.angle = fraction
    return fraction

if __name__ == "__main__":
    logger.info("Performing intialization assertions for arm")
    assert claw != None, "Claw not initialized"
    assert pivot != None, "Arm pivot not initialized"

    logger.info("Starting movement test")
    # CLAW
    set_claw_position(0.5)
    time.sleep(1.5)
    set_claw_position(1)
    time.sleep(1.5)
    change_claw_position(-0.75)
    time.sleep(1.5)

    # PIVOT
    set_pivot(90)
    time.sleep(1.5)
    set_pivot(180)
    time.sleep(1.5)
    change_pivot(-45)
    time.sleep(1.5)

    logger.warning("Inspect claw to make sure tests passed")
