#!/usr/bin/python3
'''a script that prints the first State object from the database
hbtn_0e_6_usa'''
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)

    Session = sessionmaker()
    session = Session(bind=engine)
    Base.metadata.create_all(engine)
    st = session.query(State).order_by(State.id).first()
    if st:
        print("{}: {}".format(st.id, st.name))
    else:
        print("Nothing")
    session.close()
