from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.fingerprint import FingerprintCreate, FingerprintOut
from app.crud import crud_fingerprint
from app.crud import crud_attendance
from datetime import datetime

router = APIRouter(prefix="/fingerprints", tags=["fingerprints"])

@router.post("/", response_model=FingerprintOut)
def register_fingerprint(fp: FingerprintCreate, db: Session = Depends(get_db)):
    return crud_fingerprint.create_fingerprint(db, fp)

@router.post("/verify/")
def verify_fingerprint(
    template_hash: str,
    device_id: str,
    verified_by: int,       # ID del usuario que verifica
    type: str = "checkin",  # o "checkout", por default es "checkin"
    db: Session = Depends(get_db)
):
    fingerprint = crud_fingerprint.get_by_template(db, template_hash)
    if fingerprint:
        crud_attendance.create_attendance(
            db=db,
            student_id=fingerprint.student_id,
            type=type,
            verified_by=verified_by
        )
        return {"status": "success", "student_id": fingerprint.student_id}
    return {"status": "not_found"}

