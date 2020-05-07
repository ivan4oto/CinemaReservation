import unittest

from reservations.models import ReservationModel


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.reservation_model = ReservationModel

    def test_validate_when_is_given_negative_col_return_ex(self):
        with self.assertRaises(ValueError):
            self.reservation_model.validate(row=1, col=-1, projection_id=1, user_id=1)

    def test_validate_when_is_given_double_col_return_ex(self):
        with self.assertRaises(ValueError):
            self.reservation_model.validate(row=1, col=1.1, projection_id=1, user_id=1)

    def test_validate_when_is_given_negative_row_return_ex(self):
        with self.assertRaises(ValueError):
            self.reservation_model.validate(row=-1, col=1, projection_id=1, user_id=1)

    def test_validate_when_is_given_double_row_return_ex(self):
        with self.assertRaises(ValueError):
            self.reservation_model.validate(row=1.1, col=1, projection_id=1, user_id=1)

    def test_validate_when_is_given_negative_projection_id_return_ex(self):
        with self.assertRaises(ValueError):
            self.reservation_model.validate(row=1, col=1, projection_id=-1, user_id=1)

    def test_validate_when_is_given_double_projection_id_return_ex(self):
        with self.assertRaises(ValueError):
            self.reservation_model.validate(row=1, col=1, projection_id=1.1, user_id=1)

    def test_validate_when_is_given_negative_user_id_return_ex(self):
        with self.assertRaises(ValueError):
            self.reservation_model.validate(row=1, col=1, projection_id=1, user_id=-1)

    def test_validate_when_is_given_double_user_id_return_ex(self):
        with self.assertRaises(ValueError):
            self.reservation_model.validate(row=1, col=1, projection_id=1, user_id=1.1)

    def test_convert_when_is_given_valid_data_return_reservation(self):
        reservation = self.reservation_model.convert([1, 2, 3, 4, 5])

        self.assertEqual(1, reservation.res_id)
        self.assertEqual(2, reservation.row)
        self.assertEqual(3, reservation.col)
        self.assertEqual(5, reservation.projection_id)
        self.assertEqual(4, reservation.user_id)


if __name__ == '__main__':
    unittest.main()
