class Spy:
    def __init__(self):
        self.decrypted_message = 0

    def decrypt_message_shor(self, encrypted_message):
        self.decrypted_message = encrypted_message

    def stop_bomb(self, bomb):
        bomb.stop()

