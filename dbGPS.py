from flask import *
from flaskXMLRPC import XMLRPCHandler

from os import path

from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQL access layer initialization
DATABASE_FILE = "dbGPS.sqlite"
db_exists = False
if path.exists(DATABASE_FILE):
    db_exists = True

print(db_exists)

engine = create_engine('sqlite:///%s'%(DATABASE_FILE), echo = False)

Base = declarative_base()

# DECLARATION OF CLASSES
class GPSLog(Base):
    __tablename__ = 'gpslog'
    id = Column(Integer, primary_key = True)
    id_user = Column(String)
    data = Column(String)
    hora = Column(String)
    lat = Column(Float)
    lon = Column(Float)

    def __repr__(self):
        return "<id: %d, id_user: %s, data: %s, hora: %s, lat: %f, lon: %f>" % (self.id, self.id_user, self.data, self.hora, self.lat, self.lon)

# CREATE TABLES FOR THE DATA MODELS
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

app = Flask(__name__)
handler = XMLRPCHandler('apiGPSLog')
handler.connect(app, '/apiGPSLog')

# HANDLER FUNCTIONS
@handler.register
def newGPSLog():
    print("called newGPSLog function")
    return

# OTHER FUNCTIONS

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 8000, debug = True)