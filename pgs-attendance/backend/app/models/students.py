from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from app.core.database import Base

class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
    birth_date = Column(Date)
    grade = Column(String)
    group = Column(String)

    fingerprints = relationship("Fingerprint", back_populates="student")
    attendance = relationship("Attendance", back_populates="student")

