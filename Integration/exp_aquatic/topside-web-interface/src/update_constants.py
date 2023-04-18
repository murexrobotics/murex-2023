#!C:\Python27\python.exe
import cgi
import cgitb
import socket
import sys

ip = "192.168.100.1"
port = 5678

cgitb.enable()
form = cgi.FieldStorage()

#default constants
command_list = {
    'SEA_LEVEL_PRESSURE': 1013.25,
    'TEMPERATURE_OFFSET': -5,
    'Camera_angle_speed': 15,
    'Joystick_maximum': 0.2,
    'PCA_Frequency': 50,
    'Telemetry_Period': 1,
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

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0)
    print("connection established to rpi")
    for status_name in command_list:
        command = status_name + " : " + command_list[status_name]
        s.sendto(command.encode('utf-8'), (ip, port))
        print("Client Sent --- ", command)
    s.close()
except:
    print("connection failed")

print('''
<a href="/routes/+page.svelte" class="button">Exit</a>
''')