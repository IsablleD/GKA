import socket
import random

print("this is user 1")
s_2 = random.randint(1, 256)

# Create a socket object
s1 = socket.socket()

port = 8001
# connect to the s
s1.connect(('127.0.0.1', port))

# receive data from the s
msg = s1.recv(1024).decode('utf_8')
print(msg)

# temp sum after user1
temp = int(msg)

# close the connection
s1.close()

s2 = socket.socket()

port = 8003
# connect to the s
s2.connect(('127.0.0.1', port))

# receive data from the s
msg2 = s2.recv(1024).decode('utf_8')
print(msg2)

# temp sum after user 3
temp += int(msg2)

# close the connection
s2.close()

temp += s_2

port = 8002
# bind to the port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', port))
print("socket binded to %s" % port)
# socket listening
s.listen(1)
print("socket is listening")

c, addr = s.accept()
print('Got connection from', addr)

c.send(str(temp).encode('utf8'))