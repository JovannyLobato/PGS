import face_recognition
import numpy as np
from models.kid import Kid
from config.database import Session
from config.database import SessionLocal
from utils.face_utils import capturar_rostro

def obtener_face_encoding(ruta_imagen):
    imagen = face_recognition.load_image_file(ruta_imagen)
    encoding = face_recognition.face_encodings(imagen)
    if encoding:
        return encoding[0].tobytes()
    return None

def registrar_kid(self):
    nombre = self.input_nombre.text()
    apellidos = self.input_apellidos.text()
    tutor = self.input_tutor.text()
    maestro = self.input_maestro.text()
    grado = self.input_grado.text()

    if not all([self.ruta_imagen, nombre, apellidos, tutor, maestro, grado]):
        QMessageBox.warning(self, "Campos incompletos", "Por favor, llena todos los campos y selecciona una imagen.")
        return

    encoding = obtener_face_encoding(self.ruta_imagen)
    if encoding is None:
        QMessageBox.warning(self, "Error con imagen", "No se detectó un rostro en la imagen.")
        return

    nuevo_kid = Kid(
        nombre=nombre,
        apellidos=apellidos,
        tutor=tutor,
        maestro=maestro,
        grado=grado,
        face_encoding=encoding
    )

    try:
        session = SessionLocal()
        session.add(nuevo_kid)
        session.commit()
        session.close()
        QMessageBox.information(self, "Éxito", "Niño registrado correctamente.")
    except Exception as e:
        QMessageBox.critical(self, "Error", f"Ocurrió un error al registrar: {e}")



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

def limpiar_campos(self):
    self.input_nombre.clear()
    self.input_apellidos.clear()
    self.input_tutor.clear()
    self.input_maestro.clear()
    self.input_grado.clear()
    self.label_imagen.clear()
    self.ruta_imagen = None


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
