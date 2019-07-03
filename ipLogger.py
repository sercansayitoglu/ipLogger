#! /usr/bin/python3
# run this command --> 'python3 ipLogger.py'
# version 1.0

from urllib.request import urlopen
import time
import signal
import os
from pathlib import Path

clear = "\n" * 100
print (clear)

def signal_handler(signal, frame):
        exit()
signal.signal(signal.SIGINT, signal_handler)

fn = "ip_log.txt"     #log file name
dirV = directory = str(Path().absolute())
fp = str(dirV) + "/" + fn

try:
        ip1 = str(urlopen('https://api.ipify.org').read().decode("UTF-8"))
        file = open(fp, 'a', encoding="ISO-8859-1")
        dateV = str(time.strftime("%Y-%m-%d %H:%M"))
        data = str(ip1) + " " + dateV + "\n"
        file.write(data)
        file.close
        file.flush()
        print ("\nProgram is Running!\nYour IP adress: " + str(ip1) + " Time: " + str(time.strftime("%Y-%m-%d %H:%M")))
except:
        print ("No internet maybe?")

while True:
        try:
                time.sleep (20)
                ip2 = str(urlopen('https://api.ipify.org').read().decode("UTF-8"))
                dateV = str(time.strftime("%Y-%m-%d %H:%M"))
                print(ip2 + " " + dateV + "     ", end='\r')
                if str(ip1) != str(ip2):
                        ip3 = ip1
                        ip1 = ip2
                        data = 'Ip has changed while script is running, ip changed to ' + str(ip1) + ' Detected when: ' + dateV + '\n'
                        file = open(fp, 'a', encoding="ISO-8859-1")
                        file.write(data)
                        file.close
                        file.flush()
                        print ('\n' + dateV + ' IP CHANGED!\a')
                        print (str(ip3) + ' WAS THE PREVIOUS IP! \n' + str(ip2) + ' IS THE NEW IP\n\n')
        except:
                print ("No internet maybe?")
