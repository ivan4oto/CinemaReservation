import sys

from db import Database
from db_schema import CREATE_USERS, CREATE_MOVIE_TABLE, CREATE_RESERVATIONS, CREATE_PROJECTION_TABLE, CREATE_MOVIE, CREATE_PROJECTION
from index_view import login, make_choice, UserModel


con = Database()

class Application:

    @classmethod
    def build(self):
        with con.connection:
            con.cursor.execute(CREATE_USERS)
            con.cursor.execute(CREATE_MOVIE_TABLE)
            con.cursor.execute(CREATE_PROJECTION_TABLE)
            con.cursor.execute(CREATE_RESERVATIONS)

            con.cursor.execute(CREATE_MOVIE,("Charlie's Angels", 4.6))
            con.cursor.execute(CREATE_MOVIE,("Fast and Furious", 6.6))
            con.cursor.execute(CREATE_MOVIE,("Rick and Morty", 9.9))
            con.cursor.execute(CREATE_MOVIE,("Die Hard", 8.2))

            con.cursor.execute(CREATE_PROJECTION,('2D', '2020-05-11', '19:30', 1))
            con.cursor.execute(CREATE_PROJECTION,('2D', '2020-05-13', '19:30', 1))
            con.cursor.execute(CREATE_PROJECTION,('2D', '2020-05-11', '16:30', 2))
            con.cursor.execute(CREATE_PROJECTION,('2D', '2020-05-13', '16:30', 1))
            con.cursor.execute(CREATE_PROJECTION,('2D', '2020-05-12', '13:30', 3))
            con.cursor.execute(CREATE_PROJECTION,('2D', '2020-05-12', '20:30', 1))



        # TODO: Build rest of the tables
        # TODO: Seed with inistial data - consider using another command for this


        print('Done.')

    @classmethod
    def start(self): 
        user = login()
        make_choice()
        








if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        Application.start()
    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')
