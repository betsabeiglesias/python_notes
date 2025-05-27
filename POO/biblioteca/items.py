from abc import ABC, abstractmethod
import datetime

class MaterialBiblioteca (ABC):
    def __init__(self, titulo, autor, codigo_inventario):
        self.titulo = titulo
        self.autor = autor
        self.codigo_inventario = codigo_inventario

    @abstractmethod
    def mostrar_info(self):
        print(f"Título: {self.titulo} - Autor: {self.autor} - Código: {self.codigo_inventario}")



class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo_inventario, num_paginas):
        super().__init__(titulo, autor, codigo_inventario)
        self.num_paginas = num_paginas #esto usa el setter

    @property
    def num_paginas(self):
        return self.__num_paginas
    
    @num_paginas.setter
    def num_paginas(self, valor):
        if valor <= 0:
            raise ValueError ("Un libro sin páginas no es un libro")
        else: self.__num_paginas = valor
    
    def mostrar_info(self):
        print(f"--- Información del {self.__class__.__name__} ---")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Código de inventario: {self.codigo_inventario}")
        print(f"Número de páginas: {self.num_paginas}")



class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo_inventario, num_edicion, fecha_publicacion):
        super().__init__(titulo, autor, codigo_inventario)
        self.num_edicion = 0
        self.fecha_publicacion = fecha_publicacion

    @property
    def num_edicion(self):
        return self.__num_edicion
    
    @num_edicion.setter
    def num_edicion(self, num):
        if num < 0:
            raise ValueError ("El número de edición no puede ser negativo")
        else: self.__num_edicion = num
        
    @property
    def fecha_publicacion(self):    
        return self.__fecha_publicacion
    
    @fecha_publicacion.setter
    def fecha_publicacion(self, fecha):
        if isinstance(fecha, str):
            try:
                fecha = datetime.datetime.strptime(fecha, "%d/%m/%Y").date()
            except ValueError:
                raise ValueError("El string de fecha debe estar en formato 'dd/mm/yyyy'")
        elif not isinstance(fecha, datetime.date):
            raise TypeError("La fecha tiene que ser un string 'dd/mm/yyyy' o un objeto datetime.date")
        if fecha >= datetime.date.today():
            raise ValueError("La fecha de publicación tiene que ser anterior a hoy")
        self.__fecha_publicacion = fecha

    def mostrar_info(self):
        print(f"--- Información de la {self.__class__.__name__} ---")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Código de inventario: {self.codigo_inventario}")
        print(f"Número de edición: {self.num_edicion}")
        print(f"Fecha de publicación: {self.fecha_publicacion.strftime('%d/%m/%Y')}")


class Dvd(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo_inventario):
        super().__init__(titulo, autor, codigo_inventario)
        self.duracion = None
        self.formato = None
    
    @property
    def duracion(self):
        return self.__duracion

    @duracion.setter
    def duracion(self, valor):
        if not isinstance(valor, (int, float)) or valor <= 0:
            raise ValueError("La duración debe ser un número positivo (minutos).")
        self.__duracion = valor

    @property
    def formato(self):
        return self.__formato

    @formato.setter
    def formato(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("El formato debe ser una cadena no vacía.")
        self.__formato = valor.strip()

    def mostrar_info(self):
        print(f"--- Información del {self.__class__.__name__} ---")
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Código de inventario: {self.codigo_inventario}")
        print(f"Duración: {self.duracion} minutos")
        print(f"Formato: {self.formato}")





libro = Libro("titulo","autor", "codigo", 10)
libro.mostrar_info()


revista = Revista("revista", "varios", "codigorevista", "1", "26/05/2025")
revista.mostrar_info()