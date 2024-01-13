#!/usr/bin/python3
'''a script that lists all City objects from the database hbtn_0e_101_usa'''
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import create_engine
import sys


if __name__ == "__main__":
    db_uri = 'mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3])

    engine = create_engine(db_uri, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for ct in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(ct.id, ct.name, ct.state.name))
    session.close()
