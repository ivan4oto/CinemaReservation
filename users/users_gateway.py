import bcrypt
from db import Database
from .models import Users, Base
from sqlalchemy.orm import sessionmaker

class UserGateway:
    def __init__(self):
        self.db = Database()
        self.session = sessionmaker(bind = self.db.engine)

    def create_user_table(self):
        Base.metadata.create_all(self.db.engine)

    def create(self, *, username, password, usertype):       
        Users.validate(username, password)
        password = self.get_hashed_password(password)

        session = self.db.session()
        user = Users(username = username, hashed_password = password, usertype = usertype)
        session.add(user)
        session.commit()

        return user

    def select_user_id(self, *, username):
        session = self.db.session()
        userid = session.query(Users).filter(Users.username == username).one()        
        session.commit()

        return userid.id

    def select_all_users(self):
        session = self.db.session()
        users = session.query(Users).all()
        session.commit()

        return users

    def verify_password(self, *, username, password):
        session = self.db.session()
        try:
            user = session.query(Users).filter(Users.username == username).one()
            hashed_pass = user.hashed_password
            result = self.check_password(password, hashed_pass)

            if result:
                return user
        except:
            raise ValueError('Wrong password !')
            
    def get_hashed_password(self, password):
        return bcrypt.hashpw(password, bcrypt.gensalt())

    def check_password(self, password, hashed_password):
        return bcrypt.checkpw(password, hashed_password)

    def remove_user(self, *, username):
        session = self.db.session()
        session.query(Users).filter(Users.username == username).delete()
        session.commit()

        return True