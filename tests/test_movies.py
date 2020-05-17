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


class TestMovies(unittest.TestCase):
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

    def test_get_by_id_return_valid_movie(self):
        name = "Thor"
        rating = 4.9

        self.gateway.create(name=name, rating=rating)
        movie_from_db = self.gateway.get_by_id(movie_id=1)

        self.assertEqual(name, movie_from_db.movie_name)
        self.assertEqual(rating, movie_from_db.rating)

    def test_get_all_movies_ordered_by_rating_return_valid_data(self):
        self.gateway.create(name="Thor", rating=7)
        self.gateway.create(name="Batman", rating=4)
        self.gateway.create(name="Supermen", rating=5)

        movies = self.gateway.get_all_movies_ordered_by_rating()

        self.assertEqual("Thor", movies[0].movie_name)
        self.assertEqual("Supermen", movies[1].movie_name)
        self.assertEqual("Batman", movies[2].movie_name)

    def test_update_movie_name_return_valid(self):
        self.gateway.create(name="Thor", rating=7)
        self.gateway.update_movie_name(movie_id=1, new_name="Thor: Ragnarok")

        session = self.gateway.db.session()
        movie = session.query(Movies).one()

        self.assertEqual("Thor: Ragnarok", movie.movie_name)
        self.assertEqual(7, movie.rating)

    def test_update_movie_rating_return_valid(self):
        self.gateway.create(name="Thor", rating=7)
        self.gateway.update_movie_rating(movie_id=1, new_rating=8)

        session = self.gateway.db.session()
        movie = session.query(Movies).one()

        self.assertEqual("Thor", movie.movie_name)
        self.assertEqual(8, movie.rating)

    def test_delete_movie_return_valid(self):
        self.gateway.create(name="Thor", rating=7)
        self.gateway.delete_movie(movie_id=1)

        session = self.gateway.db.session()
        movies = session.query(Movies).all()

        self.assertTrue(len(movies) == 0)





if __name__ == '__main__':
    unittest.main()
