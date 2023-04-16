from flask import Flask,request,render_template,redirect
import socket
import sys

ip = "192.168.100.1"
port = 5678

command_list = {
    'Restart_Pi?': 0,
    'Restart_PCA9685?': 0,
    'Restart_Camera?': 0
}

app = Flask(__name__)

@app.route('/report',methods = ["POST"])
def upload_image():
    change = request.files[status_name]
    if change == "Yes" or "Y" or "y":
        command_list[status_name] = 1
    elif change.isnumeric() == True:
        command_list[status_name] = str(change)
    elif change == "No" or "N" or "n":
        command_list[status_name] = "INVALID INPUT"
    return render_template("/routes/+page.svelte",filename=filename)

@app.route('/display/<filename>')

app.run(debug=True,port=2000)
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