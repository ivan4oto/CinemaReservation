from movies.controllers import MovieController
from projections.controllers import ProjectionController
from reservations.controllers import ReservationController


class ReservationViews:

    def __init__(self):
        self.controller = ReservationController()
        self.projection_controller = ProjectionController()
        self.movie_controller = MovieController()

    def choose_number_tickets(self):
        tickets = input("\nStep 1 (User): Choose number of tickets> ")
        if tickets == "cancel":
            exit()

        return tickets

    def free_seats_for_movie(self):
        print("\nStep 3 (Projection): Choose a projection")
        projection_id = input("Enter projection id : ")
        if projection_id == "cancel":
            exit()

        numbers = self.controller.take_all_free_seats_for_pr(projection_id=projection_id)
        if numbers == 0:
            raise ValueError('All seats have been taken !')
        print(f'\nThere are {numbers} available seats')

        hall = self.controller.get_all_seats_for_projection(projection_id=projection_id)
        print("Available seats (marked with a dot):")
        for i in hall:
            separator = ' '
            print(separator.join(i))
        return projection_id

    def make_reservation(self, tickets, projection_id, movie_id):
        result = []

        for i in range(int(tickets)):
            seats = self.take_user_input(projection_id)
            while self.controller.check_is_seats_are_free(*seats) or seats in result:
                print(f'This seat is already taken!')
            result.append(seats)

        print("This is your reservation:")
        movie = self.movie_controller.get_movie_by_id(movie_id=movie_id)
        print(f'Movie: {movie.name}  ({movie.rating})')
        projection = self.projection_controller.get_projection_by_id(projection_id)
        print(f"Date and Time: {projection.projection_date} {projection.projection_time}  ({projection.movie_type})")
        print("Seats:")
        for seat in result:
            print(f'({seat[0]}, {seat[1]})')
        end = input("(Confirm - type 'finalize') > ")

        if end == "cancel":
            exit()

        if end == "finalize":
            self.controller.make_reservation(result)
        print("Done")

    def take_user_input(self, projection_id):
        seat = input("Step 4 (Seats): Choose seat 1> : ")
        user_id = input("Enter user 1>")

        return [seat[0], seat[2], user_id, projection_id]
