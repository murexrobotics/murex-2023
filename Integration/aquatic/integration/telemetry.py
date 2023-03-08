import logging
import socket

def send_telemetry_data(*sources):
    for source in sources:
        telemetry_data = source.telemetry()
        if telemetry_data:
            logging.debug(f"Sending telemetry data: {telemetry_data}")
            ...