from db import Database

from movies.models import Movies
from sqlalchemy.orm import sessionmaker


class MovieGateway:
    def __init__(self):
        self.db = Database()
        self.session = sessionmaker(bind=self.db.engine)

    def create_movies_table(self):
        self.db.base.metadata.create_all(self.db.engine)

    def create(self, *, name, rating):
        session = self.db.session()
        Movies.validate(name, rating)
        movie = Movies(movie_name=name, rating=rating)
        session.add(movie)
        session.commit()

    def get_by_id(self, *, movie_id):
        session = self.db.session()
        movie = session.query(Movies). \
            filter(Movies.id == movie_id). \
            one()

        session.commit()
        return movie

    def get_all_movies_ordered_by_rating(self):
        session = self.db.session()
        # s = select([Movies]).\
        #     order_by(Movies.rating)

        movies_list = session.query(Movies).order_by(Movies.rating.desc())
        return movies_list

    def update_movie_name(self, movie_id, new_name):
        session = self.db.session()
        movie = session.query(Movies).filter(Movies.id == movie_id).one()
        movie.movie_name = new_name
        session.commit()


    def update_movie_rating(self, movie_id, new_rating):
        session = self.db.session()
        movie = session.query(Movies).filter(Movies.id == movie_id).one()
        movie.rating = new_rating
        session.commit()

    def delete_movie(self, movie_id):
        session = self.db.session()
        session.query(Movies).filter(Movies.id == movie_id).delete()
        session.commit()
