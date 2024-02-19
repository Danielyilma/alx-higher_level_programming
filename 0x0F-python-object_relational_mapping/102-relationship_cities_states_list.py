#!/usr/bin/python3
'''

'''
from sqlalchemy import create_engine, and_
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
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City).order_by(City.id).all()

    for city in results:
        print(f'{city.id} : {city.name} -> {city.state.name}')


if __name__ == '__main__':
    main()
