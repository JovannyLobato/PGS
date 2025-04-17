from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Fingerprint(Base):
    __tablename__ = "fingerprints"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    template_hash = Column(String)
    device_id = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)

    student = relationship("Student", back_populates="fingerprints")

