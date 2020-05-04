CREATE_MOVIE_TABLE = '''
    CREATE TABLE IF NOT EXISTS movies (
        id integer PRIMARY KEY NOT NULL,
        movie_name varchar(50) UNIQUE,
        rating REAL NOT NULL 
    );
'''

CREATE_MOVIE = f'''
        INSERT INTO movies (movie_name, rating)
             VALUES ( ? , ? );
'''
GET_BY_ID = f'''
        SELECT id, movie_name, rating from movies WHERE id = ?;
'''
# select movie_name,rating from movies order by rating desc
GET_ALL_MOVIES_ORDERED_BY_RATING = f'''
        SELECT id, movie_name, rating from movies ORDER BY rating DESC;
'''

UPDATE_MOVIE_NAME = f'''
        UPDATE movies SET movie_name = ? WHERE id = ?;
'''

UPDATE_MOVIE_RATING = f'''
        UPDATE movies SET rating = ? WHERE id = ?;
'''

DELETE_MOVIE = f'''
        DELETE FROM movies WHERE id = ?;
'''
