from sympy import prime, factorint, mod_inverse
import numpy as np

class PublicKey:
    def __init__(self, e, n):
        self.__e = e
        self.__n = n

    def get_e(self):
        return self.__e

    def get_n(self):
        return self.__n

class PrivateKey:
    def __init__(self, d, n):
        self.__d = d
        self.__n = n

    def get_d(self):
        return self.__d

    def get_n(self):
        return self.__n

class Receiver:
    def __init__(self):
        self.public_key: PublicKey = 0
        self.__private_key: PrivateKey = 0
        self.__decrypted_message = 0

    def crypt(self, k, e, n):
        print(k,"**", e,"mod", n)
        print(type(pow(k, e) % n), pow(k, e) % n)
        return pow(k, e) % n

    def calculate_e(self, phi):
        return np.prod(self.calculate_remaining_primes(self.calculate_forbidden_primes(phi)))


    def calculate_remaining_primes(self, forbidden_primes):
        last_prime = forbidden_primes[-1]
        print("forbidden:",forbidden_primes)
        primes = [prime(1)]
        n=2
        while primes[-1]<=last_prime:
            primes.append(prime(n))
            n+=1
        print("all:",primes)
        print("allowed:",list(set(primes)-set(forbidden_primes)))
        return list(set(primes)-set(forbidden_primes))[0]

    def calculate_forbidden_primes(self, phi):
        prime_dict = factorint(phi)
        print("Prime Dict:", prime_dict)
        forbidden_primes = []
        for a_prime in prime_dict.keys():
            forbidden_primes.append(a_prime)
        return forbidden_primes

    def egcd(self, a, b):
        if a == 0:
            return (b, 0, 1)
        g, y, x = self.egcd(b % a, a)
        return (g, x - (b // a) * y, y)

    def modinv(self, a, m):
        g, x, y = self.egcd(a, m)
        if g != 1:
            raise Exception('No modular inverse')
        return x % m

    def define_key(self):
        print("Initialize key with two Prime numbers. Specify n for the n-th prime.")
        n1 = input('n1: ')
        n2 = input('n2: ')
        p, q = prime(int(n1)), prime(int(n2))
        n = p * q
        print("Key Number n: %d, First prime p: %d, Second prime q: %d" % (n, p, q))
        phi = (p - 1) * (q - 1)
        print("Phi:", phi)
        e = self.calculate_e(phi)

        # Kehrwert von e mod phi
        print("Performing mod inverse with e, phi", e, phi)
        d = self.modinv(e, phi)

        # Public Key: e, n
        self.public_key = PublicKey(e, n)
        print("Public Key e, n: ", e, n)
        # Private Key d
        self.__private_key = PrivateKey(d, n)
        print("Private Key d, n: ", d, n)

        # Verschlüsseln:
        # Nachrichtensind positive ganze Zahlen kleiner n


        # Klartext k:
        k = 4
        print("k: ", k)
        # Geheimtext g:
        g = self.crypt(k, e, n)
        print("g: ", g)

        # Entschlüsseln
        k = self.crypt(g, d, n)
        print("k: ", k)

    def decrypt_message(self, encrypted_message):
        self.__decrypted_message = self.crypt(encrypted_message, self.__private_key.get_d(), self.__private_key.get_n())

    def start_bomb(self, bomb):
        bomb.start(self.__decrypted_message)



