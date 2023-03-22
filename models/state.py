#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')

    @property
    def cities(self):
        from models.city import City
        from models import storage
        city_list = []
        for city in storage.all(City):
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
