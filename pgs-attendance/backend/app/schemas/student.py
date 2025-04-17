from pydantic import BaseModel
from datetime import date

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    birth_date: date
    grade: str
    group: str

class StudentCreate(StudentBase):
    pass

class StudentOut(StudentBase):
    id: int

    model_config = {
        "from_attributes" : True
    }
