from sqlalchemy import Column, Integer, String
from config.database import Base

class Kid(Base):
    __tablename__ = "kids"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fingerprint_hash = Column(String)  # cadena que representa la huella

