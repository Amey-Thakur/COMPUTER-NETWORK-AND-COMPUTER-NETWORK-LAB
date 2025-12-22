"""
TCP Socket Programming - Client
Author: Amey Thakur
GitHub: https://github.com/Amey-Thakur
Repository: https://github.com/Amey-Thakur/COMPUTER-NETWORK-AND-COMPUTER-NETWORK-LAB

Description:
This program implements a simple TCP client using Python's socket library.
The client connects to a server, sends the user's name, and receives an
acknowledgment message from the server.

Usage:
1. Ensure the server program is running first
2. Run this client program
3. Enter your name when prompted
4. Client will receive and display the server's response
"""

import socket

# Create a TCP socket object
# AF_INET: IPv4 addressing
# SOCK_STREAM: TCP protocol
c = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Client socket created')

# Connect to the server
# Server is running on localhost (same machine) at port 9999
c.connect(('localhost', 9999))
print('Connected to server at localhost:9999')

# Get user input
name = input("Enter your Name: ")

# Send name to server
# bytes() converts string to bytes for transmission over network
c.send(bytes(name, 'utf-8'))
print(f'Sent name "{name}" to server')

# Receive response from server (maximum 1024 bytes)
# decode() converts received bytes back to string
response = c.recv(1024).decode()
print(f'Server response: {response}')

# Close the connection
c.close()
print('Connection closed')
