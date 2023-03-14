"""
Initializes Neopixel and exposes methods for easy usage.

Note: Importing a module runs all the code inside of it,
however, python modules are also singleton by nature. At 
any given time only one instance can be created. Thus the 
code in this file will run only once, on the first import, 
making it suitable for initialization

Example:
--------
```Python
# intialize neopixel
import pixel

# Set color
pixel.set_color(
    red=255,
    green=255,
    blue=255
)

# Light up neopixel
pixel.show()
...
```

Atrributes:
-----------
    red (int): Red value for neopixel color
    green (int): Green value for neopixel color
    blue (int): Blue value for neopixel color

    
Functions:
----------
    set_color(red, green, blue):
        Sets the color of neopixel, if channel is not specified, it won't be updated, takes kwargs.

    set_brightness(brightness):
        Sets the brightness of th neopixel

    show():
        Lights up neopixel

        
Todo:
-----
    * Enforce kwargs for set_color
    * More + Better logging
    * Telemetry/ diagnostics data
"""

import logging
import board
from neopixel import NeoPixel, GRB
import atexit

logging.info("Initializing Pixels")
_neopixel = NeoPixel(
    pin = board.D18,
    n = 1,
    brightness = 0.2,
    auto_write = False,
    pixel_order = GRB
)

red = 255
green = 255
blue = 255

def set_color(_red: int = None, _green: int = None, _blue: int = None):
    """Takes in keyword arguments for Neopixel color, updates neopixel color."""

    # Using global variables like this is bad practice, find better alternative
    global red, green, blue

    if _red > 255 or _green > 255 or _blue > 255:
        raise ValueError("Cannot set RGB value of Neopixel to something greater than 255")
    
    if _red < 0 or _green < 0 or _blue < 0:
        raise ValueError("Cannot set RGB value of Neopixel to something less than 0")
    
    red = _red if _red else red
    green = _green if _green else green
    blue = _blue if _blue else blue
    _neopixel.fill((red, green, blue))

def set_brightness(brightness: float):
    "Sets brightness of neopixel."
    if brightness > 1 or brightness < 0:
        raise ValueError(f"Brightness must be between 0 and 1, {brightness} as passed")
    
    _neopixel.brightness = brightness

def show():
    """Lights up neopixel"""
    _neopixel.show()

def _stop():
    """Gracefully shuts of neopixel"""
    _neopixel.deinit()

atexit.register(_stop)