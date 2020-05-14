import sys
from db import Database
from index_view import login, make_choice, UserViews, admin_panel
from projections.controllers import ProjectionController
from users.users_gateway import UserGateway
from movies.movies_getaway import MovieGateway



user_gate = UserGateway()
movies_gate = MovieGateway()

class Application:

    @classmethod
    def make_admin(self):
        userview = UserViews()
        adminname = input('\nYou have entered the Admin creation panel.\nTo create a new admin account please enter a username:\n')
        userview.make_admin(adminname)

    @classmethod
    def build(self):
        user_gate.create_user_table()
        movies_gate.create_movies_table()
        print('Done.')

    @classmethod
    def start(self): 
        user = login()
        if user.usertype == 'admin':
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
