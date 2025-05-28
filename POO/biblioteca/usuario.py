class Usuario():
    def __init__(self, id, nombre):
        self.nombre = nombre
        self.id = id
        self.prestamos = []

    def mostrar_info(self):
        print(f"Usuario: {self.nombre} (ID: {self.id})")
        print(f"Préstamos actuales: {[mat.titulo for mat in self.prestamos]}")
        
