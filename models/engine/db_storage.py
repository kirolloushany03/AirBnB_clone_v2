#!/usr/bin/python3
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base, BaseModel
from models.user import User
from models.state import State
from models.city import City
from itertools import chain


class DBStorage:
    """DBStorage class for handling MySQL database storage."""
    __engine = None
    __session = None

    def __init__(self):
        """Initialize DBStorage by creating engine and session."""
        user = os.getenv('HBNB_MYSQL_USER')
        pasword = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST ')
        db = os.getenv('HBNB_MYSQL_DB')
        env = os.getenv('HBNB_ENV')

        url = f"mysql+mysqldb://{user}:{pasword}@{host}:3306/{db}"
        
        self.__engine = create_engine(
                url ,
                pool_pre_ping=True
            )

        if env == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """Retrieve all instances of cls from the database, or all types if cls is None."""
        if cls is None:
            queries = chain(self.__session.query(State), self.__session.query(City), self.__session.query(User))
        else:
            queries = self.__session.query(cls)
        return {f'{type(obj).__name__}.{obj.id}': obj for obj in queries}
    
    def new(self, obj):
        """Add an object to the current database session."""
        print('calling new')
        self.__session.add(obj)

    def save(self):
        """Commit all changes of the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete an object from the current database session if not None."""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Reload the database by creating all tables and initializing a new session."""
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()


