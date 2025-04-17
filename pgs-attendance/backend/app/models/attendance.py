from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.core.database import Base

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    type = Column(String)  # checkin o checkout
    timestamp = Column(DateTime, default=datetime.utcnow)
    verified_by = Column(Integer, ForeignKey("users.id"))

    student = relationship("Student", back_populates="attendance")

