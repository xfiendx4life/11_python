from sqlalchemy import create_engine
from sqlalchemy import Table, Column, DateTime, func, Integer, String, MetaData, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref


engine = create_engine('sqlite:///bf.db')

Base = declarative_base()


class Person(Base):  
    __tablename__ = 'person' 
    id = Column(Integer, primary_key=True)
    login = Column(String)
    password = Column(String)
    info = Column(String)
    
    def __init__(self, name, password, info):
        self.login = name
        self.password = password
        self.info = info

class UserSession(Base):
    __tablename__ = 'usersession' 
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('person.id'))
    start_time = Column(DateTime, default = func.now())
    finish_time = Column(DateTime)
    person = relationship (Person, backref='usersessions', uselist=True)



Base.metadata.create_all(engine)