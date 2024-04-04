#!/usr/bin/python3
"""This prints first State object"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).order_by(State.id).first()
    """Pythonic way of calling a sessionn query to then get first states object"""
    if first:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")
    session.close()