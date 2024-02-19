#!/usr/bin/python3
'''

'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base
import sys


def main():
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state1 = State(name='California')
    state1.cities = [
        City(name='San Francisco')
    ]

    session.add(state1)
    session.commit()


if __name__ == '__main__':
    main()
