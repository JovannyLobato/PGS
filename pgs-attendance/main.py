# app/main.py
from fastapi import FastAPI
from app.routes import router
from app.database import Base, engine

app = FastAPI()
Base.metadata.create_all(bind=engine)
app.include_router(router)
