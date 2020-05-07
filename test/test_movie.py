import unittest

from movies.models import MovieModel


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.movie_validation = MovieModel

    def test_validation_when_given_invalid_name_return_ex(self):
        self.assertRaises(ValueError, self.movie_validation.validate(name="", rating=23.23))

    def test_validation_when_given_negative_rating_return_ex(self):
        self.assertRaises(ValueError, self.movie_validation.validate(name="Zoro", rating=0))

    def test_convert_when_given_correct_args_return_obj_movie(self):
        movie = self.movie_validation.convert(movie_db=(1, "Zoro", 23.32))

        self.assertEqual(1, movie.movie_id)
        self.assertEqual("Zoro", movie.name)
        self.assertEqual(23.32, movie.rating)


if __name__ == '__main__':
    unittest.main()
