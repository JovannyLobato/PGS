from fastapi import FastAPI
from app.api import students
from app.core.database import Base, engine
from app.models import user, role, students as student_model, guardian, fingerprint, attendance, association

app = FastAPI()
app.include_router(students.router)

