from db import Database
from db_schema.movies import CREATE_MOVIE, GET_BY_ID, GET_ALL_MOVIES_ORDERED_BY_RATING, UPDATE_MOVIE_NAME, \
    UPDATE_MOVIE_RATING, DELETE_MOVIE
from movies.models import MovieModel


class MovieGateway:
    def __init__(self):
        self.model = MovieModel
        self.db = Database()

    def create(self, *, name, rating):
        self.model.validate(name, rating)
        self.db.cursor.execute(CREATE_MOVIE, (name, rating))
        self.db.connection.commit()
        self.db.connection.close()

    def get_by_id(self, *, movie_id):
        self.db.cursor.execute(GET_BY_ID, (movie_id))

        movie_db = self.db.cursor.fetchall()
        movie = self.model.convert(movie_db)
        self.db.connection.commit()
        self.db.connection.close()

        return movie

    def get_all_movies_ordered_by_rating(self):
        self.db.cursor.execute(GET_ALL_MOVIES_ORDERED_BY_RATING)

        movies_db = self.db.cursor.fetchall()
        result = []
        for db_movie in movies_db:
            movie = self.model.convert(db_movie)
            result.append(movie)

        self.db.connection.commit()
        self.db.connection.close()

        return result

    def update_movie_name(self, movie_id, new_name):
        self.db.cursor.execute(UPDATE_MOVIE_NAME, (new_name, movie_id))
        self.db.connection.commit()
        self.db.connection.close()

    def update_movie_rating(self, movie_id, new_rating):
        self.db.cursor.execute(UPDATE_MOVIE_RATING, (new_rating, movie_id))
        self.db.connection.commit()
        self.db.connection.close()

    def delete_movie(self, movie_id):
        self.db.cursor.execute(DELETE_MOVIE, (movie_id))
        self.db.connection.commit()
        self.db.connection.close()
