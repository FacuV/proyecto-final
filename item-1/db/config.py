from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from pathlib import Path
from sqlalchemy.orm import sessionmaker

BASE_DIR=str(Path(__file__).parent.absolute())

DATABASE_URI = 'sqlite:////' + BASE_DIR + '/tfinal.db'

engine = create_engine(DATABASE_URI, echo=True, future=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

Base.metadata.create_all(engine)