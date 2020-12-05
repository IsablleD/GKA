import random
import socket

print("this is user 4")
s_4 = random.randint(1, 256)

# Create a socket object
s1 = socket.socket()

port = 8002
# connect to the s
s1.connect(('127.0.0.1', port))

# receive data from the s
msg = s1.recv(1024).decode('utf_8')
print(msg)

# temp sum after user1
temp = int(msg) + s_4

print("Final group key is:", temp)

# close the connection
s1.close()

# save the final group key
with open('FinalG.txt', 'w') as f:
    f.write('%d' % temp)

