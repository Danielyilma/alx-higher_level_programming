#!/usr/bin/python3
'''
defining states table using sqlalchemy in mysql database
'''
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, String, Column


Base = declarative_base()


class State(Base):
    '''
    state class that is mapped to the database states table
    '''
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
