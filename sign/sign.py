#!/usr/bin/python3

from Crypto.Signature import pss
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA

# test message
message=b'This is my message!\n'
message1=open("msg.txt").read()
key_pem=open("private.pem").read()
key=RSA.import_key(key_pem.encode(), passphrase="dees")
h=SHA256.new(message1.encode())
signer=pss.new(key)
sig=signer.sign(h)
open("signature.bin", "wb").write(sig)


