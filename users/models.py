from sqlalchemy import Column, Integer, String
from db import Database



class Users(Database.base):
    __tablename__ = 'Users'
    id = Column(Integer, primary_key = True)
    username = Column(String)
    hashed_password = Column(String)
    usertype = Column(String)   

    def __str__(self):
        return "Username: {} id: {} acc_type: {}".format(self.username, self.id, self.usertype)

    def __repr__(self):
        return self.__str__()


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

        