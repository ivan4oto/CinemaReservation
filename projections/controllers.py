from projections.projections_getaway import ProjectionGetaway
from reservations.reservations_getaway import ReservationGetaway


class ProjectionController:

    def __init__(self):
        self.projection_gateway = ProjectionGetaway()
        self.reservation_getaway = ReservationGetaway()

    def create_projection(self, movie_type, projection_date, projection_time, movie_id):
        projection_id = self.projection_gateway.create(movie_type=movie_type, projection_date=projection_date,
                                                       projection_time=projection_time, movie_id=movie_id)

        self.reservation_getaway.create_initial(projection_id=projection_id)

        return True

    def get_projection_by_id(self, projection_id):
        movie = self.projection_gateway.get_by_id(projection_id=projection_id)
        return movie

    def get_projections_for_movie(self, movie_id, date=""):
        if date == "":
            projections = self.projection_gateway.get_projections_for_movie_without_date(movie_id=movie_id)
            return projections
        else:
            projections = self.projection_gateway.get_projections_for_movie_by_date(movie_id=movie_id, date=date)
            return projections

    def get_all(self):
        movies = self.projection_gateway.get_all()
        return movies

    def update_date(self, projection_id, new_date):
        self.projection_gateway.update_date(projection_id=projection_id, new_date=new_date)
        return True

    def update_time(self, projection_id, new_time):
        self.projection_gateway.update_time(projection_id=projection_id, new_time=new_time)
        return True

    def delete(self, projection_id):
        self.projection_gateway.delete_projection(projection_id=projection_id)
        return True
