"""
TCP Socket Programming - Server
Author: Amey Thakur
GitHub: https://github.com/Amey-Thakur
Repository: https://github.com/Amey-Thakur/COMPUTER-NETWORK-AND-COMPUTER-NETWORK-LAB

Description:
This program implements a simple TCP server using Python's socket library.
The server listens for incoming client connections, receives a name from the client,
and sends back an acknowledgment message.

Usage:
1. Run this server program first
2. Run the client program to connect to this server
3. Server will display connected client information
"""

import socket

# Create a TCP socket object
# AF_INET: IPv4 addressing
# SOCK_STREAM: TCP protocol
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket Created Successfully')

# Bind the socket to localhost on port 9999
# localhost (127.0.0.1) means the server runs on the same machine
# Port 9999 is the communication endpoint
s.bind(('localhost', 9999))

# Listen for incoming connections
# Parameter 3 means maximum 3 clients can wait in queue
s.listen(3)
print('Server is listening on port 9999...')
print('Waiting for client connections...')

# Server runs indefinitely to handle multiple clients
while True:
    # Accept incoming connection
    # c: client socket object for communication
    # addr: client's address (IP and port)
    c, addr = s.accept()
    
    # Receive data from client (maximum 1024 bytes)
    # decode() converts bytes to string
    name = c.recv(1024).decode()
    
    # Display connection information
    print(f'Connected with: {addr} | Client Name: {name}')
    
    # Send acknowledgment message to client
    # bytes() converts string to bytes for transmission
    c.send(bytes('Thank you for connecting!', 'utf-8'))
    
    # Close the client connection
    c.close()
    print(f'Connection with {name} closed\n')
