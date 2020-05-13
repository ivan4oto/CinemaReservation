import sys
from db import Database
from db_schema import CREATE_USERS, CREATE_MOVIE_TABLE, CREATE_RESERVATION, CREATE_PROJECTION_TABLE, CREATE_MOVIE, CREATE_PROJECTION, CREATE_RESERVATIONS_TABLE
from index_view import login, make_choice, UserViews, UserModel, admin_panel
from projections.controllers import ProjectionController

con = Database()

class Application:

    @classmethod
    def make_admin(self):
        userview = UserViews()
        adminname = input('\nYou have entered the Admin creation panel.\nTo create a new admin account please enter a username:\n')
        userview.make_admin(adminname)

    @classmethod
    def build(self):
        proj_contoller = ProjectionController()

        with con.connection:
            print('1')
            con.cursor.execute(CREATE_USERS)
            con.cursor.execute(CREATE_MOVIE_TABLE)
            con.cursor.execute(CREATE_PROJECTION_TABLE)
            con.cursor.execute(CREATE_RESERVATIONS_TABLE)
            print('2')

            con.cursor.execute(CREATE_MOVIE,("Charlie's Angels", 4.6))
            con.cursor.execute(CREATE_MOVIE,("Fast and Furious", 6.6))
            con.cursor.execute(CREATE_MOVIE,("Rick and Morty", 9.9))
            con.cursor.execute(CREATE_MOVIE,("Die Hard", 8.2))
            print('3')

        proj_contoller.create_projection('3d', '2020-05-20', '19:30', 1)
        proj_contoller.create_projection('3d', '2020-05-21', '19:30', 1)
        proj_contoller.create_projection('4dx', '2020-05-21', '15:30', 1)
        proj_contoller.create_projection('3d', '2020-05-20', '16:30', 2)
        proj_contoller.create_projection('2d', '2020-05-20', '12:30', 3)
        proj_contoller.create_projection('2d', '2020-05-23', '19:30', 3)
        proj_contoller.create_projection('3d', '2020-05-22', '19:30', 4)

        print('Done.')

    @classmethod
    def start(self): 
        user = login()
        if user.type == 'admin':
            admin_panel()
            exit()

        else:
            make_choice()
        


if __name__ == '__main__':
    command = input()

    if command == 'build':
        print('0')
        Application.build()
    elif command == 'start':
        Application.start()
    elif command == '1337':
        Application.make_admin()
    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')
