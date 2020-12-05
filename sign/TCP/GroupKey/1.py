import random
import socket


print("this is user 1")

# random number for local group key
s_1 = random.randint(1, 256)

port = 8001
# bind to the port

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', port))
print("socket binded to %s" % port)
# socket listening
s.listen(1)
print("socket is listening")

c, addr = s.accept()
print('Got connection from', addr)

c.send(str(s_1).encode('utf8'))