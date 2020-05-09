from movies.controllers import MovieController
from tabulate import tabulate


class MovieViews:
    def __init__(self):
        self.controller = MovieController()

    def create_movie(self):
        print("Enter name and rating for movie!")
        name = input('Name: ')
        rating = float(input('Rating: '))
        if self.controller.create_movie(name=name, rating=rating):
            print("Movie was successfully created")

    def get_movie_by_id(self):
        movie_id = input('\nEnter movie id: ')
        movie = self.controller.get_movie_by_id(movie_id=movie_id)
        print(movie)
        return movie

    def get_all_movies(self):
        movies = self.controller.get_all_movies_ordered_by_rating()
        movies_table = [[m.movie_id, m.name, m.rating] for m in movies]
        movies_headers = ['ID', 'Name', 'Rating']
        print(tabulate(movies_table, movies_headers, tablefmt = 'psql'))
        # for m in movies:
        #     print(m)

    def update_movie_name(self):
        movie_id = input('Enter movie id: ')
        movie_new_name = input('Enter name: ')

        if self.controller.update_movie_name(movie_id=movie_id, new_name=movie_new_name):
            print("Movie was successfully updated")

    def update_movie_rating(self):
        movie_id = input('Enter movie id: ')
        movie_new_rating = input('Enter rating: ')

        if self.controller.update_movie_rating(movie_id=movie_id, new_rating=movie_new_rating):
            print("Movie was successfully updated")

    def delete_movie(self):
        movie_id = input('Enter movie id: ')

        if self.controller.delete_movie(movie_id=movie_id):
            print("Movie was successfully deleted")
