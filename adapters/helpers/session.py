from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import Config

some_engine = create_engine(Config.uri)

Session = sessionmaker(bind=some_engine)

session = Session()
