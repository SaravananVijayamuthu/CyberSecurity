#!/bin/python

import socket
import sys
from datetime import datetime

# Target
if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])  # translates hostname to IPV4
else:
    print("Invalid amount of arguments")

# Pretty
print("-" * 50)
print("Scanning target " + target)
print("Time started " + str(datetime.now()))
print("-" * 50)

# port
try:
    for port in range(50, 85):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        res = s.connect_ex((target, port))
        print("Checking port {}".format(port))
        if res == 0:
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\nExiting Program")
    sys.exit()
except socket.gaierror:
    print("\nCan't resolve host name")
    sys.exit()
except socket.error:
    print("\nCan't connect to the IP")
    sys.exit()
