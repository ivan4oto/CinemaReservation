from db import Database
from db_schema.projections import CREATE_PROJECTION, GET_BY_ID, GET_ALL, DELETE_PROJECTION, UPDATE_DATE, UPDATE_TIME, \
    GET_PROJECTIONS_FOR_MOVIE_BY_DATE, GET_PROJECTIONS_FOR_MOVIE_WITHOUT_DATE
from projections.models import ProjectionModel


class ProjectionGetaway:
    def __init__(self):
        self.model = ProjectionModel
        self.db = Database()

    def create(self, *, movie_type, projection_date, projection_time, movie_id):
        with self.db.connection:
            self.model.validate(movie_type, projection_date, projection_time)
            self.db.cursor.execute(CREATE_PROJECTION, (movie_type, projection_date, projection_time, movie_id))

    def get_by_id(self, *, projection_id):
        with self.db.connection:
            self.db.cursor.execute(GET_BY_ID, (projection_id))

            projection_db = self.db.cursor.fetchall()
            projection = self.model.convert(projection_db)

        return projection

    def get_all(self):
        with self.db.connection:
            self.db.cursor.execute(GET_ALL)

            projection_db = self.db.cursor.fetchall()
            result = []

            for db_projection in projection_db:
                projection = self.model.convert(db_projection)
                result.append(projection)

        return result

    def get_projections_for_movie_by_date(self, *, movie_id, date):
        with self.db.connection:
            self.db.cursor.execute(GET_PROJECTIONS_FOR_MOVIE_BY_DATE, (movie_id, date))

            projection_db = self.db.cursor.fetchall()
            result = []

            for db_projection in projection_db:
                projection = self.model.convert(db_projection)
                result.append(projection)

        return result

    def get_projections_for_movie_without_date(self, *, movie_id):
        with self.db.connection:
            self.db.cursor.execute(GET_PROJECTIONS_FOR_MOVIE_WITHOUT_DATE, (movie_id))

            projection_db = self.db.cursor.fetchall()
            result = []
            for db_projection in projection_db:
                projection = self.model.convert(db_projection)
                result.append(projection)

        return result

    def update_date(self, projection_id, new_date):
        with self.db.connection:
            self.db.cursor.execute(UPDATE_DATE, (new_date, projection_id))

    def update_time(self, projection_id, new_time):
        with self.db.connection:
            self.db.cursor.execute(UPDATE_TIME, (new_time, projection_id))

    def delete_projection(self, projection_id):
        with self.db.connection:
            self.db.cursor.execute(DELETE_PROJECTION, (projection_id))
