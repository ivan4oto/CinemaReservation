from sqlalchemy import Column, Integer, String, REAL
from sqlalchemy.ext.declarative import declarative_base
from db import Database

class Movies(Database.base):
    __tablename__ = 'Movies'
    id = Column(Integer, primary_key = True, nullable = False)
    movie_name = Column(String)
    rating = Column(REAL, nullable = False)

    def __str__(self):
        return "Movie name: {}, with rating: {}, and ID: {}".format(self.movie_name, self.rating, self.id)

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def validate(name, rating):
        if name is None:
            raise ValueError("Name should be not None!")
        if len(name) == 1:
            raise ValueError("Name should be bigger than 1!")
        if rating < 0:
            raise ValueError("Rating should be bigger than zero!")

    @staticmethod
    def convert(movie_db):
        return Movies(id=movie_db[0], movie_name=movie_db[1], rating=movie_db[2])
