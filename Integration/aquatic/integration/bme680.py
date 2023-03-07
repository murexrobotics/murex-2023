import logging
from busio import I2C
from board import SCL, SDA
from adafruit_bme680 import Adafruit_BME680_I2C

SEA_LEVEL_PRESSURE = 1013.25
TEMPERATURE_OFFSET = -5

class BME680():
    def __init__(self):
        logging.info("Initializing BME680")
        i2c = I2C(SCL, SDA)
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
    