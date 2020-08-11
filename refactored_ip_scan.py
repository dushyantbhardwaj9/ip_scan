#!/usr/bin/env python3

import re
import threading
import socket

##	Check for inputted host weather CIDR or IP
""" For CIDR
		Run ping For ALl possible ip address then
		For all Active ip address run for 65535 ports
"""

""" For IP
	Ping to check if the host is active or not
	IF active then check for port availability
"""

""" Last option is to do it by hostname
	do a hostbyname process to get IP addr and then do the thing
"""

""" Build a Parser to parse the input through CLI
	Also Build a Help module with a few examples on how to run
"""

""" The Thing To be Done
	1. First get an IP addr or a list of same out of CIDR or by resolving the hostname
 	2. Check if that host is alive
	3. If alive then check for all open ports or look for only specified ports
	4. If not return the error message saying host is down
	5. Make it robust by input sanitization and displaying error messages

	(optional)
	1. Create a json file storing all genral port number and services  or find a way to determine service running 
	2. Differentiate between TCP or UDP ports and how to perform check on them.
"""

""" Make the output messages consize and informative 
	Make it in points and seperate output between two hosts
	Try Printing Ouput Along with scanning to see the results live
"""

def check_ports(ip):
	print("Checking ports for IP:",ip)
	#  Do Something cheesy here

def check_host(ip):
	print("Checking Host:",ip)

def parse_input():
	# take input through parsing
	# sanitize input and return


if "__name__" == "__main__":
	# take input 
	# check input with regex
	# accordingly run the program 