#crud estudiantes (?
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.student import StudentCreate, StudentOut
from app.crud import crud_student
from app.core.database import get_db

router = APIRouter(prefix="/students", tags=["students"])

@router.get("/", response_model=list[StudentOut])
def list_students(db: Session = Depends(get_db)):
    return crud_student.get_students(db)

@router.post("/", response_model=StudentOut)
def register_student(student: StudentCreate, db: Session = Depends(get_db)):
    return crud_student.create_student(db, student)

