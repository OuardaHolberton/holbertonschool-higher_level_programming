#!/usr/bin/python3
"""
This module provides a script that prints the State object id
with the name passed as an argument from the database hbtn_0e_6_usa.
If no state matches, it displays 'Not found'.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    db_url = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]
    )
    engine = create_engine(db_url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == sys.argv[4]).first()

    if state is not None:
        print("{}".format(state.id))
    else:
        print("Not found")

    session.close()
