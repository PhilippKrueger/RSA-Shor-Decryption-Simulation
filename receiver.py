from sympy import prime, factorint, mod_inverse
import numpy as np

class PublicKey:
    def __init__(self, e, n):
        self.__e = e
        self.__n = n

class PrivateKey:
    def __init__(self, d, n):
        self.__d = d
        self.__n = n

class Receiver:
    def __init__(self):
        self.public_key: PublicKey = PublicKey(0,0)
        self.__private_key: PrivateKey = PrivateKey(0,0)
        self.__decrypted_message = 0

    def crypt(self, k, e, n):
        return (k ** e) % n

    def calculate_e(self, phi):
        return np.prod(self.calculate_remaining_primes(self.calculate_forbidden_primes(phi)))


    def calculate_remaining_primes(self, forbidden_primes):
        last_prime = forbidden_primes[-1]
        primes = []
        n=1
        while last_prime<primes[-1]:
            primes.append(prime(n))
            n+=1
        return set(forbidden_primes).symmetric_difference(primes)

    def calculate_forbidden_primes(self, phi):
        prime_dict = factorint(phi)
        forbidden_primes = []
        for a_prime, power in prime_dict.iteritems():
            forbidden_primes.append(a_prime)
        return forbidden_primes


    def define_key(self):
        print("Initialize key with two Prime numbers. Specify n for the n-th prime.")
        n1 = input('n1: ')
        n2 = input('n2: ')
        p, q = prime(n1), prime(n2)
        n = p * q
        print("Key Number n: %d, First prime p: %d, Second prime q: %d" % (n, p, q))
        phi = (p - 1) * (q - 1)
        e = self.calculate_e(phi)

        # Kehrwert von e mod phi
        d = mod_inverse(e, phi)

        # Public Key: e, n
        self.public_key = PublicKey(e, n)
        print("Public Key e, n: ", e, n)
        # Private Key d
        self.public_key = PrivateKey(d, n)
        print("Private Key d: ", d)

        # Verschlüsseln:
        # Nachrichtensind positive ganze Zahlen kleiner n


        # Klartext k:
        k = 23709
        print("k: ", k)
        # Geheimtext g:
        g = self.crypt(k, e, n)
        print("g: ", g)

        # Entschlüsseln
        k = self.crypt(g, d, n)
        print("k: ", k)

    def decrypt_message(self, encrypted_message: object) -> object:
        self.decrypted_message = self.crypt(encrypted_message, self.__private_key.__d, self.__private_key.__n)

    def start_bomb(self, bomb):
        bomb.start()



