from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, date
from enum import Enum

class TipoMaterialEnum(str, Enum):
    libro = "libro"
    revista = "revista"
    dvd = "dvd"

class BaseMaterial(BaseModel):
    tipo: TipoMaterialEnum
    titulo: str
    autor: str
    prestado: bool = False

class LibroCreate(BaseMaterial):
    paginas: int

class RevistaCreate(BaseMaterial):
    edicion: int
    fecha: date

class DvdCreate(BaseMaterial):
    duracion: int
    formato: str

class UsuarioCreate(BaseModel):
    nombre: str


class PrestamosRequest(BaseModel):
    id_item: int
    id_usuario: int


class PrestamoUpdate(BaseModel):
    id_prestamo: int
    fecha_limite: Optional[datetime] = None
    devuelto: Optional[bool] = False




class MaterialUpdate(BaseModel):
    tipo: Optional[TipoMaterialEnum]
    titulo: Optional[str] = None
    autor: Optional[str] = None
    prestado: Optional[bool] = None
    codigo_inventario: Optional[str] = None
    num_paginas: Optional[int] = None 
    num_edicion: Optional[int] = None 
    fecha_publicacion: Optional[str] = None 
    duracion: Optional[int] = None
    formato: Optional[str] = None


class ReviewCreate(BaseModel):
    id_item: int
    review: str
    autor: str