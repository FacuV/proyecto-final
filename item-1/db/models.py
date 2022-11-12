from db.config import Base, engine
from sqlalchemy import Column, String, Integer

class Users(Base):
    __tablename__ = "Users"
    Id = Column(Integer(), primary_key=True)
    Username = Column(String(50))
    Fullname = Column(String(200))
    Password = Column(String(120))
    IsAdmin = Column(Integer())