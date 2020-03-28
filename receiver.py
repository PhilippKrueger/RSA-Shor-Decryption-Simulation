from sympy import prime, factorint, mod_inverse

class Receiver:
    def __init__(self):
        self.public_key = 0
        self.decrypted_message = 0

    def define_key(self):
        n = input('Enter your last name: ')

        p, q = prime(32), prime(42)
        n = p * q
        print("n: %d, p: %d, q: %d" % (n, p, q))

        # Phi Funktion berechnen
        phi = (p - 1) * (q - 1)
        print("phi: %d" % phi)
        print("Prime Factors of Phi: ", factorint(phi))
        # => Teiler von Phi

        # Teilerfremde Zahl hat keine Teiler von Phi
        e = 11 * 17
        print("e: ", e)

        # Kehrwert von e mod phi
        d = mod_inverse(e, phi)
        print("e%phi: ", e % phi)

        # Public Key: e, n
        print("Public Key e, n: ", e, n)
        # Private Key d
        print("Private Key d: ", d)

        # Verschlüsseln:
        # Nachrichtensind positive ganze Zahlen kleiner n
        def crypt(k, e):
            return k ** e % n

        # Klartext k:
        k = 23709
        print("k: ", k)
        # Geheimtext g:
        g = crypt(k, e)
        print("g: ", g)

        # Entschlüsseln
        k = crypt(g, d)
        print("k: ", k)

        e =

        self.public_key = PublicKey(e, n)
        self.private_key = PrivateKey(e, n)

    def decrypt_message(self, encrypted_message):
        self.decrypted_message = encrypted_message

    def start_bomb(self, bomb):
        bomb.start()



class PublicKey():
    def __init__(self, e, n):
        __e = e
        __n = n

class PrivateKey():
    def __init__(self, d, n):
        __d = d
        __n = n
