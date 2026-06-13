#!/usr/bin/python3
"""
This module defines the City class that represents a city
mapped to the MySQL table 'cities' using SQLAlchemy.
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    City class links to the MySQL table 'cities' with attributes
    representing columns for id, name, and state_id.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
