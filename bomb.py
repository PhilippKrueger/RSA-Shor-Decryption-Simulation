class Bomb():
    def __init__(self, time_limit):
        self.time_limit = time_limit
        self.correct_password = 0

    def start(self, password):
        self.correct_password = password
        print("aaah gestartet!!")
        pass

    def stop(self, password, time):
        if password == self.correct_password and time <= self.time_limit:
            print("gestoppt")
        else:
            print("explosion! puff!")