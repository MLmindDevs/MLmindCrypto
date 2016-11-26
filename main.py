# Author: Nick Koutroumpinis
# Description: Easy AES, RSA encrypt, decrypt implementation.

from AES import *
from RSA import *






##############################################  RSA  ###############################################


cleartext = "RSA Encryption"
raw_bytes = map(ord, cleartext)

rsa = RSA()
k = rsa.RSAkeyGenerator(8327)  # returns a tuple with the keys, takes as input a semi-prime number
PU = k[0]
PK = k[1]
print "cleartext: " + cleartext
encrypted = rsa.encrypt(raw_bytes, PU)
print "cleartext in raw_bytes: " + str(raw_bytes)
print "encrypted : " + str(encrypted)
decrypted = rsa.decrypt(encrypted, PK)
print "decrypted: " + str(decrypted)
decr_clear = map(chr, decrypted)
print "decrypted clear in a list: " + str(decr_clear)

###################################################################################################

