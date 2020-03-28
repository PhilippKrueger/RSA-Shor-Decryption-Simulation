from receiver import Receiver
from emitter import Emitter
from spy import Spy
from bomb import Bomb


if __name__ == "__main__":
    #initialize
    receiver = Receiver()
    emitter = Emitter()
    spy = Spy()
    bomb = Bomb(time_limit=100)

    #message
    receiver.define_key()
    emitter.write_message()
    emitter.encrypt_message(receiver.public_key)
    receiver.decrypt_message(emitter.encrypted_message)
    receiver.start_bomb(bomb)

    #intervention
    # spy.decrypt_message_shor(emitter.encrypted_message)
    # spy.stop_bomb(bomb)





