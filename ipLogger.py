#! /usr/bin/python
# run this command --> 'python ipLogger.py'
# version 1.0

import urllib2
import time
from subprocess import Popen
from random import randint
import signal
import os

clear = "\n" * 100
print clear

def signal_handler(signal, frame):
    print ("\nCan you just close this window?")
signal.signal(signal.SIGINT, signal_handler)

fn = "ip_log.txt"     #log file name
fp = os.path.join(os.path.dirname(__file__), fn)

try:
	ip1 = urllib2.urlopen('https://api.ipify.org').read()
	file = open(fp, 'a')
	file.write(ip1 + ' ' + time.strftime("%Y-%m-%d %H:%M") + '\n')
	file.close
	print ("\nProgram is Running!\n Your IP adress: " + ip1 + "   Time: " + time.strftime("%Y-%m-%d %H:%M"))
except:
	print ("No internet maybe?")

while True:
	try:
		time.sleep (20)
		ip2 = urllib2.urlopen('https://api.ipify.org').read()
		if ip1 != ip2:
			ip3 = ip1
			ip1 = ip2
			data = 'Ip has changed while script is running, ip changed to ' + ip1 + '     Detected when: ' + time.strftime("%Y-%m-%d %H:%M") + '\n'
			file = open(fp, 'a')
			file.write(data)
			file.close
			print (time.strftime("%Y-%m-%d %H:%M") + ' IP CHANGED!\a')
			print (ip3 + ' WAS THE PREVIOUS IP! \n' + ip2 + ' IS THE NEW IP\n\n')
	except:
		print ("No internet maybe?")
		continue
