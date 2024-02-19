#!/usr/bin/python3
'''
quering data based on relationship
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State
import sys


def main():
    '''main function that run when it is not imported'''
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).order_by(State.id).all()

    for state in results:
        print("{}: {}".format(state.id, state.name))
        for city in state.cities:
            print('    {}: {}'.format(city.id, city.name))


if __name__ == '__main__':
    main()
