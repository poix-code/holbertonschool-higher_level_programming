#!/usr/bin/python3
"""Deletes a state"""

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
    to_del = session.query(State).order_by(State.id).filter(State.name.
                                                            like('%a%'))
    for row in to_del:
        session.delete(row)
    session.commit()
    session.close()
