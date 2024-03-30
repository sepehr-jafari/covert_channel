"""
    this code establishes a covert communication channel with a server.
    it measures the time intervals between receving data from the server
    and interprets these intervals as binary data into characters to 
    reveal a covert message.
"""

import socket
from sys import stdout
from time import time

# Specifies the server's IP address and port number for connection.
IP = '127.0.0.1'
PORT = 55555
DEBUG = True
# Defines time intervals corresponding to binary values 1 and 0, respectively.
ONE = 0.1
ZERO = 0.025

# Creats a TCP socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connects the socket to the specified server and port
client.connect((IP, PORT))

