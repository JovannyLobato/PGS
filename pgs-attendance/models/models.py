# models/models.py
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base
from datetime import datetime

Base = declarative_base()

class Nino(Base):
    __tablename__ = "ninos"
    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    tutor = Column(String)

class RegistroEntrada(Base):
    __tablename__ = "entradas"
    id = Column(Integer, primary_key=True)
    nino_id = Column(Integer, ForeignKey("ninos.id"))
    fecha_hora = Column(DateTime, default=datetime.utcnow)

