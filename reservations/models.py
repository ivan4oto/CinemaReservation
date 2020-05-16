from sqlalchemy.orm import relationship

from db import Database
from sqlalchemy import Column, Integer, String, REAL, ForeignKey

from projections.models import Projection
from users.models import Users


class Reservation(Database.base):
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True, nullable=False)
    row = Column(Integer)
    col = Column(Integer)
    projection_id = Column(Integer, ForeignKey(Projection.id))
    reservations_projection = relationship(Projection, backref="reservations")
    user_id = Column(Integer, ForeignKey(Users.id), nullable=True)
    reservations_user = relationship(Users, backref="reservations")

    def __str__(self):
        return f'''Reservation : [{self.id}]\n'
                Row : {self.row}, Col : {self.col},
                User_id : {self.user_id}, Projection_id : {self.projection_id}'''

    @staticmethod
    def validate(row, col, user_id, projection_id):
        check = [row, col, user_id, projection_id]

        for i in check:
            if i < 0 or i is not int:
                raise ValueError(f"{i} should be bigger than 0 and should be integer.")

    @staticmethod
    def convert(reservation_db):
        return Reservation(row=reservation_db[1], col=reservation_db[2], user_id=reservation_db[3],
                                projection_id=reservation_db[4], res_id=reservation_db[0])
