from sqlalchemy import Column, Integer, ForeignKey, Table
from app.core.database import Base

user_student_table = Table(
    "user_student",
    Base.metadata,
    Column("user_id", Integer, ForeignKey("users.id")),
    Column("student_id", Integer, ForeignKey("students.id"))
)

