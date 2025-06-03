from abc import ABC, abstractmethod
import datetime
import uuid

class MaterialBiblioteca (ABC):
    def __init__(self, titulo, autor, codigo_inventario):
        self.titulo = titulo
        self.autor = autor
        self.codigo_inventario = uuid.uuid4().hex[:6].upper()
        self.prestado = False

    @abstractmethod
    def mostrar_info(self):
        print(f"titulo: {self.titulo} - Autor: {self.autor} - Código: {self.codigo_inventario}")

    def prestar(self):
        print(f"Se ha prestado el titulo {self.titulo} ({self.__class__.__name__})")
        self.prestado = True

    def devolver(self):
        print(f"Se ha devuelto el titulo {self.titulo} ({self.__class__.__name__})")
        self.prestado = False

    def mostrar_info(self):
        print(f"--- Información del {self.__class__.__name__} ---")
        print(f"titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Código de inventario: {self.codigo_inventario}")
        print(f"Prestado: {self.prestado}")


class Libro(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo_inventario, num_paginas):
        super().__init__(titulo, autor, codigo_inventario)
        self.tipo = "libro"
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
        super().mostrar_info()
        print(f"Número de páginas: {self.num_paginas}")
    



class Revista(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo_inventario, num_edicion, fecha_publicacion):
        super().__init__(titulo, autor, codigo_inventario)
        self.tipo = "revista"
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
        super().mostrar_info()
        print(f"Número de edición: {self.num_edicion}")
        print(f"Fecha de publicación: {self.fecha_publicacion.strftime('%d/%m/%Y')}")


class Dvd(MaterialBiblioteca):
    def __init__(self, titulo, autor, codigo_inventario, duracion, formato):
        super().__init__(titulo, autor, codigo_inventario)
        self.tipo = "dvd"
        self.duracion = duracion
        self.formato = formato
    
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
        super().mostrar_info()
        print(f"Duración: {self.duracion} minutos")
        print(f"Formato: {self.formato}")

   





# libro = Libro("El Hobbit", "J.R.R. Tolkien", "L001", 310)
# libro.mostrar_info()
# libro.prestar()
# libro.devolver()

# revista = Revista("National Geographic", "Varios", "R100", 5, "15/03/2024")
# revista.mostrar_info()
# revista.prestar()
# revista.devolver()

# dvd = Dvd("Interstellar", "Christopher Nolan", "D777", 169, "Blu-ray")
# dvd.mostrar_info()
# dvd.prestar()
# dvd.devolver()
          