from config.database import SessionLocal
from models.kid import Kid

def find_kid_by_fingerprint(fingerprint_hash):
    db = SessionLocal()
    result = db.query(Kid).filter(Kid.fingerprint_hash == fingerprint_hash).first()
    db.close()
    return result

