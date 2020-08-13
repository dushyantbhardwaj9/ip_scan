#!/usr/bin/env python3

import re
import sys
import threading
import socket
import argparse

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

# Make it all in Socket Programming like for ICMP packets for HOSTS and PORT scanning



""" Regex to check for IP	
	ipv4_regex = "^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$"
	cidr_block_regex = "^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))?$"
	domain_name_regex = "((?=[a-z0-9-]{1,63}\.)(xn--)?[a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,63}"
"""	

""" Regex for port number
	comma_sep_value_regex = "[0-9]+(,[0-9]+)+$"
	range_ports_regex = "(\d+)(?:-(\d+))?$"
	single_port_regex = "^(0|[1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$"
"""

def check_ports(ip):
	print("Checking ports for IP:",ip)
	#  Do Something cheesy here

def check_host(ip):
	print("Checking Host:",ip)

def parse_input():
	# take input through parsing
	# sanitize input and return
	parser = argparse.ArgumentParser(description = "Network Scanner")
	parser.add_argument("host", help = "Hostname/IP/CIDR " )
	parser.add_argument("-p","--port", nargs = "*", help = "Specific ports to enumerate for" )

	inputs = parser.parse_args()
	if inputs.port:
		return (inputs.host, inputs.port)
	else:
		return (inputs.host,None)


print("Program Begin")
# take input 
hosts_input,ports_input = parse_input()
# print(type(hosts_input), type(ports_input))

ports_input = "".join(ports_input)
# Regex's to validate input
comma_sep_value_regex = "^[0-9]+(,[0-9]+)+$"
range_ports_regex = "^(\d+)(?:-)(\d+)+$"
individual_port_regex = "^(0|[1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$"

if ports_input == None:
	ports = [x for x in range(1,65536)]
elif re.fullmatch(pattern = comma_sep_value_regex, string = ports_input):
	value = re.fullmatch(pattern = comma_sep_value_regex,string = ports_input)
	ports = value.group().split(',')
	if max(ports) > 65535 or min(ports):
		# Show Error
		sys.exit(1)

elif re.fullmatch(range_ports_regex, ports_input):
	value = re.fullmatch(range_ports_regex, ports_input)
	start,end = value.group().split('-')
	start,end = int(start),int(end)
	if start < 0 or start > 65535 or end < 0 or end > 65535:
		# Show error
		sys.exit()
	ports = [port for port in range(start, end+1)]

elif re.fullmatch(individual_port_regex, ports_input):
	value = re.fullmatch(individual_port_regex, ports_input)
	ports = [int(value.group())]

if ports == None:
	ports = [x for x in range(1,65536)]

print(hosts_input, ports)
# check input with regex
# accordingly run the program 