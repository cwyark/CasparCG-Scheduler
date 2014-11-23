from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import settings


Base = declarative_base()


class ResourceList(Base):
    __tablename__ = "resource_list"
    id = Column(Integer, primary_key=True)
    file_name = Column(String)
    file_path = Column(String)
    file_category = Column(String)
    on_the_air = relationship("OnTheAir")

    def __init__(self, file_name, file_path, file_category):
        self.file_name = file_name
        self.file_path = file_path
        self.file_category = file_category


class OnTheAir(Base):
    __tablename__ = 'on_the_air_list'
    id = Column(Integer, primary_key=True)
    resource = Column(String, ForeignKey('resource_list.file_name'))
    playtime = Column(DateTime)

    def __init__(self, name, playtime, filepath):
        self.name = name
        self.playtime = playtime


class ModelHandler(object):

    def __init__(self):
        if settings.__DATABASE_TYPE__ not in ['sqlite']:
            return None
        engine = create_engine('%s:///%s' % (settings.__DATABASE_TYPE__, settings.__DATABASE_NAME__), echo=True)
        Base.metadata.create_all(engine)
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def update_resource_list(self, resource_list):
        try:
            resources = self.session.query(ResourceList)
            for item in resources:
                print item.file_name
        except:
            pass
