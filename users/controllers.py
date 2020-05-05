from .users_gateway import UserGateway
from .models import UserModel

class UserContoller:
    def __init__(self):
        self.users_gateway = UserGateway()
        self.logged_users = []

    def create_user(self, username, password):
        user = self.users_gateway.create(username = username, password=password)
        return user

    def log_user(self, username, password):
        if username in self.logged_users:
            raise ValueError('User already logged in !')
        user_id = self.users_gateway.select_user_id(username = username)
        return self.users_gateway.verify_password(username = username, password = password)