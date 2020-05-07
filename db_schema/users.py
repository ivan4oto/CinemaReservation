CREATE_USERS = '''
    CREATE TABLE IF NOT EXISTS Users (
        id integer PRIMARY KEY NOT NULL,
        username varchar(50) UNIQUE,
        hashed_password varchar(250)
    );
'''

CREATE_RESERVATIONS = '''
    CREATE TABLE IF NOT EXISTS Reservations (
        id INTEGER PRIMARY KEY NOT NULL,
        user_id,
        projection_id,
        row INTEGER,
        col INTEGER,
        FOREIGN KEY (user_id) REFERENCES Users (id),
        FOREIGN KEY (projection_id) REFERENCES Projections (id)
    );
'''

ADD_USER = f'''
    INSERT INTO users (username, hashed_password)
    VALUES ( ? , ? );
    '''

SELECT_USER_ID = f'''
    SELECT id, username
    FROM users
    WHERE username = ?;
    '''

SELECT_USER_HASH_PASSWORD = f'''
    SELECT hashed_password
    FROM users
    WHERE username = ?;
    '''

SELECT_ALL_USERS = f'''
    SELECT id, username FROM users;
    '''

