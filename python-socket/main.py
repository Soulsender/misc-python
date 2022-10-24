#!/bin/python3
import socket

host = "127.0.0.1"
port = 7777

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# socket.AF_INET is IPv4
# socket.SOCK_STREAM is port

s.connect((host, port))