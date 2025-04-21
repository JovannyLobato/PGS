from pydantic import BaseModel
from datetime import datetime

class FingerprintCreate(BaseModel):
    student_id: int
    template_hash: str
    device_id: str

class FingerprintOut(BaseModel):
    id: int
    student_id: int
    template_hash: str
    device_id: str
    created_at: datetime

    class Config:
        from_attributes = True

