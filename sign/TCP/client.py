
import socket

# Create a socket object
s = socket.socket()

port = 12345
# connect to the s
s.connect(('127.0.0.1', port))

# receive data from the s
print(s.recv(1024).decode('utf_8'))

# close the connection
s.close()


