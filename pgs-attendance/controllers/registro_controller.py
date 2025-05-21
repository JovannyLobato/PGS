# controllers/registro_controller.py

import face_recognition
import pickle
import numpy as np
from config.database import SessionLocal
from models.kid import Kid

def comparar_con_kids(image_path):
    try:
        # Cargar y codificar imagen capturada
        imagen_capturada = face_recognition.load_image_file(image_path)
        codigos_captura = face_recognition.face_encodings(imagen_capturada)

        if not codigos_captura:
            return "No se detectó ningún rostro en la imagen capturada."

        rostro_capturado = codigos_captura[0]

        # Conectarse a la base de datos
        session = SessionLocal()
        kids = session.query(Kid).all()

        for kid in kids:
            if not kid.face_encoding:
                continue

            encoding_kid = pickle.loads(kid.face_encoding)

            if face_recognition.compare_faces([encoding_kid], rostro_capturado)[0]:
                session.close()
                return f"✅ Rostro identificado: {kid.name}"

        session.close()
        return "❌ Rostro no reconocido en la base de datos."

    except Exception as e:
        return f"⚠️Error: {str(e)}"

