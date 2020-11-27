#!/usr/bin/python3

from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# test message
message = b'This is my message!\n'
message1= open("msg.txt", "rb").read()
signature= open('signature.bin', 'rb').read()
key = RSA.import_key(open('public.pem').read())
h = SHA256.new(message1)  # hash the message to make it shorter
verifier = pss.new(key)

try:
    verifier.verify(h, signature)
    print("The signature is valid.")  # signature correct
except (ValueError, TypeError):
    print("The signature is NOT valid.")  # signature wrong


