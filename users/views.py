from .controllers import UserContoller, UserModel, UserGateway

class UserViews:
    def __init__(self):
        self.controller = UserContoller()

    def signup(self):
        username = input('Username: ')
        password = input('Password: ')
        user = self.controller.create_user(username = username, password = password)

        print(f'Successfully created username: {user.username} with id: {user.id}')
        return user

    def login(self):
        username = input('Username: ')
        password = input('Password: ')
        result = self.controller.log_user(username, password)
        print(result)
        if result:
            print("You have successfully logged in !")
            return result
        else:
            raise ValueError('Wrong Password !')
    
