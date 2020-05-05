from .controllers import UserContoller


class UserViews:
    def __init__(self):
        self.controller = UserContoller()

    def signup(self):
        username = input('Username: ')
        password = input('Password: ')
        user = self.controller.create_user(username = username, password = password)

        print(f'Successfully created username: {user[1]} with id: {user[0]}')


    def login(self):
        username = input('Username: ')
        password = input('Password: ')
        result = self.controller.log_user(username, password)
        if result:
            print("You have successfully logged in !")
        else:
            raise ValueError('Wrong Password !')
