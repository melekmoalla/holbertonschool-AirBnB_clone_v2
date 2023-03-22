#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, INTEGER, Float
from sqlalchemy.orm import relationship
from models.review import Review


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128),  nullable=False)
    description = Column(String(1024),  nullable=True)
    number_rooms = Column(INTEGER,  nullable=False, default=0)
    number_bathrooms = Column(INTEGER,  nullable=False, default=0)
    max_guest = Column(INTEGER,  nullable=False, default=0)
    price_by_night = Column(INTEGER,  nullable=False, default=0)
    latitude = Column(Float,  nullable=True)
    longitude = Column(Float,  nullable=True)
    amenity_ids = []

    reviews = relationship('Review', cascade='all, delete', backref='place')

    @property
    def reviews(self):
        """Returns the list of Review instances with place_id equals to the current Place.id"""
        from models import storage
        reviews = []
        for review in storage.all(Review):
            if review.place_id == self.id:
                reviews.append(review)
        return reviews
