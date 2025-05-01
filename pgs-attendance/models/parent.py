from sqlalchemy import Column, Integer, String
from config.database import Base

class Parent(Base):
    __tablename__ = "parents"
    id = Column(Integer, primary_key=True)
    name = Column(String)

