from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class OnTheAir(Base):
    __tablename__ = 'OnTheAir_list'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    tag = Column(String)
    playtime = Column(DateTime)
    filepath = Column(String)

    def __init__(self, name, tag, playtime, filepath):
        self.name = name
        self.tag = tag
        self.playtime = playtime
        self.filepath = filepath


class PlayHistory(Base):
    __tablename__ = 'played_history'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    playtime = Column(DateTime)

    def __init__(self, name, playtime):
        self.name = name
        self.playtime = playtime


