
import socket

# create a socket object

port = 12345
# bind to the port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', port))
print("socket binded to %s" % port)
# socket listening
s.listen(1)
print("socket is listening")

# an infinite loop
# while True
# Establish connection with client.
c, addr = s.accept()
print('Got connection from', addr)
c.send(b'Thank you for connecting')

# Close the connection with the client
c.close()
