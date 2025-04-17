from app.core.database import Base, engine
from app.models import user, role, students, guardian, fingerprint, attendance, association

# Crea todas las tablas
print("Creando tablas...")
Base.metadata.create_all(bind=engine)
print("Listo.")

