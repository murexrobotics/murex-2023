import logging
import os
from socket import socket, AF_INET, SOCK_DGRAM

from .gamepad import Gamepad
from .thrusters import Thrusters
from .bme680 import BME680
from .camera import Camera
from .pixels import Pixels

logging.basicConfig(
    level=logging.DEBUG, 
    filename="DEBUGLOG.log", 
    filemode="w", 
    format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s', 
    datefmt='%H:%M:%S'
)

gamepad = Gamepad()
thrusters = Thrusters()
bme680 = BME680()
camera = Camera()
pixels = Pixels()

os.system("ffmpeg -f v4l2 -i /dev/video0 -c:v h264_v4l2m2m -b:v 125000 -fflags nobuffer -flags low_delay -preset ultrafast -tune zerolatency -probesize 32 -num_output_buffers 32 -num_capture_buffers 16 -analyzeduration 0 -f mpegts udp://192.168.100.52:1234")

ip = "192.168.100.1"
port = 6666

# Create socket for server
server = socket(AF_INET, SOCK_DGRAM, 0)
server.bind((ip, port))

while True:
    hid_code, game_state = gamepad.get_new_input()
    thrusters.adjust_magnitudes_from_gamepad(gamepad)

    # @TODO: experimental support for arm motors
    # arm_bldcs[0] = claw
    # arm_bldcs[1] = servo
    # arm_bldcs[2] = turning 1
    # arm_bldcs[3] = turning 2

    camera.rotate(hid_code, game_state)

    # @TODO: host webserver with telemetry/diagnostic data?
    # @TODO: better debugging/logging potential

    # Change color of Neopixel
    # Nothing curretnly changes color of Neopixel
    pixels.show()

    # Stream Telemetry
    # asyncio.run(telemetry_server.main(output_dictionary))

