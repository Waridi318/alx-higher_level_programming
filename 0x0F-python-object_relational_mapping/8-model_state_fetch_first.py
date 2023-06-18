#!/usr/bin/python3
"""
This module prints the first State object
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

    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.id == 1)
    state = states.first()
    if states:
        print('{}: {}'.format(state.id, state.name))
    else:
        print('Nothing')
