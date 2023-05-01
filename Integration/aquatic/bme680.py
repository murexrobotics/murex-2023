from logger import logger
from adafruit_bme680 import Adafruit_BME680_I2C
from i2c import i2c

SEA_LEVEL_PRESSURE = 1013.25
TEMPERATURE_OFFSET = -5

class BME680():
    def __init__(self, i2c):
        logger.info("Initializing BME680")
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

bme = BME680(i2c)


if __name__ == "__main__":
    """Test code for BME680"""
    logger.info("Testing BME680")
    
    from i2c import i2c
    assert i2c.scan() is not [], "No I2C devices found"

    logger.info("Assertions Passed, testing BME680")

    bme680 = BME680(i2c)
    print(bme680.telemetry())
    logger.info("Done testing BME680")
