from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from config.database import Base

class Registro(Base):
    __tablename__ = "registros"

    id = Column(Integer, primary_key=True)
    kid_id = Column(Integer, ForeignKey("public.kids.id"))
    timestamp = Column(DateTime, default=func.now())

