import socket

s = socket.socket()
print('Socket Created')

s.bind(('localhost', 9999))

s.listen(3)
print('Waiting for the connection')

while True:
    c , addr = s.accept()

    name = c.recv(1024).decode()
    print('Connected with : ', addr , name)
    c.send(bytes('Thankyou','utf-8'))
    c.close()
