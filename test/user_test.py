import unittest

from users.models import UserModel


class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.reservation_model = UserModel

    def test_validate_when_password_is_too_small_return_ex(self):
        with self.assertRaises(ValueError):
            self.reservation_model.validate(email="mail", password="pass")

    def test_validate_when_password_has_not_uppercase_letter_return_ex(self):
        with self.assertRaises(ValueError):
            self.reservation_model.validate(email="mail", password="passwords")

    def test_validate_when_password_has_not_special_letter_return_ex(self):
        with self.assertRaises(ValueError):
            self.reservation_model.validate(email="mail", password="passwordSSs")


if __name__ == '__main__':
    unittest.main()
