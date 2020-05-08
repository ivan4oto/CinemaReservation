from movies.views import MovieViews
from projections.views import ProjectionViews
from reservations.views import ReservationViews
from users.views import UserViews, UserModel
from movies.views import MovieViews


def login():
    print('Welcome to HackCinema!\n')
    command = int(input('Choose a command:\n  1 - log in\n  2 - sign up\n\n  Input: '))
    user_views = UserViews()
    if command == 1:
        return user_views.login()

    if command == 2:
        return user_views.signup()
    
    if command == 'cancel':
        exit()

    else:
        raise ValueError(f'Unknown command {command}.')



def make_choice():
    movie_views = MovieViews()
    projection_views = ProjectionViews()
    reservation_views = ReservationViews()

    number_of_seats = reservation_views.choose_number_tickets()
    print("\nWe're currently streaming the following movies:\n")
    movie_views.get_all_movies()
    movie_id = projection_views.get_projections_for_movie()
    projection_id = reservation_views.free_seats_for_movie()
    
    reservation_views.make_reservation(number_of_seats, projection_id, movie_id)


def admin_panel():
    user_views = UserViews()
    movie_views = MovieViews()
    projection_views = ProjectionViews()

    print('\n\nWelcome to the ADMIN Control Panel\nYou have the following options:\n\n')
    print('''
    1. Create a movie
    2. Update an existing movie
    3. Delete an existing movie
    
    4. Create projection
    5. Update projection
    6. Delete projection    
    
    7. Delete user
    8. Display all users

    ''')

    command = input('\nEnter a command: ')

    if command == '1':
        movie_views.create_movie()
        admin_panel()

    if command == '3':
        movie_views.delete_movie()
        admin_panel()

    if command == '6':
        projection_views.delete_movie()
        admin_panel()

    if command == '7':
        user_views.remove_user()
        admin_panel()

    if command == '8':
        user_views.show_all_users()
        admin_panel()
    
    if command == 'cancel':
        exit()
    

