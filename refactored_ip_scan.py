#!/usr/bin/env python3

import re
import sys
import threading
import socket
import argparse
import ipaddress


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

def validate_ports(ports_input):
						## Checking Ports for various types of inputs
						## If no ports are specified then choose all 0-65535

	# Regex's to validate input ports
	comma_sep_value_regex = r"^[0-9]+(,[0-9]+)+$"
	range_ports_regex = r"^(\d+)(?:-)(\d+)+$"
	individual_port_regex = r"^(0|[1-9][0-9]{0,3}|[1-5][0-9]{4}|6[0-4][0-9]{3}|65[0-4][0-9]{2}|655[0-2][0-9]|6553[0-5])$"

	if ports_input == None:
		ports = [x for x in range(1,65536)]
							## Matching ports_input for comma separated value (22,25,45,98)
	elif re.fullmatch(pattern = comma_sep_value_regex, string = ports_input):
		value = re.fullmatch(pattern = comma_sep_value_regex,string = ports_input)
		ports = value.group().split(',')
		ports = [int(port) for port in ports]
		if max(ports) > 65535 or min(ports) < 0:
			# Show Error
			sys.exit(1)

							## Matching ports_input for range seperated value ( 22-55 )
	elif re.fullmatch(range_ports_regex, ports_input):
		value = re.fullmatch(range_ports_regex, ports_input)
		start,end = value.group().split('-')
		start,end = int(start),int(end)
		if start < 0 or start > 65535 or end < 0 or end > 65535:
			# Show error
			sys.exit(1)
		ports = [port for port in range(start, end+1)]
	
							## Matching ports_input for indvidual value ( 22 )
	elif re.fullmatch(individual_port_regex, ports_input):
		value = re.fullmatch(individual_port_regex, ports_input)
		ports = int(value.group())
		if ports < 0 or ports > 65535:
			# Show Error if
			sys.exit(1)
	else:
		# Display invalid port format
		print("Invalid Port format")
	
	return ports

def validate_host(hosts_input):
	ipv4_regex = r"^\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|$)){4}\b$"
	cidr_block_regex = r"^([0-9]{1,3}\.){3}[0-9]{1,3}(\/([0-9]|[1-2][0-9]|3[0-2]))+$"
	domain_name_regex = r"((?=[a-z0-9-]{1,63}\.)(xn--)?[a-z0-9]+(-[a-z0-9]+)*\.)+[a-z]{2,63}"

	if re.fullmatch(pattern = ipv4_regex, string = hosts_input):
		value = re.fullmatch(pattern = ipv4_regex, string =hosts_input)
		host = value.group()

	elif re.fullmatch(pattern = cidr_block_regex, string = hosts_input):
		value = re.fullmatch(pattern = cidr_block_regex, string =hosts_input)
		host = value.group()

		net4 = ipaddress.ip_network(host)
		host = []
		for x in net4.hosts():
			host.append(str(x))


	elif re.fullmatch(pattern = domain_name_regex, string = hosts_input):
		value = re.fullmatch(pattern = domain_name_regex, string =hosts_input)
		host = value.group()
	
	else:
		# Display error saying host format is invalid
		print("Invalid host format")
		host = None
	
	return host


# take input 
hosts_input,ports_input = parse_input()


if ports_input:
	ports_input = "".join(ports_input)

host = validate_host(hosts_input)
ports = validate_ports(ports_input)


print(len(host), ports)
# check input with regex
# accordingly run the program 