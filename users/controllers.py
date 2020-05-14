from .users_gateway import UserGateway

class UserContoller:
    def __init__(self):
        self.users_gateway = UserGateway()
        self.logged_users = []

    def create_user(self, username, password, usertype):
        user = self.users_gateway.create(username = username, password=password, usertype = usertype)
        return user

    def log_user(self, username, password):
        result =  self.users_gateway.verify_password(username = username, password = password)
        return result

    def remove_user(self, username):
        result = self.users_gateway.remove_user(username = username)
        return result

    def get_users(self):
        return self.users_gateway.select_all_users()