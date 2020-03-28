from sympy import prime, factorint, mod_inverse

class Receiver:
    def __init__(self):
        self.public_key = 0
        self.decrypted_message = 0

    def define_key(self):
        self.public_key = PublicKey()
        self.private_key = PrivateKey()

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
