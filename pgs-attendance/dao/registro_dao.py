from config.database import SessionLocal
from models.registro import Registro
from datetime import datetime

def registrar_entrada(kid_id):
    db = SessionLocal()
    nueva_entrada = Registro(kid_id=kid_id, timestamp=datetime.now())
    db.add(nueva_entrada)
    db.commit()
    db.close()

