import uuid

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.id_usuario = uuid.uuid4().hex[:6].upper()  # Genera un ID único
        self.prestamos = []

    def mostrar_info(self):
        print(f"Usuario: {self.nombre} (ID: {self.id_usuario})")
        print(f"Préstamos actuales: {[mat.titulo for mat in self.prestamos]}")
        
