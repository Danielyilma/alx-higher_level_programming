#!/usr/bin/python3
'''
retrieving rows from a database table named states
'''
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main():
    engine = create_engine(
        '''mysql+mysqldb://{}:{}@localhost:3306/{}'''.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    row = session.query(State).first()

    if row:
        print("{}: {}".format(row.id, row.name))
    else:
        print("Nothing")


if __name__ == '__main__':
    main()
