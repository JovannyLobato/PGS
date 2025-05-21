from sqlalchemy import Column, Integer, String, LargeBinary
from config.database import Base

class Kid(Base):
    __tablename__ = "kids"
    __table_args__ = {"schema": "public"} 

    id = Column(Integer, primary_key=True)
    name = Column(String)
    face_encoding = Column(LargeBinary)

