#!/usr/bin/python3
'''
creating city class that has relationship to state class
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from relationship_state import Base


class City(Base):
    '''
    City class that is mapped to the database cities table
    '''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

    state = relationship('State', back_populates='cities')
