# import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from settings import DB_NAME

class Database:
    def __init__(self):
        self.engine = create_engine(f"sqlite:///{DB_NAME}")
        self.session = sessionmaker(bind = self.engine)
        # self.connection = sqlite3.connect(DB_NAME)
        # self.cursor = self.connection.cursor()
        
