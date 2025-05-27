
from POO.biblioteca.items import MaterialBiblioteca, Libro, Revista, Dvd


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materiales = []

    def agregar_material(self, material):
        if not isinstance(material, MaterialBiblioteca):
            raise TypeError("Solo se pueden agregar objetos de tipo MaterialBiblioteca")
        self.materiales.append(material)