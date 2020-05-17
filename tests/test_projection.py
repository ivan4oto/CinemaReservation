import unittest

from movies.models import Movies
from movies.movies_getaway import MovieGateway
from projections.models import Projection
from projections.projections_getaway import ProjectionGetaway
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


class ProjectionTest(unittest.TestCase):

    def setUp(self):
        self.gateway = ProjectionTestGate()
        self.gateway.create_projection_table()

    def tearDown(self):
        os.remove('test_db.db')

    def test_create_projection_with_valid_data(self):
        self.gateway.movie_gateway.create(name="Thor", rating=2.2)
        self.gateway.create(movie_type="3D", projection_date="2020-12-12", projection_time="12:12", movie_id=1)
        session = self.gateway.db.session()

        movie = session.query(Movies).first()

        self.assertTrue(len(movie.projections) == 1)

    def test_get_by_id_return_valid_projection(self):
        self.gateway.movie_gateway.create(name="Thor", rating=2.2)
        self.gateway.create(movie_type="3D", projection_date="2020-12-12", projection_time="12:12", movie_id=1)

        projection = self.gateway.get_by_id(projection_id=1)

        self.assertEqual("3D", projection.movie_type)
        self.assertEqual("2020-12-12", projection.projection_date)
        self.assertEqual("12:12", projection.projection_time)

    def test_get_all_return_valid_data(self):
        self.gateway.movie_gateway.create(name="Thor", rating=2.2)
        self.gateway.create(movie_type="3D", projection_date="2020-12-12", projection_time="12:12", movie_id=1)
        self.gateway.movie_gateway.create(name="Batman", rating=5.2)
        self.gateway.create(movie_type="3D", projection_date="2020-12-12", projection_time="11:11", movie_id=2)

        projections = self.gateway.get_all()

        self.assertTrue(len(projections) == 2)

    def test_get_projections_for_movie_by_date_return_valid_projection(self):
        self.gateway.movie_gateway.create(name="Thor", rating=2.2)
        self.gateway.create(movie_type="3D", projection_date="2020-12-12", projection_time="12:12", movie_id=1)

        projections = self.gateway.get_projections_for_movie_by_date(movie_id=1, date="2020-12-12")

        self.assertTrue(len(projections) == 1)

    def test_get_projections_for_movie_without_date_return_valid_projections(self):
        self.gateway.movie_gateway.create(name="Thor", rating=2.2)
        self.gateway.create(movie_type="3D", projection_date="2020-12-12", projection_time="12:12", movie_id=1)
        self.gateway.create(movie_type="3D", projection_date="2020-12-12", projection_time="23:12", movie_id=1)

        projections = self.gateway.get_projections_for_movie_without_date(movie_id=1)

        self.assertTrue(len(projections) == 2)

    def test_update_date_return_valid_data(self):
        self.gateway.movie_gateway.create(name="Thor", rating=2.2)
        self.gateway.create(movie_type="3D", projection_date="2020-12-12", projection_time="12:12", movie_id=1)

        self.gateway.update_date(projection_id=1, new_date="2020-13-12")

        session = self.gateway.db.session()
        projection = session.query(Projection).first()

        self.assertEqual("2020-13-12", projection.projection_date)

    def test_update_time_return_valid_data(self):
        self.gateway.movie_gateway.create(name="Thor", rating=2.2)
        self.gateway.create(movie_type="3D", projection_date="2020-12-12", projection_time="12:12", movie_id=1)

        self.gateway.update_time(projection_id=1, new_time="13:13")

        session = self.gateway.db.session()
        projection = session.query(Projection).first()

        self.assertEqual("13:13", projection.projection_time)

    def test_delete_return_valid_data(self):
        self.gateway.movie_gateway.create(name="Thor", rating=2.2)
        self.gateway.create(movie_type="3D", projection_date="2020-12-12", projection_time="12:12", movie_id=1)

        movie_before_delete = self.gateway.movie_gateway.get_by_id(movie_id=1)
        self.assertTrue(len(movie_before_delete.projections) == 1)
        self.gateway.delete_projection(projection_id=1)

        movie_after_delete = self.gateway.movie_gateway.get_by_id(movie_id=1)
        self.assertTrue(len(movie_after_delete.projections) == 0)


if __name__ == '__main__':
    unittest.main()
