from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI, DEBUG
from app.models.assets import Base  # Importa Base desde el archivo de modelos

# Configuración del ORM y base de datos
engine = create_engine(DATABASE_URI, echo=True)  # echo=True para ver consultas en consola (modo debug)

# Sesiones para interactuar con la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """Crea las tablas definidas en los modelos si no existen."""
    Base.metadata.create_all(bind=engine)

def get_db():
    """Provee una sesión de base de datos y garantiza su cierre al finalizar."""
    db = SessionLocal()
    try:
        yield db  # Sesión disponible para consultas
    finally:
        db.close()  # Cierra la sesión al terminar