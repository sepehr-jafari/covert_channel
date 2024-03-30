"""
    This server-side code establiches a covert communication channel with 
    a client. It sends a covert message character by character with specified
    time delays to simulate binary data transmission.
"""
import socket
from time import sleep
# Specifies the connection port and time interval treshold
ONE = 0.1
ZERO = 0.025
PORT = 55555

# Creates TCP socket and bind it to the specified port
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("", PORT))

# Initializes the secret message that we want to send over covert channel
covert = "THIS IS A SECRET TING"
print("Covert message: " + covert)

# Initializes an empty string to store the covert binary data. 
covert_bin = ""
# Iterates through each character in the covert message.  
for i in covert:
    # Convert each charcter to its binary representation, pads it with zeros to ensure it's 8 bits long, and appends to the covert_bin string.
    covert_bin += bin(int(ord(i)))[2:].zfill(8)

print("Covert in binary: " + covert_bin)

# Listens for incoming connections with a backlog of 0.
server.listen(0)

# Accepts an incoming connection from a client and retrieves the client's address.
client, addr = server.accept()

msg = "Some message ...."

print("sending characters with delays: ")

n = 0 
count = 0
"""
    Enter a loop to send characters from delays based on the binary representation of the 
    covert message. Send each character from 'msg' to the client, introducing a delay based
    on whether the corresponding bit in the covert message is 0 or 1.
"""
while(count < len(covert_bin)):
    for i in msg:
        # Sends one character of msg.
        client.send(i.encode())
        # Introducing a delay.
        if(covert_bin[n] == "0"):
            sleep(ZERO)
        else:
            sleep(ONE)
        
        n = (n + 1) % len(covert_bin)
        count += 1
# Sends 'EOF' to indicate the end of the covert message transmission.
client.send("EOF".encode())
# Closes the connection with the client
client.close()