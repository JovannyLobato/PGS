import face_recognition
import numpy as np
from models.kid import Kid
from config.database import Session
from utils.face_utils import capturar_rostro

def registrar_kid(self):
    nombre = self.input_nombre.text()
    apellidos = self.input_apellidos.text()
    tutor = self.input_tutor.text()
    maestro = self.input_maestro.text()
    grado = self.input_grado.text()

    if not all([self.ruta_imagen, nombre, apellidos, tutor, maestro, grado]):
        QMessageBox.warning(self, "Campos incompletos", "Por favor, llena todos los campos y selecciona una imagen.")
        return

    try:
        # 1. Cargar imagen y obtener encoding facial
        imagen = face_recognition.load_image_file(self.ruta_imagen)
        encodings = face_recognition.face_encodings(imagen)
        if not encodings:
            QMessageBox.critical(self, "Error", "No se detectó ningún rostro en la imagen.")
            return

        face_encoding = encodings[0]
        face_encoding_bytes = np.array(face_encoding).tobytes()

        # 2. Crear instancia de Kid
        nuevo_kid = Kid(
            nombre=nombre,
            apellidos=apellidos,
            tutor=tutor,
            maestro=maestro,
            grado=grado,
            face_encoding=face_encoding_bytes
        )

        # 3. Guardar en la base de datos
        Session = sessionmaker(bind=engine)
        session = Session()
        session.add(nuevo_kid)
        session.commit()
        session.close()

        QMessageBox.information(self, "Éxito", "Niño registrado correctamente.")
        self.close()

    except Exception as e:
        QMessageBox.critical(self, "Error", f"Ocurrió un error:\n{str(e)}")
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

def guardar_kid(nombre, path_imagen):
    with open(path_imagen, 'rb') as f:
        imagen_binaria = f.read()
    nuevo_kid = Kid(nombre=nombre, rostro=imagen_binaria)
    session.add(nuevo_kid)
    session.commit()


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
