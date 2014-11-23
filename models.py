from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import settings


Base = declarative_base()

session = None

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


def database_init():
    if settings.__DATABASE_TYPE__ not in ['sqlite']:
        return None
    engine = create_engine('%s:///%s' % (settings.__DATABASE_TYPE__, settings.__DATABASE_NAME__), echo=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
