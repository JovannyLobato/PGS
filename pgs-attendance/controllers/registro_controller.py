# controllers/registro_controller.py

import face_recognition
from sqlalchemy.orm import Session
from models.registro import Registro
from config.database import SessionLocal
from models.kid import Kid
import numpy as np

def comparar_con_kids(image_path):
    try:
        # Cargar imagen capturada y obtener su encoding
        imagen_capturada = face_recognition.load_image_file(image_path)
        codigos_captura = face_recognition.face_encodings(imagen_capturada)

        if not codigos_captura:
            return "No se detectó ningún rostro en la imagen."

        rostro_capturado = codigos_captura[0]

        db: Session = SessionLocal()
        try:
            kids = db.query(Kid).all()

            for kid in kids:
                if not kid.face_encoding:
                    continue

                # Convertir el LargeBinary a numpy array
                encoding_bd = np.frombuffer(kid.face_encoding, dtype=np.float64)

                # Comparar rostros
                resultados = face_recognition.compare_faces([encoding_bd], rostro_capturado)

                if resultados[0]:
                    # Registrar la entrada
                    nuevo_registro = Registro(kid_id=kid.id)
                    db.add(nuevo_registro)
                    db.commit()
                    db.refresh(nuevo_registro)

                    return f"Entrada registrada para {kid.name} (ID: {kid.id}) correctamente."

            return "Rostro no reconocido en la base de datos."

        finally:
            db.close()

    except Exception as e:
        return f"Error al procesar la imagen: {str(e)}"

