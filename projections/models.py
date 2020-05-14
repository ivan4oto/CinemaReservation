from sqlalchemy.orm import relationship

from db import Database
from sqlalchemy import Column, Integer, String, REAL, ForeignKey

from movies.models import Movies


class Projection(Database.base):
    __tablename__ = 'projections'
    id = Column(Integer, primary_key=True, nullable=False)
    movie_type = Column(String)
    projection_date = Column(String)
    projection_time = Column(String)
    movie_id = Column(Integer, ForeignKey(Movies.id))
    projections = relationship(Movies, backref="projections")

    def __str__(self):
        return f'Movie type : {self.movie_type}, projection date {self.projection_date} , projection time {self.projection_time}, id = {self.projections_id}. '

    @staticmethod
    def validate(movie_type, projection_time, projection_date):
        if len(movie_type) < 1:
            raise ValueError("Movie type should be bigger than 1!")
        if len(projection_time) < 8:
            raise ValueError("Projection time should be bigger than 8!")
        if len(projection_date) < 4 or projection_date is None:
            raise ValueError("Projection date should be bigger than 4!")

    @staticmethod
    def convert(projection_db):
        return Projection(projections_id=projection_db[0], movie_type=projection_db[1],
                          projection_date=projection_db[2], projection_time=projection_db[3],
                          movie_id=int(projection_db[4]))
