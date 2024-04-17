#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.amenity import Amenity
from sqlalchemy.orm import relationship
from models import storage

# Create the table to establish a Many-to-Many relationship between Place and Amenity
place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)

class Place(BaseModel, Base):
    """ A class representing a place in the HBNB project """
    __tablename__ = 'places'
    
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0)
    number_bathrooms = Column(Integer, default=0)
    max_guest = Column(Integer, default=0)
    price_by_night = Column(Integer, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    
    user = relationship('User')
    city = relationship('City')
    reviews = relationship('Review', back_populates="place", cascade="all, delete, delete-orphan")
    
    amenities = relationship(
        Amenity.__name__,
        secondary=place_amenity,
        back_populates="places",
        viewonly=False
    )
    
    amenity_ids = []

    @property
    def amenities(self):
        """Return the list of Amenity instances based on the amenity_ids list."""
        amenities_list = []
        for amenity_id in self.amenity_ids:
            amenity = storage.get('Amenity', amenity_id)
            if amenity:
                amenities_list.append(amenity)
        return amenities_list

    @amenities.setter
    def amenities(self, obj):
        """Add an Amenity instance to the list of amenities."""
        if isinstance(obj, Amenity):
            if obj.id not in self.amenity_ids:
                self.amenity_ids.append(obj.id)
