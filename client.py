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
# Defines time intervals corresponding to binary values 1 and 0, respectively.
ONE = 0.1
ZERO = 0.025

# Creats a TCP socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connects the socket to the specified server and port
client.connect((IP, PORT))

# Receives data from the server and decodes it into a string.
data = client.recv(1024).decode('ascii')

"""
    Now we start to get data from server. This loop until the received data indicates the end of the file.
    Inside the loop, it prints the received data, measures the time interval between receiving data, interprets
    the interval as a binary digit (0 or 1) based on predefined time thresholds, and appends it to the 'covert_bi'
    string.
"""
# Initializes an empty string to store the covert binary data.
covert_bin = ""

while (data.strip("\n") != "EOF"):
    # Write the received data to the standard output.
    stdout.write(data)
    # Flushes the standard output buffer to ensure immedaite display of the written data.
    stdout.flush()
    # Record the current time before receiving an other data from the server.
    t0 = time()
    # Receives next data from the server
    data = client.recv(1024).decode('ascii')
    # Record the time after receiving the data.
    t1 = time()
    # Calculate the time interval between receiving the data and the previous data reception time, rounded to three decimal places.
    delta = round(t1 - t0, 3)
    # Compares the time interval with the threshold value 'ONE' to determine if the received bit is 1 or 0.
    if (delta >= ONE):
        # Appends '1' to to the covert binary string if the time interval indicates a binary 1.
        covert_bin += "1"
    else:
        # If the time interval is less than 'ONE', it implies a binary 0.
        covert_bin += "0"
# Closes the socket connection with the server.
client.close()

"""
    This loop iterates through the covert binary string, converting each byte into its correspondig decimal
    value and then into a character using the 'chr()' function.
"""

covert = ""
i=0
while (i<len(covert_bin)):
    # Select one byte of the covert binary string.
    message_byte = covert_bin[i:i+8]
    
    if(len(message_byte) !=8):
        break
    
    # Converts a binary string 'b' into its corresponding decimal integer ''
    char_decimal = int("0b{}".format(message_byte), 2)
    
    try:
        covert += chr(char_decimal)
    except:
        covert += "?"
    
    i += 8

print("\nCovert message: "+ covert)