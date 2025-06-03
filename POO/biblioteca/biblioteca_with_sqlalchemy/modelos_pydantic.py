from pydantic import BaseModel
from typing import Optional

class BaseMaterial(BaseModel):
    tipo: str
    titulo: str
    autor: str

class LibroCreate(BaseMaterial):
    paginas: int

class RevistaCreate(BaseMaterial):
    edicion: int
    fecha: str

class DvdCreate(BaseMaterial):
    duracion: int
    formato: str

class UsuarioCreate(BaseModel):
    nombre: str