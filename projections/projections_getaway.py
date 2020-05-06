from db import Database
from db_schema.projections import CREATE_PROJECTION, GET_BY_ID, GET_ALL, DELETE_PROJECTION, UPDATE_DATE, UPDATE_TIME, \
    GET_PROJECTIONS_FOR_MOVIE_BY_DATE, GET_PROJECTIONS_FOR_MOVIE_WITHOUT_DATE
from projections.models import ProjectionModel


class ProjectionGetaway:
    def __init__(self):
        self.model = ProjectionModel

    def create(self, *, movie_type, projection_date, projection_time, movie_id):
        db = Database()
        self.model.validate(movie_type, projection_date, projection_time)
        db.cursor.execute(CREATE_PROJECTION, (movie_type, projection_date, projection_time, movie_id))
        db.connection.commit()
        projection_id = db.cursor.lastrowid
        db.connection.close()

        return projection_id

    def get_by_id(self, *, projection_id):
        db = Database()
        db.cursor.execute(GET_BY_ID, (projection_id))

        projection_db = db.cursor.fetchall()
        projection = self.model.convert(projection_db[0])
        db.connection.commit()
        db.connection.close()

        return projection

    def get_all(self):
        db = Database()
        db.cursor.execute(GET_ALL)

        projection_db = db.cursor.fetchall()
        result = []

        for db_projection in projection_db:
            projection = self.model.convert(db_projection)
            result.append(projection)

        db.connection.commit()
        db.connection.close()

        return result

    def get_projections_for_movie_by_date(self, *, movie_id, date):
        db = Database()
        db.cursor.execute(GET_PROJECTIONS_FOR_MOVIE_BY_DATE, (movie_id, date))

        projection_db = db.cursor.fetchall()
        result = []

        for db_projection in projection_db:
            projection = self.model.convert(db_projection)
            result.append(projection)

        db.connection.commit()
        db.connection.close()

        return result

    def get_projections_for_movie_without_date(self, *, movie_id):
        db = Database()
        db.cursor.execute(GET_PROJECTIONS_FOR_MOVIE_WITHOUT_DATE, (movie_id))

        projection_db = db.cursor.fetchall()
        result = []
        for db_projection in projection_db:
            projection = self.model.convert(db_projection)
            result.append(projection)

        db.connection.commit()
        db.connection.close()

        return result

    def update_date(self, projection_id, new_date):
        db = Database()
        db.cursor.execute(UPDATE_DATE, (new_date, projection_id))
        db.connection.commit()
        db.connection.close()

    def update_time(self, projection_id, new_time):
        db = Database()
        db.cursor.execute(UPDATE_TIME, (new_time, projection_id))
        db.connection.commit()
        db.connection.close()

    def delete_projection(self, projection_id):
        db = Database()
        db.cursor.execute(DELETE_PROJECTION, (projection_id))
        db.connection.commit()
        db.connection.close()
