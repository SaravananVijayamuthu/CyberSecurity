#!/bin/python3

import socket

HOST = '127.0.0.1'
PORT = 8080

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #AF_INET is just a IPV4 & SOCK_STREAM is a port

s.connect((HOST, PORT))