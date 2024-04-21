#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, ForeignKey, Table
from models.place import Place

class Amenity(BaseModel, Base):
    """This is the Amenity class
    Attributes:
        name: input name
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity")

    """Association table for many-to-many relation between Place and Amenity"""
    place_amenity = Table('place_amenity', Base.metadata,
                          Column('place_id', String(60), ForeignKey('places.id'), primary_key=True),
                          Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True),
                          extend_existing=True
                         )
