#! SOURCE: https://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output

import logging

class Formatter(logging.Formatter):
    grey = "\x1b[36;20m"
    green = "\x1b[32;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(filename)s:%(lineno)d - %(levelname)s - %(message)s"

    FORMATS = {
        logging.DEBUG: green + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt, datefmt='%I:%M:%S %p')
        return formatter.format(record)
    
# create logger with 'spam_application'
logger = logging.getLogger("Murex")
logger.setLevel(logging.DEBUG)

# create console handler with a higher log level
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(Formatter())
logger.addHandler(ch)

if __name__ == "__main__":
    logger.debug("Test Debug")
    logger.info("Test Info")
    logger.warning("Test Warning")
    logger.error("Test Error")
    logger.critical("Test Critical")
