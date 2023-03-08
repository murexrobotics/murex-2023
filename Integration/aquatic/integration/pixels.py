import logging
import board
from neopixel import NeoPixel, GRB


class Pixels():
    def __init__(self):
        logging.info("Initializing Pixels")
        self.pixels = NeoPixel(
            pin = board.D18,
            n = 1,
            brightness = 0.2,
            auto_write = False,
            pixel_order = GRB
        )
        self.red = 255
        self.green = 255
        self.blue = 255
    
    def set_color(self, red, green, blue):
        logging.debug(f"Updated pixels color to: {red=}, {green=}, {blue=}")
        self.red = red
        self.green = green
        self.blue = blue
        self.pixels.fill((red, green, blue))

    def set_brightness(self, brightness):
        logging.debug(f"Updated pixels brightness to: {brightness}")
        self.pixels.brightness = brightness

    def show(self):
        self.pixels.show()

    def telemetry(self):
        return { "neopixel": {
            "red": self.red,
            "green": self.green,
            "blue": self.blue
        }}