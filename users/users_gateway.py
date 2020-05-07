import bcrypt

from db import Database
from .models import UserModel
from db_schema.users import CREATE_USERS, ADD_USER, SELECT_USER_ID, SELECT_USER_HASH_PASSWORD, SELECT_ALL_USERS


class UserGateway:
    def __init__(self):
        self.model = UserModel
        self.db = Database()

    def create(self, *, username, password):
        with self.db.connection:
            self.model.validate(username, password)
            self.db.cursor.execute(ADD_USER, (username, self.get_hashed_password(password)))
            self.db.cursor.execute(SELECT_USER_ID, (username,))
            user_id = self.db.cursor.fetchone()
            user = self.model(username = username, id = user_id[0])
            return user

    def select_user_id(self, *, username):
        with self.db.connection:
            self.db.cursor.execute(SELECT_USER_ID, (username,))
            user_id = self.db.cursor.fetchone()
            if user_id is None:
                raise ValueError("User not found !")
            else:
                return user_id[0]

    def select_all_users(self):
        raw_users = self.db.cursor.execute(SELECT_ALL_USERS)
        return [self.model(**row) for row in raw_users]

    def verify_password(self, *, username, password):
        with self.db.connection:
            self.db.cursor.execute(SELECT_USER_HASH_PASSWORD, (username,))
            hashed = self.db.cursor.fetchone()
            if hashed == None:
                raise ValueError('User not found !')

            result = self.check_password(password, hashed[0])
            if result:
                self.db.cursor.execute(SELECT_USER_ID, (username,))
                user_id = self.db.cursor.fetchone()
                return self.model(username = username,id = user_id[0] )
            else:
                raise ValueError('Wrong password !')
            
    def get_hashed_password(self, password):
        return bcrypt.hashpw(password, bcrypt.gensalt())

    def check_password(self, password, hashed_password):
        return bcrypt.checkpw(password, hashed_password)