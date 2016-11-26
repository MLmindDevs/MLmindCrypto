# Author: Nick Koutroumpinis
# Description : A Simple functional and object oriented RSA implementation

import random
from fractions import gcd

# RSAkeyGenerator is the main function.. it takes as an argument a semiprime number and generates the RSA keys


class RSA(object):

    def RSAkeyGenerator(self, modulo):
        q, p = self.productOfPrimes(modulo)
        f = (int(p) - 1)*(int(q) - 1)
        e = self.ecoeff(f)
        d = self.dGenerate(e, f)
        pubKey = [e, modulo]
        privKey = [d, modulo]
        self.keyLog(privKey, pubKey)
        return pubKey, privKey

    def CheckIfPrime(self, a):  # Simple prime check function
        for i in range(2, a):
            if a % i == 0:
                return False
        return True

    def dGenerate(self, e, F):  # Generate d
        d = 0
        while d * e % F != 1:
            d += 1
        return d

    def productOfPrimes(self, n):  # Find the product of the primes
        primearray = []
        if self.CheckIfPrime(n):
            return 1, n
        for i in range(2, n):
            if self.CheckIfPrime(i):
                primearray.append(i)
        for i in primearray:
            for j in primearray:
                if i * j == n:
                    return i, j
        print "no product of two primes"

    def coprime(self, n, F):  # Find a co-prime needed to generate e
        if gcd(n, F) == 1:
            return True
        else:
            return False

    def ecoeff(self,f):  # Generate e co-efficient
        for i in range(f):
            if self.coprime(i, f) and i != 1:
                return i

    def encrypt(self, txt, pu):  # The encryption function
        encrypted = []
        for number in txt:
            encrypted.append(pow(number, pu[0]) % pu[1])
        return encrypted

    def decrypt(self, txt, pk):  # The decryption function
        decrypted = []
        for number in txt:
            decrypted.append(pow(number, pk[0]) % pk[1])
        return decrypted

    def keyLog(self, priv, pub):  # function to save the keys in the file
        fp = open("Keypair.pair", 'w')
        fp.write(str(priv))
        fp.write(str(pub))

        fp1 = open("PUkey.pub", "w")
        fp1.write(str(pub))

        fp2 = open("PKkey.sec", "w")
        fp2.write(str(priv))
