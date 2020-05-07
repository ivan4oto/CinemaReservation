from .controllers import UserContoller, UserModel, UserGateway

class UserViews:
    def __init__(self):
        self.controller = UserContoller()

    def signup(self):
        username = input('Username: ')
        if username == 'cancel':
            exit()

        password = input('Password: ')
        user = self.controller.create_user(username = username, password = password)

        print(f'\nSuccessfully created username: {user.username} with id: {user.id}\n')
        return user

    def login(self):
        username = input('\nUsername: ')
        if username == 'cancel':
            exit()

        password = input('Password: ')
        result = self.controller.log_user(username, password)
        if result:
            print("\nYou have successfully logged in !\n")
            return result
        else:
            raise ValueError('\nWrong Password !\n')
    
    def make_admin(self, username):
        if username == 'cancel':
            exit()
        password = 'Administrator1337!'
        user = self.controller.create_user(username = username, password = password)
        user.type = 'admin'

        print(f'\nAdmin type user has been created. Username - {user.username}')
        return user