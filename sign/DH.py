#!/usr/bin/python3

import pyDH

d1 = pyDH.DiffieHellman()  # generate private key x for d1
d2 = pyDH.DiffieHellman()  # generate private key y for d2
d1_pubkey = d1.gen_public_key()  # g^x
d2_pubkey = d2.gen_public_key()  # g^y
d1_sharedkey = d1.gen_shared_key(d2_pubkey)  # H(g^xy)
d2_sharedkey = d2.gen_shared_key(d1_pubkey)  # H(g^xy)

# Testing
print(d1_sharedkey == d2_sharedkey)  # test if they are equal

share_key12 = pow(d2_pubkey, d1.get_private_key(), d1.p)  # g^xy
share_key21 = pow(d1_pubkey, d2.get_private_key(), d2.p)  # g^yx

print(share_key12 == share_key21)   # test if they are equal
