import subprocess
def restart():
    print("restarting Pi")
    command = "/usr/bin/sudo /sbin/ shutdown -r now"
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)

def communicate(command):
    print("running new command")
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output = process.communicate()[0]
    print(output)