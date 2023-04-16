import cgi
import cgitb
import socket
import sys

ip = "192.168.100.1"
port = 5678

#cgitb.enable()
form = cgi.FieldStorage()

command_list = {
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
        command_list[status_name] = "INVALID INPUT"

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