#!/usr/bin/python3
'''
defining city table using sqlalchemy in mysql database
'''
from sqlalchemy import Column, String, Integer, ForeignKey
from model_state import Base


class City(Base):
    '''city class that is mapped to database'''
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
