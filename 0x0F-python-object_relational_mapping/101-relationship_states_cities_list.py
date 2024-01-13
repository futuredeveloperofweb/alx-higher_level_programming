#!/usr/bin/python3
'''a script that lists all State objects, and corresponding City
objects, contained in the database hbtn_0e_101_usa'''
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy.schema import Table
from relationship_state import Base, State
from relationship_city import City
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(engine)
    for st in session.query(State).order_by(State.id).all():
        print("{}: {}".format(st.id, st.name))
        for ct in st.cities:
            print("    {}: {}".format(ct.id, ct.name))
    session.close()
