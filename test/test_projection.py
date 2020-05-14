import unittest
from projections.models import Projection


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.projection_model = Projection

    def test_validate_when_given_invalid_type_return_ex(self):
        with self.assertRaises(ValueError):
            self.projection_model.validate(movie_type="", projection_time="", projection_date="")

    def test_validate_when_given_time_return_ex(self):
        with self.assertRaises(ValueError):
            self.projection_model.validate(movie_type="3D", projection_time="", projection_date="")

    def test_validate_when_given_data_type_return_ex(self):
        with self.assertRaises(ValueError):
            self.projection_model.validate(movie_type="3D", projection_time="2020-02-02",
                                           projection_date="")

    def test_convert_when_is_given_valid_data_return_projection(self):
        projection = self.projection_model.convert([1, "3D", "2020-02-02", "12:12", 1])
        self.assertEqual("3D", projection.movie_type)
        self.assertEqual(1, projection.projections_id)
        self.assertEqual("2020-02-02", projection.projection_date)
        self.assertEqual("12:12", projection.projection_time)
        self.assertEqual(1, projection.movie_id)


if __name__ == '__main__':
    unittest.main()
