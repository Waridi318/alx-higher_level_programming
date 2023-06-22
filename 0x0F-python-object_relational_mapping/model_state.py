#!/usr/bin/python3

"""
This module contains the class definition of a State
and an instance Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
# from sqlalchemy.orm import sessionmaker, relationship

# engine = create_engine(
#    'mysql+mysqldb://root:root@localhost:3306/hbtn_0e_6_usa'
# )

Base = declarative_base()
# Session = sessionmaker(bind=engine)
# session = Session()


class State(Base):
    """
    This is class definition of a state
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
#    cities = relationship("City", backref='state')
