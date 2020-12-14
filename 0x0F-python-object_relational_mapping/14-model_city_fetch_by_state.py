#!/usr/bin/python3
"""Prints all City objects"""

from model_city import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    obj = session.query(City.id, City.name,
                        State.name).join(State, State.id == City.state_id).\
        order_by(City.id).all()
    for row in obj:
        print("{}: ({}) {}".format(row[2], row[0], row[1]))
    session.close()
