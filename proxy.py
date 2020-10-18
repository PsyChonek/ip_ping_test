import os
import sys

path = sys.argv[1]
output = sys.argv[2]

list = open(path, "r")
lines = list.read().split('\n')
list.close()

ip = []

import platform
import subprocess

def ping(host):

    command = ['ping.exe', "-n", '1', host]
    p = subprocess.Popen(command, stdout = subprocess.PIPE)
    return p.communicate()[0]


new_list = open(output, "w")

for line in lines:
    ip = line.split("	")[0]
    print("Checking " + ip)
    origo = ping(ip).decode("utf-8")
    test_check = origo.split("\n")[5].split(",")[1].split(" ")[3]

    if test_check == "1" and origo.split("\n")[2].split(" ")[4] != 'port':
        test_ms = origo.split("\n")[7].split(",")[2].split(" ")[3]
        print("Success.")
        new_list.write(line.split("	")[0] + ":" + line.split("	")[1] + "\t" + test_ms)
    elif test_check == "1":
        print("Port unreachable.")
        new_list.write(line.split("	")[0] + ":" + line.split("	")[1] + "\t" "unreachable"+"\n")
    else:
        print("Error.")

list.close()
import webbrowser
webbrowser.open(output)
