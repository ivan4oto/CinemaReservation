from .controllers import UserContoller, UserModel, UserGateway

class UserViews:
    def __init__(self):
        self.controller = UserContoller()

    def signup(self):
        username = input('Username: ')
        if username == 'cancel':
            exit()

        password = input('Password: ')
        user = self.controller.create_user(username = username, password = password, usertype = 'basic')

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
        user = self.controller.create_user(username = username, password = password, usertype = 'admin')
        print(f'\nAdmin type user has been created. Username - {user.username}')
        print(user.type)
        return user

    def remove_user(self):
        username = input('Username: ')
        if username == "cancel":
            exit()
        result = self.controller.remove_user(username)
        if result:
            print(f'User {username} has been successfully deleted')

    def show_all_users(self):
        users = self.controller.get_users()
        for u in users:
            print(u)