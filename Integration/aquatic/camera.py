from logger import logger
from adafruit_motor.servo import Servo

class Camera():
    # TODO: Add the actual functionality of the camera
    def __init__(self, channel):
        logger.info("Initializing Camera")
        self.camera_servo = Servo(channel)
        self.angle = 0

    def rotate(self, hid_code, game_state):
        logger.debug(f"Rotating camera...")
        if hid_code == "ABS_HAT0Y":
            if game_state == 1:
                self.angle += 15

            elif game_state == -1:
                self.angle -= 15

            if self.angle > 180 or self.angle < 0:
                self.camera_servo.angle(self.angle)

        logger.debug(f"New camera angle: {self.angle}")
        return self.angle

    def __del__(self):
        logger.info("Resetting camera angle")
        self.camera_servo.angle = 0

    def telemetry(self):
        return { "camera": {
            "camera_angle": self.angle
        }}

if __name__ == "__main__":
    """Test code for camera servo"""
    logger.info("Testing camera servo")

    from pca9685 import CAMERA_SERVO_CHANNEL
    from time import sleep

    camera = Camera(CAMERA_SERVO_CHANNEL)
    camera.rotate("ABS_HAT0Y", 45)
    print(camera.telemetry())
    sleep(1)
    camera.rotate("ABS_HAT0Y", 135)
    print(camera.telemetry())

    logger.info("Done testing camera servo")