#!/usr/bin/python3

from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

message = b'This is my message!\n'
message1= open("msg.txt", "rb").read()
signature= open('signature.bin', 'rb').read()
key = RSA.import_key(open('public.pem').read())
h = SHA256.new(message1)
verifier = pss.new(key)
#     verifier.verify(0x01, signature)

try:
    verifier.verify(h, signature)   
#if it is invalid, the ValueError is raised
    print("The signature is valid.")
except (ValueError, TypeError):
    print("The signature is NOT valid.")

#try:
#     verifier.verify(h, signature)   
     #if 0<1:
     #  raise ValueError        
#except ValueError:
#     print("There is an exception occured")
