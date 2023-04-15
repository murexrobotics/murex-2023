"""
Initializes I2C bus for parts that communicate over I2C

Note: Importing a module runs all the code inside of it,
however, python modules are also singleton by nature. At 
any given time only one instance can be created. Thus the 
code in this file will run only once, on the first import, 
making it suitable for initialization

Atrributes:
-----------
    i2c (I2C): I2C bus
"""

from busio import I2C
from board import SCL, SDA
from logger import logger

i2c = I2C(SCL, SDA)

if __name__ == '__main__':
    assert i2c is not None, "I2C bus not initialized"