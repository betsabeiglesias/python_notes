from sqlalchemy import MetaData,Column, Integer, String, Date, Boolean, Enum, ForeignKey, DateTime, Float
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime, timedelta

metadata = MetaData()
Base = declarative_base(metadata=metadata)

class Usuarios_Alchemy(Base):
    __tablename__ = 'usuarios_alchemy'

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(30), nullable=False)

    prestamos = relationship("Prestamo_Alchemy", back_populates="usuario")

class CatalogoBiblioteca(Base):
    __tablename__ = 'catalogo_biblioteca'

    id_material = Column(Integer, primary_key=True, autoincrement=True)
    tipo = Column(Enum('Libro', 'Revista', 'Dvd'), nullable=False)
    titulo = Column(String(255), nullable=False)
    autor = Column(String(255))
    codigo_inventario = Column(String(100), unique=True, nullable=False)
    prestado = Column(Boolean, default=False)

    prestamo = relationship("Prestamo_Alchemy", back_populates="material", uselist=False)



# 💡 Diferencia:
# backref = crea automáticamente el lado inverso de la relación.
# back_populates = requiere definir explícitamente ambos lados, dando más control y claridad.


class Libro(Base):
    __tablename__ = 'libros_alchemy'

    id_material = Column(Integer, ForeignKey('catalogo_biblioteca.id_material', ondelete='CASCADE'), primary_key=True)
    num_paginas = Column(Integer, nullable=False)

    catalogo = relationship("CatalogoBiblioteca", backref="libro")


class Revista(Base):
    __tablename__ = 'revistas_alchemy'

    id_material = Column(Integer, ForeignKey('catalogo_biblioteca.id_material', ondelete='CASCADE'), primary_key=True)
    num_edicion = Column(Integer, nullable=False)
    fecha_publicacion = Column(Date, nullable=False)

    catalogo = relationship("CatalogoBiblioteca", backref="revista")


class DVD(Base):
    __tablename__ = 'dvds_alchemy'

    id_material = Column(Integer, ForeignKey('catalogo_biblioteca.id_material', ondelete='CASCADE'), primary_key=True)
    duracion = Column(Float, nullable=False)
    formato = Column(String(50), nullable=False)

    catalogo = relationship("CatalogoBiblioteca", backref="dvd")


class Prestamo_Alchemy(Base):
    __tablename__ = 'prestamos_alchemy'

    id_prestamo = Column(Integer, primary_key=True, autoincrement=True)

    id_usuario = Column(Integer, ForeignKey('usuarios_alchemy.id'), nullable=False)
    id_material = Column(Integer, ForeignKey('catalogo_biblioteca.id_material'), nullable=False)

    fecha_prestamo = Column(DateTime, default=datetime.now())
    fecha_limite = Column(DateTime, default=lambda: datetime.now() + timedelta(days=14))
    fecha_devolucion = Column(DateTime, nullable=True)

    # Relaciones bidireccionales
    usuario = relationship("Usuarios_Alchemy", back_populates="prestamos")
    material = relationship("CatalogoBiblioteca", back_populates="prestamo")
