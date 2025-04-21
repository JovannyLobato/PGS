from sqlalchemy.orm import Session
from app.models.fingerprint import Fingerprint
from app.schemas.fingerprint import FingerprintCreate

def create_fingerprint(db: Session, fp: FingerprintCreate):
    db_fp = Fingerprint(**fp.dict())
    db.add(db_fp)
    db.commit()
    db.refresh(db_fp)
    return db_fp

def get_by_template(db: Session, template_hash: str):
    return db.query(Fingerprint).filter(Fingerprint.template_hash == template_hash).first()

