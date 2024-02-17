#!/usr/bin/python3
'''
creating city table in database and displaying the rows
'''
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys


def main():
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    results = session.query(State, City).join(City)\
        .order_by(City.id.asc()).all()

    for state, city in results:
        print(
            '{}: ({}) {}'.format(state.name, city.id, city.name)
        )


if __name__ == '__main__':
    main()
