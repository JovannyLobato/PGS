from sqlalchemy.orm import Session
from app.models.attendance import Attendance

def create_attendance(db: Session, student_id: int, type: str, verified_by: int):
    attendance = Attendance(
        student_id=student_id,
        type=type,
        verified_by=verified_by
    )
    db.add(attendance)
    db.commit()
    db.refresh(attendance)
    return attendance

