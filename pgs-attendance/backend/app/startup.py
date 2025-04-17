from fastapi import FastAPI
from app.api import students
from app.core.database import Base, engine

# Crea tablas si no existen
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Incluir las rutas
app.include_router(students.router)

