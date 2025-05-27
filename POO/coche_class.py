
class Coche:

    def __init__(self, marca, modelo, longitud, precio):
        self.marca = marca
        self.modelo = modelo
        self.longitud = longitud
        self.precio = precio
    
    def __del__(self):
        print(f"Se ha borrado {self.marca} {self.modelo}")

    def __str__(self):
         return f"Coche: {self.marca} {self.modelo}, Longitud: {self.longitud}m, Precio: {self.precio}€"
    
    def __len__(self):
        return int(self.longitud) * 100 
    
    
    def __eq__(self, other):
        return self.precio == other.precio


    def __lt__(self, other):
        return self.precio < other.precio
    
    def __gt__(self, other):
        return int(self.precio) > int(other.precio)
    
    def presentarse(self):
        print(f"Hola soy el coche {self.marca} {self.modelo} mido {self.longitud} y cuesto {self.precio}")
