from classes.items import MaterialBiblioteca
from classes.usuario import Usuario
import datetime

class Prestamo:
    def __init__(self, id_material, id_usuario):
        self.id_material = id_material
        self.id_usuario = id_usuario
        self.fecha_prestamo = datetime.now()
        self.fecha_devolucion = datetime.now() + datetime.timedelta(day=14)
    
    
    def mostrar_info(self):
        print (f"El código {self.codigo} lo tienen el usuario {self.usuario}")


