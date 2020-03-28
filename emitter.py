from receiver import PublicKey

class Emitter:

    def __init__(self):
        self.__message = 0
        self.encrypted_message = 0

    def write_message(self):
        self.__message = input('create password for the bomb: ') # muss kleiner sein als n
        # evtl. Test?:
        # if (self.__message <= receiver.public_key.n - 1):
        #   print('choose a shorter password.')
        #   write_message()

    def numerize_message(self, message):#fixme
        return int(message)

    def encrypt_message(self, public_key: PublicKey):
        self.encrypted_message = (self.numerize_message(self.__message) ** public_key.get_e()) % public_key.get_n() # e und n sollten doch gerade nicht private sein...
        pass
