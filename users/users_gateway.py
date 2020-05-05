from db import Database
from .models import UserModel
from db_schema.users import CREATE_USERS, ADD_USER, SELECT_USER_ID, SELECT_USER_HASH_PASSWORD, SELECT_ALL_USERS, get_hashed_password, check_password 


class UserGateway:
    def __init__(self):
        self.model = UserModel
        self.db = Database()

    def create(self, *, username, password):
        self.model.validate(username, password)
        self.db.cursor.execute(ADD_USER, (username, get_hashed_password(password)))
        self.db.cursor.execute(SELECT_USER_ID, (username,))
        user = self.db.cursor.fetchone()
        self.db.connection.commit()
        return user

    def select_user_id(self, *, username):
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
        self.db.cursor.execute(SELECT_USER_HASH_PASSWORD, (username,))
        hashed = self.db.cursor.fetchone()[0]
        #toadd check if hashed is None
        return check_password(password, hashed)

        
