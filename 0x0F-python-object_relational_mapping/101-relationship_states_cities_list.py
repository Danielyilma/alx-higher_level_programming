#!/usr/bin/python3
'''
quering data based on relationship
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base
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

    results = session.query(State).join(City).\
        order_by(State.id.asc(), City.id.asc()).all()

    for state in results:
        print(f'{state.id}: {state.name}')
        for city in state.cities:
            print(f'    {city.id}: {city.name}')


if __name__ == '__main__':
    main()
