from config.database import engine, SessionLocal, Base
from models.kid import Kid
from models.teacher import Teacher
from models.parent import Parent
from models.registro import Registro

# Crear las tablas
Base.metadata.create_all(bind=engine)

# Insertar datos de ejemplo
session = SessionLocal()

kid1 = Kid(name="Juan Pérez", fingerprint_hash="abc123")
kid2 = Kid(name="Ana López", fingerprint_hash="def456")

teacher = Teacher(name="Maestra Luz")
parent = Parent(name="Señor Pérez")

session.add_all([kid1, kid2, teacher, parent])
session.commit()
session.close()

print("Base de datos inicializada con datos de ejemplo.")

