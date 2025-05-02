from config.database import engine, SessionLocal, Base
from models.kid import Kid
from models.teacher import Teacher
from models.parent import Parent
from models.registro import Registro

from controllers.registro_controller import process_fingerprint

# Crear las tablas
Base.metadata.create_all(bind=engine)

# Insertar datos de ejemplo
session = SessionLocal()

kid1 = Kid(name="Juan Pérez Gomez", fingerprint_hash=process_fingerprint("abc123"))
kid2 = Kid(name="Ana López Herrera", fingerprint_hash=process_fingerprint("def456"))

teacher = Teacher(name="Guadalupe Elizabeth Camarena Castro")
parent = Parent(name="Fernando Fernández Hernández")

session.add_all([kid1, kid2, teacher, parent])
session.commit()
session.close()

print("Base de datos inicializada con datos de ejemplo.")

