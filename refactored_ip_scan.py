#!/usr/bin/env python3
##	Check for inputted host weather CIDR or IP
""" For CIDR
		Run ping For ALl possible ip address then
		For all Active ip address run for 65535 ports
"""
""" For IP
	Ping to check if the host is active or not
	IF active then check for port availability
"""


def check_ports(ip):
	print("Checking ports for IP:",ip)
	#  Do Something cheesy here

def check_host(ip):
	print("Checking Host:",ip)
if "__name__" == "__main__":
	# take input 
	# check input with regex
	# accordingly run the program 