#!/usr/bin/python3
"""Print the first state of the database hbtn_0e_6_usa"""

from model_state import Base, State
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
    data = session.query(State).order_by(State.id).first()
    if data is None:
        print("Nothing")
    else:
        print("{}: {}".format(data.id, data.name))
    session.close()
