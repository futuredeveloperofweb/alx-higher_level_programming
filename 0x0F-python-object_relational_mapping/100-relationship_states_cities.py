#!/usr/bin/python3
'''a script that creates the State “California” with the City
“San Francisco” from the database hbtn_0e_100_usa'''
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
    n_ct = City(name='San Francisco')
    n_st = State(name='California')
    new.cities.append(n_ct)
    session.add_all([n_st, n_ct])
    session.commit()
    session.close()
