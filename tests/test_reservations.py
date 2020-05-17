import unittest

from movies.models import Movies
from movies.movies_getaway import MovieGateway
from projections.models import Projection
from projections.projections_getaway import ProjectionGetaway
from reservations.reservations_getaway import ReservationGetaway
from reservations.models import Reservation
from users.users_gateway import UserGateway
from users.models import Users
from db import TestDatabase
from sqlalchemy.orm import sessionmaker
import os


class MoviesTestGate(MovieGateway):
    def __init__(self):
        self.db = TestDatabase()
        self.session = sessionmaker(bind=self.db.engine)


class ProjectionTestGate(ProjectionGetaway):
    def __init__(self):
        self.db = TestDatabase()
        self.session = sessionmaker(bind=self.db.engine)
        self.movie_gateway = MoviesTestGate()
        self.movie_gateway.create_movies_table()


class ReservationTestGate(ReservationGetaway):
    def __init__(self):
        self.db = TestDatabase()
        self.session = sessionmaker(bind=self.db.engine)
        self.projection_gateway = ProjectionTestGate()
        self.projection_gateway.create_projection_table()
        self.movie_gateway = MoviesTestGate()
        self.movie_gateway.create_movies_table()
        self.START_COL = 1
        self.END_COL = 5
        self.START_ROW = 1
        self.END_ROW = 4


class ReservationTest(unittest.TestCase):

    def setUp(self):
        self.gateway = ReservationTestGate()
        self.gateway.create_reservation_table()

    def tearDown(self):
        os.remove('test_db.db')

    def test_create_initial_return_valid_data(self):
        self.gateway.movie_gateway.create(name="Thor", rating=2.2)
        self.gateway.projection_gateway.create(movie_type="3D", projection_date="2020-12-12", projection_time="12:12",
                                               movie_id=1)
        self.gateway.create_initial(projection_id=1)

        session = self.gateway.db.session()
        reservation = session.query(Reservation).all()

        self.assertTrue(len(reservation) == 12)

    def test_get_free_seats_for_projection_return_valid_data(self):
        self.gateway.movie_gateway.create(name="Thor", rating=2.2)
        self.gateway.projection_gateway.create(movie_type="3D", projection_date="2020-12-12", projection_time="12:12",
                                               movie_id=1)
        self.gateway.create_initial(projection_id=1)

        seats = self.gateway.get_free_seats_for_projection(projection_id=1)

        self.assertEqual(seats, 12)


if __name__ == '__main__':
    unittest.main()
