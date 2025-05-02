import bcrypt

def process_fingerprint(fingerprint: str) -> bytes:
    fingerprint_bytes = fingerprint.encode()
    sal = bcrypt.gensalt()
    return bcrypt.hashpw(fingerprint_bytes, sal)

def verify_fingerprint(fingerprint: str, hash_saved: bytes) -> bool:
    return bcrypt.checkpw(fingerprint.encode(), hash_saved)

