from sqlalchemy.orm import sessionmaker

from db import Database
from movies.movies_getaway import MovieGateway
from projections.models import Projection


class ProjectionGetaway:
    def __init__(self):
        self.db = Database()
        self.session = sessionmaker(bind=self.db.engine)
        self.movie_gateway = MovieGateway()

    def create_projection_table(self):
        self.db.base.metadata.create_all(self.db.engine)

    def create(self, *, movie_type, projection_date, projection_time, movie_id):

        session = self.db.session()
        Projection.validate(movie_type, projection_date, projection_time)
        movie = self.movie_gateway.get_by_id(movie_id=movie_id)
        p = Projection(movie_type=movie_type, projection_date=projection_date, projection_time=projection_time, movie_id = movie.id)
        session.add(p)
        session.commit()

        return p.id

    def get_by_id(self, *, projection_id):

        session = self.db.session()
        projection = session.query(Projection). \
            filter(Projection.id == projection_id). \
            one()

        session.commit()
        return projection

    def get_all(self):
        session = self.db.session()
        projections = session.query(Projection).all()
        session.commit()

        return projections

    def get_projections_for_movie_by_date(self, *, movie_id, date):

        movie = self.movie_gateway.get_by_id(movie_id=movie_id)
        result = []
        for p in movie.projections:
            if p.projection_date == date:
                result.append(p)
        return result

    def get_projections_for_movie_without_date(self, *, movie_id):

        movie = self.movie_gateway.get_by_id(movie_id=movie_id)
        return movie.projections

    def update_date(self, projection_id, new_date):
        session = self.db.session()
        projection = session.query(Projection).filter(Projection.id == projection_id).one()
        projection.projection_date = new_date
        session.commit()

    def update_time(self, projection_id, new_time):
        session = self.db.session()
        projection = session.query(Projection).filter(Projection.id == projection_id).one()
        projection.projection_date = new_time
        session.commit()

    def delete_projection(self, projection_id):
        session = self.db.session()
        session.query(Projection).filter(Projection.id == projection_id).delete()
        session.commit()
