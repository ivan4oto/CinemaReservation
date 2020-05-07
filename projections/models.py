class ProjectionModel:
    def __init__(self, *, projections_id, movie_type, projection_date, projection_time, movie_id):
        self.projections_id = projections_id
        self.movie_type = movie_type
        self.projection_date = projection_date
        self.projection_time = projection_time
        self.movie_id = movie_id

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
        return ProjectionModel(projections_id=projection_db[0], movie_type=projection_db[1],
                               projection_date=projection_db[2], projection_time=projection_db[3],
                               movie_id=int(projection_db[4]))
