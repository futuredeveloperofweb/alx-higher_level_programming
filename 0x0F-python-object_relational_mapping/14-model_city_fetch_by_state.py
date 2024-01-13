#!/usr/bin/python3
'''A script that prints all City objects from the database hbtn_0e_14_usa'''
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    for st, ct in session.query(State, City).join(City).order_by(City.id):
        print('{}: ({}) {}'.format(st.name, ct.id, ct.name))
    session.close()
