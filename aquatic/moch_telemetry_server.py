"""Generates random telemetry data and sends it to the client. Use to test web-interface"""

import asyncio
import json
import random
import threading
import time
import websockets
import random

CONNECTIONS = set()

n = 0
camera_servo_angle = 0
neopixel_r, neopixel_g, neopixel_b = 255, 255, 255
thruster_fr = None
thruster_fl = None
thruster_br = None
thruster_bl = None
thruster_v1 = None
thruster_v2 = None
bldc_0 = None
bldc_1 = None
bldc_2 = None
bldc_3 = None
bme680_temperature = None
bme680_gas = None
bme680_humidity = None
bme680_pressure = None
bme680_altitude = None
joystick_left = None
joystick_right = None
button_y = None
button_x = None
button_b = None
button_a = None
button_view = None
button_menu = None
button_xbox = None
joystick_left_x = None
joystick_left_y = None
joystick_right_x = None
joystick_right_y = None
dpad_up = None
dpad_down = None
dpad_left = None
dpad_right = None
trigger_right = None
trigger_left = None
bumper_right = None
bumper_left = None

output_dictionary = {
    "thruster": {
        "fr": thruster_fr,
        "fl": thruster_fl,
        "br": thruster_br,
        "bl": thruster_bl,
        "v1": thruster_v1,
        "v2": thruster_v2,
    },
    "arm": {
        "bldc_0": bldc_0,
        "bldc_1": bldc_1,
        "bldc_2": bldc_2,
        "bldc_3": bldc_3,
    },
    "bme680": {
        "temperature": bme680_temperature,
        "gas": bme680_gas,
        "humidity": bme680_humidity,
        "pressure": bme680_pressure,
        "altitude": bme680_altitude,
    },
    "joystick": {
        "joystick_left_x": joystick_left_x,
        "joystick_left_y": joystick_left_y,
        "joystick_right_x": joystick_right_x,
        "joystick_right_y": joystick_right_y,
        "button_y": button_y,
        "button_x": button_x,
        "button_b": button_b,
        "button_a": button_a,
        "button_menu": button_menu,
        "button_view": button_view,
        "button_xbox": button_xbox,
        "dpad_up": dpad_up,
        "dpad_down": dpad_down,
        "dpad_left": dpad_left,
        "dpad_right": dpad_right,
        "trigger_right": trigger_right,
        "trigger_left": trigger_left,
        "bumper_right": bumper_right,
        "bumper_left": bumper_left,
    },
    "camera_angle": camera_servo_angle,
    "time": 0,
}

async def register(websocket):
    CONNECTIONS.add(websocket)
    try:
        await websocket.wait_closed()
    finally:
        CONNECTIONS.remove(websocket)

async def echo():
    global n
    while True:
        websockets.broadcast(CONNECTIONS, str(json.dumps(output_dictionary, indent = 4)))
        await asyncio.sleep(1)

async def main():
    async with websockets.serve(register, "localhost", 5678):
        await echo()

def infiniteloop2():
    global output_dictionary
    while True:
        # print(output_dictionary)
        output_dictionary["time"] += 1
        output_dictionary["bme680"]["temperature"] = random.randint(0, 20)
        output_dictionary["bme680"]["gas"] = random.randint(0, 20)
        output_dictionary["bme680"]["humidity"] = random.randint(0, 20)
        output_dictionary["bme680"]["pressure"] = random.randint(0, 20)
        output_dictionary["bme680"]["altitude"] = random.randint(0, 20)
        output_dictionary["thruster"]["fr"] = round(random.uniform(-1, 1), 2)
        output_dictionary["thruster"]["fl"] = round(random.uniform(-1, 1), 2)
        output_dictionary["thruster"]["br"] = round(random.uniform(-1, 1), 2)
        output_dictionary["thruster"]["bl"] = round(random.uniform(-1, 1), 2)
        output_dictionary["thruster"]["v1"] = round(random.uniform(-1, 1), 2)
        output_dictionary["thruster"]["v2"] = round(random.uniform(-1, 1), 2)
        output_dictionary["arm"]["bldc_0"] = round(random.uniform(-1, 1), 2)
        output_dictionary["arm"]["bldc_1"] = round(random.uniform(-1, 1), 2)
        output_dictionary["arm"]["bldc_2"] = round(random.uniform(-1, 1), 2)
        output_dictionary["arm"]["bldc_3"] = round(random.uniform(-1, 1), 2)
        output_dictionary["camera_angle"] = random.randint(0, 180)
        output_dictionary["joystick"]["joystick_left_x"] = round(random.uniform(-1, 1), 2)
        output_dictionary["joystick"]["joystick_left_y"] = round(random.uniform(-1, 1), 2)
        output_dictionary["joystick"]["joystick_right_x"] = round(random.uniform(-1, 1), 2)
        output_dictionary["joystick"]["joystick_right_y"] = round(random.uniform(-1, 1), 2)
        output_dictionary["joystick"]["button_joystick_left"] = random.randint(0, 1)
        output_dictionary["joystick"]["button_joystick_right"] = random.randint(0, 1)
        output_dictionary["joystick"]["button_y"] = random.randint(0, 1)
        output_dictionary["joystick"]["button_x"] = random.randint(0, 1)
        output_dictionary["joystick"]["button_b"] = random.randint(0, 1)
        output_dictionary["joystick"]["button_a"] = random.randint(0, 1)
        output_dictionary["joystick"]["button_menu"] = random.randint(0, 1)
        output_dictionary["joystick"]["button_view"] = random.randint(0, 1)
        output_dictionary["joystick"]["button_xbox"] = random.randint(0, 1)
        output_dictionary["joystick"]["trigger_right"] = random.randint(0, 1)
        output_dictionary["joystick"]["trigger_left"] = random.randint(0, 1)
        output_dictionary["joystick"]["bumper_right"] = random.randint(0, 1)
        output_dictionary["joystick"]["bumper_left"] = random.randint(0, 1)
        output_dictionary["joystick"]["dpad_up"] = random.randint(0, 1)
        output_dictionary["joystick"]["dpad_down"] = random.randint(0, 1)
        output_dictionary["joystick"]["dpad_left"] = random.randint(0, 1)
        output_dictionary["joystick"]["dpad_right"] = random.randint(0, 1)
        print(output_dictionary)
        time.sleep(1)

thread1 = threading.Thread(target=asyncio.run, args=(main(),))
thread1.start()

thread2 = threading.Thread(target=infiniteloop2)
thread2.start()

thread1.join()
thread2.join()
