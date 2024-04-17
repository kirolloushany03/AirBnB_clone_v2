#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('Child', cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        from models.city import City
        from models import storage
        return [
            obj for k, obj in storage.all().items()
            if type(obj) is City and obj.state_id == self.id
        ]
