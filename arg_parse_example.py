#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser(description = "Network Scanner")
parser.add_argument("host", help = "Hostname/IP/CIDR to be searched for " )
parser.add_argument("-p","--port", required = False, nargs = "*", help = "Specific ports to enumerate for" )

inputs = parser.parse_args()

print( inputs.host, inputs.port )

