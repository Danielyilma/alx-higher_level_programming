#!/usr/bin/python3
'''
creating state class that has relationship to city class
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


Base = declarative_base()


class State(Base):
    '''
    state class that is mapped to the database states table
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship(
        'City', cascade='all, delete, delete-orphan',
        back_populates='state'
    )
