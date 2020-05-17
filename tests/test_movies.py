import unittest

from movies.models import Movies
from movies.movies_getaway import MovieGateway
from db import TestDatabase
from sqlalchemy.orm import sessionmaker
import os


class MoviesTestGate(MovieGateway):
    def __init__(self):
        self.db = TestDatabase()
        self.session = sessionmaker(bind=self.db.engine)


class TestCreateMovies(unittest.TestCase):
    def setUp(self):
        self.gateway = MoviesTestGate()
        self.gateway.create_movies_table()

    def tearDown(self):
        os.remove('test_db.db')

    def test_create_movie_with_valid_data(self):
        name = "Thor"
        rating = 4.9
        self.gateway.create(name=name, rating=rating)
        session = self.gateway.db.session()
        movie = session.query(Movies).one()

        self.assertEqual(movie.movie_name, name)
        self.assertEqual(movie.rating, rating)


if __name__ == '__main__':
    unittest.main()
