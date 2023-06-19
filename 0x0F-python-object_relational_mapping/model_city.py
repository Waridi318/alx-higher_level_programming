#!/usr/bin/python3

"""
This module contains class City
"""


from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base

engine = create_engine(
    'mysql+mysqldb://root:root@localhost:3306/hbtn_0e_14_usa')


Session = sessionmaker(bind=engine)
session = Session()


class City(Base):
    """
    This is class definition of a city
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
