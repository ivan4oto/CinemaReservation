import bcrypt

def get_hashed_password(password):
    return bcrypt.hashpw(password, bcrypt.gensalt())

def check_password(password, hashed_password):
    return bcrypt.checkpw(password, hashed_password)

CREATE_USERS = '''
    CREATE TABLE IF NOT EXISTS users (
        id integer PRIMARY KEY NOT NULL,
        username varchar(50) UNIQUE,
        hashed_password varchar(250)
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