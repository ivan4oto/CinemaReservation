from .movies_getaway import MovieGateway

class MovieController:
    def __init__(self):
        self.movies_gateway = MovieGateway()

    def create_movie(self, name, rating):
        self.movies_gateway.create(name=name, rating=rating)
        return True

    def get_movie_by_id(self, movie_id):
        movie = self.movies_gateway.get_by_id(movie_id=movie_id)
        return movie

    def get_all_movies_ordered_by_rating(self):
        movies = self.movies_gateway.get_all_movies_ordered_by_rating()
        return movies

    def update_movie_name(self, movie_id, new_name):
        self.movies_gateway.update_movie_name(movie_id=movie_id, new_name=new_name)
        return True

    def update_movie_rating(self, movie_id, new_rating):
        self.movies_gateway.update_movie_rating(movie_id=movie_id, new_rating=new_rating)
        return True

    def delete_movie(self, movie_id):
        self.movies_gateway.delete_movie(movie_id=movie_id)
        return True
