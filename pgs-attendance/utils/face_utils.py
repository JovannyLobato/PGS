import face_recognition
import cv2
import numpy as np
import pickle
from models.kid import Kid
from config.database import SessionLocal

# Captura el rostro y lo convierte en un encoding binario (para almacenar)
def capturar_rostro():
    cam = cv2.VideoCapture(0)
    ret, frame = cam.read()
    cam.release()

    if not ret:
        return None

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    locations = face_recognition.face_locations(rgb)
    encodings = face_recognition.face_encodings(rgb, locations)

    if encodings:
        return pickle.dumps(encodings[0])  # Guardar como binario
    return None

# Compara una imagen nueva con todos los encodings almacenados en la BD
def comparar_con_db(yo1_path):
    yo1_image = face_recognition.load_image_file(yo1_path)
    yo1_encodings = face_recognition.face_encodings(yo1_image)

    if not yo1_encodings:
        print("❌ No se detectó ningún rostro en la imagen proporcionada.")
        return

    yo1_encoding = yo1_encodings[0]
    session = SessionLocal()
    kids = session.query(Kid).all()

    for kid in kids:
        if kid.face_encoding is None:
            continue

        encoding_kid = pickle.loads(kid.face_encoding)
        resultado = face_recognition.compare_faces([encoding_kid], yo1_encoding)[0]
        distancia = np.linalg.norm(encoding_kid - yo1_encoding)

        print(f"🔍 Comparando con: {kid.name} → {'✅ Coincidencia' if resultado else '❌ No coincide'} (Distancia: {distancia:.2f})")

    session.close()

