from movies.views import MovieViews
from projections.views import ProjectionViews
from reservations.views import ReservationViews
from users.views import UserViews


def welcome():
    print('Welcome to HackCinema!')
    command = int(input('Choose a command:\n  1 - log in\n  2 - sign up\n  Input: '))
    user_views = UserViews()
    movie_views = MovieViews()
    projection_views = ProjectionViews()
    reservation_views = ReservationViews()

    if command == 1:
        return user_views.login()

    if command == 2:
        return user_views.signup()

    if command == 10:
        number_of_seats = reservation_views.choose_number_tickets()
        movie_views.get_all_movies()
        movie_id = projection_views.get_projections_for_movie()
        projection_id = reservation_views.free_seats_for_movie()
        reservation_views.make_reservation(number_of_seats, projection_id, movie_id)

    # raise ValueError(f'Unknown command {command}.')
