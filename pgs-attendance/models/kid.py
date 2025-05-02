from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import BYTEA
from config.database import Base

class Kid(Base):
    __tablename__ = "kids"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    fingerprint_hash = Column(BYTEA)  # cadena que representa la huella

