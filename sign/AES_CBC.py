#!/usr/bin/python3

from Crypto.Cipher import AES
from Crypto.Util import Padding
from Crypto.Random import get_random_bytes

key_hex_string = '00112233445566778899AABBCCDDEEFF'
key = bytes.fromhex(key_hex_string)  # byte array
i = get_random_bytes(16)  # initialization vector
data = b'Group Key Agreement for Social Networks'

# Encryption
cipher = AES.new(key, AES.MODE_CBC, i)  # initialize cipher
cipher_text = cipher.encrypt(Padding.pad(data, 16))  # encrypt the plain text with padding, block size = 16 bytes
print("\nCiphertext: {0}\n".format(cipher_text.hex()))

# Decryption
cipher = AES.new(key, AES.MODE_CBC, i)  # initialize cipher for decryption
plain_text = cipher.decrypt(cipher_text)  # decryption with un-padding
print("Plaintext: {0}\n".format(Padding.unpad(plain_text, 16)))