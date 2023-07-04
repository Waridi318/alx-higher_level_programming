#!/usr/bin/python3

"""
This script prints all City objects from the database hbtn_0e_14_usa
"""


import sys
from sqlalchemy import create_engine
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )

    Session = sessionmaker(bind=engine)
    session = Session()
    cities = session.query(City).join(State).order_by(City.id)

    for city in cities:
        print('{}: ({}) {}'.format(city.state.name, city.id, city.name))
