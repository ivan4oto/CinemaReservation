from users.views import UserViews
from movies.views import MovieViews


def login():
    print('Welcome to HackCinema!')
    command = int(input('Choose a command:\n  1 - log in\n  2 - sign up\n  Input: '))
    user_views = UserViews()

    if command == 1:
        return user_views.login()

    if command == 2:
        return user_views.signup()

    raise ValueError(f'Unknown command {command}.')

def get_seats():
    pass
    
    