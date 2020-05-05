CREATE_PROJECTION_TABLE = '''
     CREATE TABLE IF NOT EXISTS projections (
        id integer PRIMARY KEY NOT NULL,
        movie_type varchar(50) UNIQUE,
        projection_date varchar(50) UNIQUE,
        projection_time varchar(50) UNIQUE,
        movie_id INTEGER,
        CONSTRAINT fk_movie foreign key (movie_id) REFERENCES movies(id));
'''



CREATE_PROJECTION = f'''
        INSERT INTO projections (movie_type, projection_date, projection_time, movie_id)
             VALUES ( ? , ? , ? ,?);
'''
GET_BY_ID = f'''
        SELECT id,movie_type, projection_date, projection_time, movie_id from projections WHERE id = ?;
'''

GET_PROJECTIONS_FOR_MOVIE_BY_DATE = f'''
        SELECT id,movie_type, projection_date, projection_time, movie_id from projections
            WHERE movie_id = ? AND projection_date = ?
            ORDER BY projection_date DESC;
'''

GET_PROJECTIONS_FOR_MOVIE_WITHOUT_DATE = f'''
        SELECT id,movie_type, projection_date, projection_time, movie_id from projections
            WHERE movie_id = ?
            ORDER BY projection_date DESC;
'''

GET_ALL = f'''
        SELECT id,movie_type, projection_date, projection_time, movie_id  from projections;
'''

UPDATE_DATE = f'''
        UPDATE projections SET projection_date = ? WHERE id = ?;
'''

UPDATE_TIME = f'''
        UPDATE projections SET projection_time = ? WHERE id = ?;
'''

DELETE_PROJECTION = f'''
        DELETE FROM projections WHERE id = ?;
'''
