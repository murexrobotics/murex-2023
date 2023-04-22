"""
Initializes BME680

Note: Importing a module runs all the code inside of it,
however, python modules are also singleton by nature. At 
any given time only one instance can be created. Thus the 
code in this file will run only once, on the first import, 
making it suitable for initialization

Example:
--------
```Python
# intialize BME680
from bme680 import bme

# Take whatever data is required
print(bme.temperature)
print(bme.telemetry())
...
```

Atrributes:
-----------
    bme (BME680): Interface for getting data from BME680
"""

import atexit
from logger import logger
from adafruit_bme680 import Adafruit_BME680_I2C
from i2c import i2c

SEA_LEVEL_PRESSURE = 1013.25
TEMPERATURE_OFFSET = -5

class BME680():
    def __init__(self, i2c):
        self.bme680 = Adafruit_BME680_I2C(i2c, debug=False)
        self.bme680.sea_level_pressure = SEA_LEVEL_PRESSURE

    @property
    def temperature(self):
        return self.bme680.temperature + TEMPERATURE_OFFSET

    @property
    def humidity(self):
        return self.bme680.humidity

    @property
    def pressure(self):
        return self.bme680.pressure

    @property
    def gas(self):
        return self.bme680.gas

    @property
    def altitude(self):
        return self.bme680.altitude
    
    def telemetry(self):
        return { 
            "bme680": {
                "temperature": self.temperature,
                "gas": self.gas,
                "humidity": self.humidity,
                "pressure": self.pressure,
                "altitude": self.altitude
            }
        }

# This is what should be imported
logger.info("Initializing BME680")
bme = BME680(i2c)

def _stop():
    """Deinitializes BME680"""
    logger.info("Deinitializing BME680")
    # bme.bme680.deinit()

logger.debug("Registering BME deinitialization")
atexit.register(_stop)

if __name__ == "__main__":
    """Test code for BME680"""
    logger.info("Testing BME680")
    
    from i2c import i2c
    assert i2c.scan() is not [], "No I2C devices found"

    logger.info("Assertions Passed, testing BME680")
    print(bme.telemetry())
    logger.info("Done testing BME680")
