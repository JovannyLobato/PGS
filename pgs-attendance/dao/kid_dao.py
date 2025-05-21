from models.kid import Kid
from config.database import Session
from utils.face_utils import capturar_rostro

def registrar_kid(nombre):
    session = Session()
    encoding = capturar_rostro()
    if encoding is None:
        print("No se detectó un rostro.")
        return

    nuevo_kid = Kid(name=nombre, face_encoding=encoding)
    session.add(nuevo_kid)
    session.commit()
    session.close()
    print("Niño registrado con éxito.")


def reconocer_kid():
    session = Session()
    todos = session.query(Kid).all()

    known_encodings = []
    nombres = []

    for kid in todos:
        if kid.face_encoding:
            known_encodings.append(np.frombuffer(kid.face_encoding, dtype=np.float64))
            nombres.append((kid.id, kid.name))

    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()

    if not ret:
        return None

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    locations = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, locations)

    for enc in encodings:
        results = face_recognition.compare_faces(known_encodings, enc)
        if True in results:
            idx = results.index(True)
            session.close()
            return nombres[idx]  # (id, nombre)

    session.close()
    return None



"""
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
"""
