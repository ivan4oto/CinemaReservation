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

        print(f'Successfully created username: {user.username} with id: {user.id}')
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
    
