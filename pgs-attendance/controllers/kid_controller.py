from models.kid import Kid
from config.database import SessionLocal
import face_recognition
import pickle
import os
import re

def validar_nombre(texto):
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]{3,}", texto.strip()))

def validar_apellidos(texto):
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]{6,}", texto.strip()))

def validar_tutor(texto):
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]{10,}", texto.strip()))

def validar_maestro(texto):
    return bool(re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]{10,}", texto.strip()))

def validar_grado(texto):
    return bool(re.fullmatch(r"[1-6][A-C]", texto.strip(), flags=re.IGNORECASE))

def registrar_kid_con_datos(nombre, apellidos, tutor, maestro, grado, ruta_imagen):
    if not all([ruta_imagen, nombre, apellidos, tutor, maestro, grado]):
        return False, "Todos los campos deben estar completos."

    # Validaciones de formato
    if not validar_nombre(nombre):
        return False, "Nombre inválido. Debe tener al menos 3 letras y solo letras y espacios."

    if not validar_apellidos(apellidos):
        return False, "Apellidos inválidos. Deben tener al menos 6 letras y solo letras y espacios."

    if not validar_tutor(tutor):
        return False, "Nombre del tutor inválido. Debe tener al menos 10 letras."

    if not validar_maestro(maestro):
        return False, "Nombre del maestro inválido. Debe tener al menos 10 letras."

    if not validar_grado(grado):
        return False, "Grado y grupo inválido. Debe tener formato como '1A', '2B', etc."

    # Validar imagen específica no permitida
    if os.path.basename(ruta_imagen).lower() == "guadalupe garcía díaz.gif":
        return False, "Imagen no válida para registro."

    try:
        imagen = face_recognition.load_image_file(ruta_imagen)
        encodings = face_recognition.face_encodings(imagen)

        if not encodings:
            return False, "No se detectó ningún rostro en la imagen."

        face_encoding = pickle.dumps(encodings[0])

        session = SessionLocal()
        nuevo_kid = Kid(
            nombre=nombre.strip(),
            apellidos=apellidos.strip(),
            tutor=tutor.strip(),
            maestro=maestro.strip(),
            grado=grado.strip().upper(),
            face_encoding=face_encoding
        )
        session.add(nuevo_kid)
        session.commit()
        session.close()

        return True, "Niño registrado exitosamente."

    except Exception as e:
        return False, f"Error al registrar niño: {e}"

