from adafruit_pca9685 import PCA9685
import logging
from adafruit_motor.servo import Servo
import time

from .gamepad import Gamepad

THRUSTER_INIT_TIME = 7
MIN_PLUSE_WIDTH = 1100
MAX_PLUSE_WIDTH = 1900

# Same code can be generalized to work with BLDC motors too
class Thrusters():
    def __init__(self, channels):
        logging.info("Initializing Thrusters, waiting 7 seconds")
        self.thrusters = [Servo(
            pwm_out=channel, 
            min_pulse=MIN_PLUSE_WIDTH, 
            max_pulse=MAX_PLUSE_WIDTH
        ) for channel in channels]

        self.thrusters.map(lambda thruster: thruster.fraction(0.5))
        time.sleep(THRUSTER_INIT_TIME)
        logging.info("Thrusters Initialized")

    def _set_thrusts(self, *thrusts):
        if len(thrusts) != len(self.thrusters):
            # This is critical because it interferes with the core purpose of the robot
            logging.critical(f"Tried to adjust {len(thrusts)} thrusters with {len(self.thrusters)} thrust values")
            raise ValueError("Number of arguments must match number of thrusters")

        for i, thrust in enumerate(thrusts):
            # Sets bounds on thrust
            thrust = min(max(thrust, -1), 1)

            # SPEED/2 + 0.5 is used to translate fraction from -1 <-> 1
            thrust_frac = (thrust / 2) + 0.5
            logging.debug(f"Set Thrusters[{i}] to {thrust_frac}")
            self.thrusters[i].fraction(thrust_frac)

    def adjust_magnitudes_from_gamepad(self, gamepad: Gamepad):
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

        self._set_thrusts(
            thruster_fr,
            thruster_fl,
            thruster_br,
            thruster_bl,
            thruster_v,
            thruster_v
        )

    def telemetry(self):
        return { "thrusters": {
            "fr": self.thrusters[0].fraction,
            "fl": self.thrusters[1].fraction,
            "br": self.thrusters[2].fraction,
            "bl": self.thrusters[3].fraction,
            "v": self.thrusters[4].fraction
        }}
    
    def __del__(self):
        logging.info("Stopping thrusters")
        # Should stop motors
        self.thrusters.map(lambda thruster: thruster.fraction(0.5))

