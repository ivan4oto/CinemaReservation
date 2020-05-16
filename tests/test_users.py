import unittest
from users.users_gateway import UserGateway
from users.models import Users
from db import TestDatabase
from sqlalchemy.orm import sessionmaker
import os

class UserTestGate(UserGateway):
    def __init__(self):
        self.db = TestDatabase()
        self.session = sessionmaker(bind = self.db.engine)

class TestDBCreate(unittest.TestCase):
    def setUp(self):
        self.gateway = UserTestGate()
        self.gateway.create_user_table()
    
    def tearDown(self):
        os.remove('test_db.db')
        pass

    def test_create_user_with_valid_data(self):
        username = 'peshomesho'
        usertype = 'superhero'
        self.gateway.create(username = username, password = 'Pasword1!', usertype = usertype)
        session = self.gateway.db.session()
        u = session.query(Users).one()

        self.assertEqual(u.username, username)
        self.assertEqual(u.usertype, usertype)         
        


if __name__ == "__main__":
    unittest.main()