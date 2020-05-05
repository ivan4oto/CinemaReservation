from users.views import UserViews
from movies.views import MovieViews


def welcome():
    print('Welcome to HackCinema!')
    command = int(input('Choose a command:\n  1 - log in\n  2 - sign up\n  Input: '))
    user_views = UserViews()

    if command == 1:
        return user_views.login()

    if command == 2:
        return user_views.signup()

    raise ValueError(f'Unknown command {command}.')

def get_number_of_seats():
    seats = int(input('How many seats you wish to reserve: '))
    movie_views = MovieViews()
    movie_views.get_all_movies()
