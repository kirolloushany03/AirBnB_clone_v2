#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
from sqlalchemy.engine import create_engine
from models.city import City
from models.state import State
from models.user import User
from sqlalchemy.orm import sessionmaker, scoped_session
from os import environ
from itertools import chain


class DBStorage:
    '''Class to handle database storage'''
    __engine = None
    __session = None

    def __init__(self):
        '''constructor for dbstorage'''
        from models.base_model import Base
        self.__engine = create_engine(f"mysql+mysqldb://{environ['HBNB_MYSQL_USER']}:{environ['HBNB_MYSQL_PWD']}@{environ['HBNB_MYSQL_HOST']}:3306/{environ['HBNB_MYSQL_DB']}", pool_pre_ping=True)
        if 'HBNB_ENV' in environ and environ['HBNB_ENV'] == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        '''get a dictionary that contains all objects stored in the current session'''
        from models.city import City
        from models.state import State
        from models.user import User

        if cls is None:
            queries = chain(self.__session.query(State), self.__session.query(City), self.__session.query(User))
        else:
            queries = self.__session.query(cls)

        return {f'{type(obj).__name__}.{obj.id}': obj for obj in queries}

    def new(self, obj):
        '''add obj to the current session'''
        print('calling new')
        self.__session.add(obj)

    def save(self):
        '''save current session to the database'''
        self.__session.commit()

    def delete(self, obj=None):
        '''delete obj from the current session if obj is not None'''
        if obj is None:
            return

        self.__session.delete(obj)

    def reload(self):
        '''creates all tables in the database, initializes current session'''
        from models.base_model import Base
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
