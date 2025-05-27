
from POO.biblioteca.items import MaterialBiblioteca, Libro, Revista, Dvd


class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materiales = []

    