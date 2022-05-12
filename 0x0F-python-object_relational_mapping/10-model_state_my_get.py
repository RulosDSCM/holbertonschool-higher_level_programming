#!/usr/bin/python3
"""Start link class to table in database
"""
from operator import contains
import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    states = session.query(State).filter_by(name=sys.argv[4]).first()

    if states:
        print(states.id)
    else:
        print("Not found")

    session.close()
