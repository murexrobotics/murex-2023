import cgi
import cgitb
import websockets
import asyncio
from websockets.sync.client import connect
import logging
import sys
import os

IP = "localhost"
PORT = 6789

cgitb.enable()
form = cgi.FieldStorage()
command_list = {
    'SEA_LEVEL_PRESSURE': 1013.25,
    'TEMPERATURE_OFFSET': -5,
    'Camera_angle_speed': 15,
    'Joystick_maximum': 0.4,
    'PCA_Frequency': 50,
    'Telemetry_Period': 0.05,
    'MIN_PULSE_WIDTH': 1100,
    'MAX_PULSE_WIDTH': 1900,
    'STOP_DUTY_CYCLE': 5232,
    'MAX_DUTY_CYCLE': 6880,
    'MIN_DUTY_CYCLE': 3600,
    'THRUSTER_INIT_TIME': 7,
    'Restart_Pi?': 0,
    'Restart_PCA9685?': 0,
    'Restart_Camera?': 0
}

for status_name in command_list:
    change = form.getvalue(status_name)
    if change == "Yes" or "Y" or "y":
        command_list[status_name] = 1
    elif change.isnumeric() == True:
        command_list[status_name] = str(change)
    elif change == "No" or "N" or "n":
        command_list[status_name] = 0
    else:
        command_list[status_name] = "INVALID INPUT"

print("Content-Type: text/html")

with connect("ws://localhost:8765") as websocket:
    message = websocket.recv()
    logging.debug(f"Received: {message}")
    for status_name in command_list:
        command = status_name + " : " + str(command_list[status_name])
        logging.debug(f"Telemetry Payload Sent [{command}] on {IP}:{PORT}")
        websocket.send(str(json.dumps(command)))