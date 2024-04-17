#!/usr/bin/python3
"""State Module for HBNB project"""
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # Check the storage type using environment variable
    storage_type = os.getenv('HBNB_TYPE_STORAGE')

    # Define the `cities` attribute conditionally based on storage type
    if storage_type == 'db':
        # For DBStorage, set up a relationship with the `City` class
        cities = relationship(
            'City',
            cascade='all, delete, delete-orphan',
            backref='state'
        )
    else:
        # For FileStorage, define a getter property for `cities`
        @property
        def cities(self):
            """Returns a list of City instances with state_id equals to the current State.id."""
            from models import storage
            cities_list = []
            # Iterate over all City objects in storage and filter by state_id
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
