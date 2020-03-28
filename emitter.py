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


    def encrypt_message(self, receiver):
        self.__encrypted_message = self.__message ** receiver.public_key.e % receiver.public_key.n # e und n sollten doch gerade nicht private sein...
        pass
