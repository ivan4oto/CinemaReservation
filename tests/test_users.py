import unittest
from users import UserGateway
from users import Users
from db import TestDatabase, session_scope
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

        with session_scope(self.gateway.session()) as session:
            u = session.query(Users).one()
            self.assertEqual(u.username, username)
            self.assertEqual(u.usertype, usertype)         
        
    def test_create_user_raises_error_with_invalid_data(self):
        with self.assertRaises(Exception) as context:
            self.gateway.create(username = 'pesho', password = 'pass!', usertype = 'basic')
        
        self.assertTrue(isinstance(context.exception, ValueError))

    def test_select_user_id(self):
        with session_scope(self.gateway.session()) as session:
            user = Users(username = 'username', hashed_password = 'password', usertype = 'basic')
            session.add(user)
            user_fetch = session.query(Users).one()
            self.assertEqual(1, user_fetch.id)

    def test_select_all_users_returns_all_user_objects(self):
        with session_scope(self.gateway.session()) as session:
            u1 = Users(username = 'pesho', hashed_password = 'peshomesho123', usertype = 'hero')
            u2 = Users(username = 'mesho', hashed_password = 'goshomosho123', usertype = 'gosho')
            session.add_all([u1,u2])

        users = self.gateway.select_all_users()
        users_type = [isinstance(u, Users) for u in users]

        self.assertTrue(users_type)


if __name__ == "__main__":
    unittest.main()