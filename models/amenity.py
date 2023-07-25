#!/usr/bin/python3
"""
Amenity Module for HBNB project
"""
import models
from os import getenv
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Will be mapped to amenities table
    """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        from models.place import place_amenity
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place",secondary=place_amenity, viewonly=False, back_populates="amenities")

    else:
        name = ""
