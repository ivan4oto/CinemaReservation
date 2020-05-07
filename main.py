import sys

from db import Database
from db_schema import CREATE_USERS, CREATE_MOVIE_TABLE, CREATE_RESERVATIONS, CREATE_PROJECTION_TABLE
from index_view import login


con = Database()

class Application:

    @classmethod
    def build(self):
        with con.connection:
            con.cursor.execute(CREATE_USERS)
            con.cursor.execute(CREATE_MOVIE_TABLE)
            con.cursor.execute(CREATE_PROJECTION_TABLE)
            con.cursor.execute(CREATE_RESERVATIONS)

        # TODO: Build rest of the tables
        # TODO: Seed with inistial data - consider using another command for this


        print('Done.')

    @classmethod
    def start(self): 
        user = login()

if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        Application.start()
    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')
