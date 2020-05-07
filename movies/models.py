class MovieModel:
    def __init__(self, *, movie_id, name, rating):
        self.movie_id = movie_id
        self.name = name
        self.rating = rating

    def __str__(self):
        return f'[{self.movie_id}] {self.name} ({self.rating}).'

    @staticmethod
    def validate(name, rating):
        if len(name) == 1 or name is None:
            raise ValueError("Name should be bigger than 1 and should be not None!")
        if rating < 0:
            raise ValueError("Rating should be bigger than zero!")

    @staticmethod
    def convert(movie_db):
        return MovieModel(movie_id=movie_db[0], name=movie_db[1], rating=movie_db[2])
