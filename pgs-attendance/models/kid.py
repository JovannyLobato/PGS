from sqlalchemy import Column, Integer, String, LargeBinary
from sqlalchemy.dialects.postgresql import BYTEA
from config.database import Base

class Kid(Base):
    __tablename__ = "kids"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    face_encoding = Column(LargeBinary, nullable=True) 
