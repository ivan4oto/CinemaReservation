CREATE_RESERVATIONS_TABLE = '''
     CREATE TABLE IF NOT EXISTS reservations (
        id integer PRIMARY KEY NOT NULL,
        row INTEGER,
        col INTEGER ,
        user_id INTEGER,
        projection_id INTEGER,
        foreign key (user_id) REFERENCES users(id),
        foreign key (projection_id) REFERENCES projections(id));
'''

CREATE_RESERVATION = f'''
        INSERT INTO reservations (row, col, user_id,projection_id)
             VALUES ( ? , ? , ? ,?);
'''

GET_BY_ID = f'''
        SELECT id, row, col, user_id,projection_id from reservations WHERE id = ?;
'''

GET_ALL = f'''
        SELECT id, row, col, user_id,projection_id  from reservations;
'''

DELETE_RESERVATION = f'''
        DELETE FROM reservations WHERE id = ?;
'''

CHECK_ALL_FREE_SEATS = f'''
        SELECT count(*) FROM reservations WHERE user_id = 0 and projection_id = ?;
'''
CHECK_IS_SEAT_IS_FREE = f'''
        SELECT id, row, col, user_id,projection_id from reservations WHERE projection_id = ? and (row = ? and col= ?);
'''

MAKE_RESERVATION = f'''
         UPDATE reservations SET user_id = ? WHERE projection_id = ? and col = ? and row = ?;
'''

GET_ALL_RESERVATION_FOR_PROJECTION = f'''
        SELECT id, row, col, user_id,projection_id from reservations WHERE projection_id = ?;
'''