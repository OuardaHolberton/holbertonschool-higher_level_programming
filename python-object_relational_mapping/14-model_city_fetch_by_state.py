#!/usr/bin/python3
"""
This module provides a script that lists all City objects from
the database hbtn_0e_14_usa sorted by cities.id via SQLAlchemy.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(City, State).join(
        State, City.state_id == State.id
    ).order_by(City.id).all()

    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
