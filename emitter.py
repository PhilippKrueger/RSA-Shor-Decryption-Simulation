from sympy import prime, factorint, mod_inverse

class Emitter:
    def __init__(self):
        self.__message = 0
        self.encrypted_message = 0

    def write_message(self):
        self.__message = 1
        pass

    def encrypt_message(self, receiver):
        self.__encrypted_message = self.__message, receiver.public_key.__e, receiver.public_key.__n
        pass
