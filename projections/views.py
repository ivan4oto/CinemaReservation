from projections.controllers import ProjectionController
from tabulate import tabulate

class ProjectionViews:
    def __init__(self):
        self.controller = ProjectionController()

    def create(self):
        print("Enter type, date, time and movie_id!")
        movie_type = input('Type: ')
        projection_date = input('Date: ')
        projection_time = input('Time: ')
        movie_id = int(input('Movie Id: '))

        if self.controller.create_projection(movie_type=movie_type, projection_date=projection_date,
                                             projection_time=projection_time, movie_id=movie_id):
            print("Movie was successfully created")

    def get_by_id(self):
        projection_id = input('Enter projection id: ')
        projection = self.controller.get_projection_by_id(projection_id=projection_id)
        print(projection)

    def get_all(self):
        projections = self.controller.get_all()

        for p in projections:
            print(p)

    def update_data_projection(self):
        projection_id = input('Enter projection id: ')
        new_data = input('Enter new data: ')

        if self.controller.update_date(projection_id=projection_id, new_date=new_data):
            print("Projection was successfully updated")

    def update_time(self):
        projection_id = input('Enter projection id: ')
        new_time = input('Enter new time: ')

        if self.controller.update_time(projection_id=projection_id, new_time=new_time):
            print("Projection was successfully updated")

    def delete_movie(self):
        projection_id = input('Enter projection id: ')

        if self.controller.delete(projection_id=projection_id):
            print("Projection was successfully deleted")

    def get_projections_for_movie(self):
        print("\nStep 2 (Movie): Choose a movie> \n")
        movie_id = input('Enter movie id: ')
        p_data = input('Enter date (optional): ')

        if movie_id == 'cancel' or p_data == 'cancel':
            exit()

        projections = self.controller.get_projections_for_movie(movie_id=movie_id, date=p_data)
        projections_table = [[p.projections_id, p.movie_type, p.projection_date, p.projection_time] for p in projections]
        projections_headers = ['ID', 'Type', 'Date', 'Time']
        print(tabulate(projections_table, projections_headers, tablefmt = 'psql'))

        # for p in projections:
        #     print(p)

        return movie_id
