from sqlalchemy.orm import Session
from app.models.students import Student  # <-- corregido: 'students' en plural
from app.schemas.student import StudentCreate

def get_students(db: Session):
    return db.query(Student).all()

def create_student(db: Session, student: StudentCreate):
    db_student = Student(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

