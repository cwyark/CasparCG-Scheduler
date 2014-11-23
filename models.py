from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import uuid


Base = declarative_base()


class OnTheAir(Base):
    __tablename__ = 'OnTheAir_list'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    playtime = Column(DateTime)
    filepath = Column(String)

    def __init__(self, name, tag, playtime, filepath):
        self.name = name
        self.playtime = playtime
        self.filepath = filepath


engine = create_engine('sqlite:///database.sqlite', echo=True)
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def insert_item(name, playtime, filepath):
    item = OnTheAir(name, playtime, filepath)
    session.add(item)

