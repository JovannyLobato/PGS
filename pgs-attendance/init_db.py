import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import face_recognition
import pickle
from config.database import engine, SessionLocal, Base
from models.kid import Kid
from models.teacher import Teacher
from models.parent import Parent
from models.registro import Registro

# Crear las tablas
Base.metadata.create_all(bind=engine)

# Función auxiliar para obtener el encoding facial
def obtener_face_encoding(ruta_imagen):
    imagen = face_recognition.load_image_file(ruta_imagen)
    encodings = face_recognition.face_encodings(imagen)
    if encodings:
        return pickle.dumps(encodings[0])  # Convertir a binario
    return None

# Insertar datos de ejemplo
session = SessionLocal()

kid1 = Kid(
    nombre="Jovany",
    apellidos="Lobato Merenguez",
    tutor="Fernando",
    maestro="Maestra Ejemplo",
    grado="3A",
    face_encoding=obtener_face_encoding("kids_faces/Jovany Lobato Merenguez.jpg")
)

kid2 = Kid(
    nombre="Aurora",
    apellidos="Aksnes",
    tutor="Padre X",
    maestro="Maestra Y",
    grado="3B",
    face_encoding=obtener_face_encoding("kids_faces/Aurora Aksnes.jpeg")
)


teacher = Teacher(name="Guadalupe Elizabeth Camarena Castro")
parent = Parent(name="Fernando Fernández Hernández")

session.add_all([kid1, kid2, teacher, parent])
session.commit()
session.close()

print("Base de datos inicializada con datos de ejemplo.")

