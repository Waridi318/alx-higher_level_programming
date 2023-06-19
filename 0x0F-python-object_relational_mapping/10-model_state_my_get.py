#!/usr/bin/python3
"""
This module  lists all State objects
from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        )
    )

    search_state = sys.argv[4]
    Session = sessionmaker(bind=engine)
    session = Session()
    state = session.query(
         State).order_by(State.id).filter(State.name == search_state).first()

    if state is None:
        print('Not found')
    else:
        print(state.id)
