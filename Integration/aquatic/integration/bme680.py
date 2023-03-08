import logging
from adafruit_bme680 import Adafruit_BME680_I2C

SEA_LEVEL_PRESSURE = 1013.25
TEMPERATURE_OFFSET = -5

class BME680():
    def __init__(self, i2c):
        logging.info("Initializing BME680")
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
        return { "bme680": {
            "temperature": self.temperature,
            "humidity": self.humidity,
            "pressure": self.pressure,
            "gas": self.gas,
            "altitude": self.altitude
        }}
    