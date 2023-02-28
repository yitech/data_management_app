from . import CRUD


class Auth(CRUD):
    def __init__(self):
        super(Auth, self).__init__()
        self.db = self.conn['auth']

    def user_exist(self, username):
        res = self.read('auth', 'user', username=username)
        return len(res) > 0

    def create_user(self, username, password):  # Assume username exist
        res = self.create('auth', 'user', username=username, password=password)
        return res

    def verify_user(self, username, password):  # Assume username exist
        res = self.read('auth', 'user', username=username, password=password)
        return len(res) > 0

    def delete_user(self, username):
        res = self.delete('auth', 'user', username=username)
        return res

    def change_password(self, username, old_password, new_password):
        user = self.read('auth', 'user', username=username)
        if user[0]['password'] == old_password:
            res = self.update('auth', 'user', {'password': new_password}, username=username)
            return res
        else:
            return 0  # Invalid password
