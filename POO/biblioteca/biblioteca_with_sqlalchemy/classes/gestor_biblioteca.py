
from classes.items import MaterialBiblioteca, Libro, Revista, Dvd
import pickle
from classes.usuario import Usuario
from classes.db import Gestor_BBDD

class Gestor:
    def __init__(self, nombre):
        self.nombre = nombre
        self.materiales = []
        self.usuarios = []
        self.db = Gestor_BBDD()

    # def conectar_base(self):
    #     self.db.conectar_db()

    # def desconectar_base(self):
    #     self.db.


    def agregar_material(self, material, filename="materiales.pkl"):
        if not isinstance(material, MaterialBiblioteca):
            raise TypeError("Solo se pueden agregar objetos de tipo MaterialBiblioteca")
        for mat in self.materiales:
            if mat.codigo_inventario == material.codigo_inventario:
                raise ValueError ("Ya existe un elemento con eses código de inventario")
        #if any(mat.codigo_inventario == material.codigo_inventario for mat in self.materiales):
        self.materiales.append(material)
        self.guardar_materiales_pickle(filename)
        return material


        

    def __str__(self):
        return (f"La Biblioteca: {self.nombre}\nTiene {len(self.materiales)} elementos")
    
    def listar_elementos(self):
        for i, mat in enumerate(self.materiales, start = 1):
            print (f"{i}: ") 
            mat.mostrar_info()

    def mostar_elemento(self, index):
        if index < 1 or index > len(self.materiales):
            return ("El elemento seleccionado no existe")
        mat = self.materiales[index - 1]
        mat.mostrar_info()

    def mostrar_elemento_codigo(self, cod):
        for mat in self.materiales:
            if mat.codigo_inventario == cod:
                return mat.mostar_info()
        print ("No se encontró el código")

    def borrar_elemento_codigo(self, cod):
        for i, mat in enumerate(self.materiales):
            if mat.codigo_inventario == cod:
                print(f"Eliminado {mat.titulo.upper()} ...")
                self.materiales.pop(i)
                return
        print ("No se encontró el código")

   

       
    def mostrar_libros(self):
        for mat in self.materiales:
            if isinstance(mat, Libro):
                print(f"- {mat.titulo} (Código {mat.codigo_inventario})")
        # con listas de comprensión
        # libros = [mat.titulo for mat in self.materiales if isinstance(mat, Libro)]
        # for titulo in libros:
        #     print(titulo)

    def mostrar_revistas (self):
        for mat in self.materiales:
            if isinstance(mat, Revista):
                print(f"- {mat.titulo} (Código {mat.codigo_inventario})")
    
    def mostrar_dvd(self):
        for mat in self.materiales:
            if isinstance(mat, Dvd):
                print(f"- {mat.titulo} (Código {mat.codigo_inventario})")

    def pedir_y_agregar_material(self):
        tipo = input("¿Qué tipo de material quieres agregar? (libro/revista/dvd): ").strip().lower()
        titulo = input("Título: ")
        autor = input("Autor: ")
        if tipo == "libro":
            paginas = int(input("Número de páginas: "))
            nuevo = Libro(titulo, autor, codigo, paginas)
        elif tipo == "revista":
            edicion = int(input("Número de edición: "))
            fecha = input("Fecha de publicación (dd/mm/yyyy): ")
            nuevo = Revista(titulo, autor, codigo, edicion, fecha)
        elif tipo == "dvd":
            duracion = float(input("Duración (minutos): "))
            formato = input("Formato: ")
            nuevo = Dvd(titulo, autor, codigo, duracion, formato)
        else:
            print("Tipo no válido. Cancela operación.")
            return
        # self.agregar_material(nuevo)
        # print(f"Material '{titulo}' agregado correctamente.")
        return nuevo

        
    def guardar_materiales_pickle(self, filename="../../materiales.pkl"):
        with open(filename, "wb") as f:
            pickle.dump(self.materiales, f)

    def cargar_materiales_pickle(self, filename="../../materiales.pkl"):
        try:
            with open(filename, "rb") as f:
                self.materiales = pickle.load(f)
        except FileNotFoundError:
            print(f"No se ha encontrado archivo {filename}, se inicializa lista vacía.")
            self.materiales = []
    
    def guardar_usuarios_pickle(self, filename="usuarios.pkl"):
        with open(filename, "wb") as f:
                pickle.dump(self.usuarios, f)
        # except FileNotFoundError:
        #     print(f"No se ha encontrado archivo {filename}, se inicializa lista vacía.")
        #     self.usuarios = []

    def cargar_usuarios_pickle(self, filename="usuarios.pkl"):
        try:
            with open(filename, "rb") as f:
                self.usuarios = pickle.load(f)
        except FileNotFoundError:
            print(f"No se ha encontrado archivo {filename}, se inicializa lista vacía.")
            self.usuarios = []
     
     


# if __name__ == "__main__":
#     biblio = Gestor("Central")

#     libro1 = Libro("El Hobbit", "J.R.R. Tolkien", "L001", 310)
#     libro1.mostrar_info()
#     libro1.prestar()
#     libro1.devolver()
#     libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "L002", 417)
#     libro3 = Libro("1984", "George Orwell", "L003", 328)
#     libro4 = Libro("Fahrenheit 451", "Ray Bradbury", "L004", 249)
#     libro5 = Libro("Orgullo y Prejuicio", "Jane Austen", "L005", 279)

#     revista = Revista("National Geographic", "Varios", "R100", 5, "15/03/2024")
#     revista.mostrar_info()
#     revista.prestar()
#     revista.devolver()

#     dvd = Dvd("Interstellar", "Christopher Nolan", "D777", 169, "Blu-ray")
#     dvd.mostrar_info()
#     dvd.prestar()
#     dvd.devolver()
            
            
#     biblio.agregar_material(libro1)
#     biblio.agregar_material(libro2)
#     biblio.agregar_material(libro3)
#     biblio.agregar_material(libro4)
#     biblio.agregar_material(libro5)
#     biblio.agregar_material(revista)
#     biblio.agregar_material(dvd)

#     print(biblio)
#     biblio.listar_elementos()

#     biblio.mostrar_libros()

