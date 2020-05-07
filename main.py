import sys

from db import Database
<<<<<<< HEAD
from db_schema import CREATE_USERS, CREATE_MOVIE_TABLE, CREATE_RESERVATIONS, CREATE_PROJECTION_TABLE
from index_view import welcome, get_seats

=======
from db_schema import CREATE_USERS, CREATE_MOVIE_TABLE

from index_view import welcome, get_number_of_seats
>>>>>>> 281bf92dc269d6f227da6cf678d9ec45702b8521

con = Database()

class Application:

    @classmethod
    def build(self):
<<<<<<< HEAD
        with con.connection:
            con.cursor.execute(CREATE_USERS)
            con.cursor.execute(CREATE_MOVIE_TABLE)
            con.cursor.execute(CREATE_PROJECTION_TABLE)
            con.cursor.execute(CREATE_RESERVATIONS)
=======
        db = Database()
        db.cursor.execute(CREATE_USERS)
        db.cursor.execute(CREATE_MOVIE_TABLE)
>>>>>>> 281bf92dc269d6f227da6cf678d9ec45702b8521

        # TODO: Build rest of the tables
        # TODO: Seed with inistial data - consider using another command for this


        print('Done.')

    @classmethod
    def start(self): 
        welcome()
<<<<<<< HEAD
        get_seats()
=======
        get_number_of_seats()

>>>>>>> 281bf92dc269d6f227da6cf678d9ec45702b8521

if __name__ == '__main__':
    command = sys.argv[1]

    if command == 'build':
        Application.build()
    elif command == 'start':
        Application.start()
    else:
        raise ValueError(f'Unknown command {command}. Valid ones are "build" and "start"')
