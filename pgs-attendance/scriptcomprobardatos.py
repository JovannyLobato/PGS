import os
import face_recognition
import numpy as np
from sqlalchemy.orm import Session
from config.database import SessionLocal
from models.kid import Kid

# Ruta a las imágenes base (usa nombres como 'Jovany Lobato Merenguez.jpg')
IMAGES_PATH = "kids_faces"

def nombre_archivo_coincide(nombre_kid):
    # Simplifica el nombre del niño para matchear con el archivo
    nombre = nombre_kid.lower().replace(" ", "")
    for archivo in os.listdir(IMAGES_PATH):
        if archivo.lower().endswith(('.jpg', '.jpeg', '.png')):
            nombre_archivo = os.path.splitext(archivo)[0].lower().replace(" ", "")
            if nombre_archivo == nombre:
                return os.path.join(IMAGES_PATH, archivo)
    return None

db: Session = SessionLocal()
kids = db.query(Kid).all()

for kid in kids:
    ruta = nombre_archivo_coincide(kid.name)
    if ruta:
        print(f"Procesando: {kid.name} ({ruta})")
        imagen = face_recognition.load_image_file(ruta)
        encodings = face_recognition.face_encodings(imagen)

        if len(encodings) > 0:
            encoding = encodings[0].astype(np.float64)  # Asegura tipo correcto
            kid.face_encoding = encoding.tobytes()
            print(f"✓ Guardado correctamente para {kid.name}")
        else:
            print(f"⚠ No se detectó rostro en {ruta}")
    else:
        print(f"⚠ No se encontró imagen para {kid.name}")

db.commit()
db.close()
print("Proceso completado.")




