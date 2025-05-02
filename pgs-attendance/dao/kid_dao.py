from config.database import SessionLocal
from models.kid import Kid
from utils.fingerprint_utils import verify_fingerprint

def find_kid_by_fingerprint(fingerprint_plaintext: str):
    db = SessionLocal()
    kids = db.query(Kid).all()
    for kid in kids:
        if verify_fingerprint(fingerprint_plaintext, kid.fingerprint_hash):
            db.close()
            return kid
    db.close()
    return None

def get_all_kids():
    db = SessionLocal()
    kids = db.query(Kid).all()
    db.close()
    return kids
