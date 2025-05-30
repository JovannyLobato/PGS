from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker


# En psql creen una bd llamada  'pgs', con un usuario llamado 'admon' y 'password123' como contrasenia
DATABASE_URL = "postgresql+psycopg2://admon:password123@localhost/pgs"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
Base = declarative_base()

