#!/usr/bin/python3
"""
This module defines the State class and an instance of Base
using SQLAlchemy to map the Python class to a MySQL table.
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    State class links to the MySQL table 'states' with attributes
    representing the table columns id and name.
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
