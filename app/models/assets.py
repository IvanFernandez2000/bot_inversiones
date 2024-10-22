from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, REAL
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre_usuario = Column(String, nullable=False)
    chat_id = Column(String, nullable=False)
    fecha_registro = Column(DateTime, default=datetime)

    activos = relationship("Activo", back_populates="usuario")


# Modelo de la tabla 'activos'
class Activo(Base):
    __tablename__ = "activos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    ticker = Column(String, nullable=False)
    tipo_activo = Column(String, nullable=False)
    nombre_activo = Column(String, nullable=False)
    ultima_actualizacion = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    precio_actual = Column(REAL, nullable=False)
    cambio_diario = Column(REAL, nullable=False)

    # Relación con la tabla 'usuarios'
    usuario = relationship("Usuario", back_populates="activos")

    # Relación con la tabla 'HistoricoPrecio'
    registros_precios = relationship("HistoricoPrecio", back_populates="activo")

# Modelo de la tabla 'registro_precios'
class HistoricoPrecio(Base):
    __tablename__ = "HistoricoPrecio"

    id = Column(Integer, primary_key=True, autoincrement=True)
    activo_id = Column(Integer, ForeignKey('activos.id'), nullable=False)
    precio = Column(Float, nullable=False)
    fecha = Column(DateTime, default=datetime)

    # Relación con la tabla 'activos'
    activo = relationship("Activo", back_populates="registros_precios")

