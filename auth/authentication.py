from mongodb.auth import Auth


class Authentication:
    def __init__(self):
        self.auth = Auth()
        self.username = 'guest'

    def get_user(self):
        return self.username

    def login(self, username, password):
        if self.auth.verify_user(username, password):
            self.username = username

    def logout(self):
        self.username = 'guest'


