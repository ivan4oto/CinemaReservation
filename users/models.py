from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from db import Database



Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key = True)
    username = Column(String)
    hashed_password = Column(String)
    usertype = Column(String)   


# class UserModel:
#     def __init__(self, *, username, id, usertype = ''):
#         self.username = username
#         self.id = id
#         self.type = usertype

#     def __str__(self):
#         return f'username: {self.username}  account_type: {self.type}   id: {self.id}'


    @staticmethod
    def validate(username, password):
        if len(password) < 8:
            raise ValueError('Password is too short !')
        if not any([x.isupper() for x in password]):
            raise ValueError('Password must include one uppercase letter !')
        n = False
        for i in "[@_!#$%^&*()<>?/\|}{~:]":
            if i in password:
                n = True
        if not n:
            raise ValueError('Password must contain atleast one special character !')

        