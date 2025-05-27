#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:46:48 2023

@author: laptop
"""

############
# Herencia #
############
"""
La Herencia permite definir clases con características derivadas de otras que 
no necesitan definirse en las clases herederas. Aunque pueden sobreescribirse.
"""
#----------------------------
# Clase padre (o superclase)
#----------------------------
class Mamifero:
    def __init__(self, comestible):
        self.patas = 4
        self.cola = True
        self.comestible = comestible

    # Los métodos correr y saltar son heredables por cualquier mamífero
    def correr(self):
        print("Este animal corre")

    def saltar(self):
        print("Este animal salta")
    
    def me_lo_como(self):
        if self.comestible:
            print("Te has comido un mamífero")
        else:
            print("No puedes comerte este animal")    

#---------------------------
# Clases hijo (o subclases)
#---------------------------
class Animal_de_granja(Mamifero):
    def __init__(self, comestible):
        self.patas = 4
        self.cola = True
        self.comestible = comestible
        self.en_choza = False

    # Hay dos métodos nuevos que permiten modificar un atributo que no existía en la superclase
    # Los heredarán las subclases
    def guardar_en_choza(self):
        self.en_choza = True

    def sacar_de_choza(self):
        self.en_choza = False

    def me_lo_como(self):
        if self.comestible:
            print("Te has comido un animal de granja")
        else:
            print("No puedes comerte este animal")


class Animal_domestico(Animal_de_granja):
    def __init__(self, nombre):
        self.nombre = nombre
        self.patas = 4
        self.cola = True
        self.comestible = False
        self.en_choza = False
        self.en_casa = False

    # Hay dos métodos nuevos que permiten modificar un atributo que no existía en la superclase
    def guardar_en_casa(self):
        self.en_casa = True

    def sacar_de_casa(self):
        self.en_casa = False

    def me_lo_como(self):
        print(f"No te puedes comer a {self.nombre}")
        raise NotImplementedError("Este método no está disponible en la subclase")


ciervo = Mamifero(comestible = True)
ciervo.comestible
ciervo.correr()
# El ciervo no se puede meter en una choza
ciervo.guardar_en_choza()
ciervo.me_lo_como()

raton = Mamifero(comestible = False)
raton.correr()
raton.saltar()
raton.me_lo_como()

cerdo = Animal_de_granja(comestible = True)
cerdo.comestible
cerdo.correr()
cerdo.cola

cerdo.en_choza
cerdo.guardar_en_choza()
cerdo.en_choza
cerdo.sacar_de_choza()
cerdo.en_choza

cerdo.guadar_en_casa()

cerdo.me_lo_como()

burro = Animal_de_granja(comestible = False)
burro.me_lo_como()

perro = Animal_domestico("Lassie")
perro.patas
# Este atributo no tiene un método que lo modifique
perro.comestible
perro.nombre

# Los métodos heredados siguen funcionando
perro.en_choza
perro.guardar_en_choza()
perro.en_choza
perro.sacar_de_choza()
perro.en_choza

perro.correr()
perro.saltar()

# Y además tieme métodos nuevos
perro.en_casa
perro.guardar_en_casa()
perro.en_casa
perro.sacar_de_casa()
perro.en_casa

perro.me_lo_como()


# ____________________________________________________
# Para no tener que reescribir la funcion __init__

class Mamifero:
    def __init__(self, comestible):
        self.patas = 4
        self.cola = True
        self.comestible = comestible

    # Los métodos correr y saltar son heredables por cualquier mamífero
    def correr(self):
        print("Este animal corre")

    def saltar(self):
        print("Este animal salta")
    
    def me_lo_como(self):
        if self.comestible:
            print("Te has comido un mamífero")
        else:
            print("No puedes comerte este animal")    


class Animal_de_granja(Mamifero):
    def __init__(self, comestible):
        super().__init__(comestible)  # Llamamos al constructor de la clase padre
        self.en_choza = False  # Agregamos el atributo adicional

    def guardar_en_choza(self):
        self.en_choza = True

    def sacar_de_choza(self):
        self.en_choza = False

    def me_lo_como(self):
        if self.comestible:
            print("Te has comido un animal de granja")
        else:
            print("No puedes comerte este animal")


class Animal_domestico(Animal_de_granja):
    def __init__(self, nombre):
        super().__init__(False)  # Llamamos al constructor de la clase padre
        self.nombre = nombre
        self.en_casa = False
        self.patas = 3

    def guardar_en_casa(self):
        self.en_casa = True

    def sacar_de_casa(self):
        self.en_casa = False

    def me_lo_como(self):
        print(f"No te puedes comer a {self.nombre}")
        raise NotImplementedError("Este método no está disponible en la subclase")


# Los objetos son instancias de su clase y de las clases de las que hereda su clase
isinstance(perro, Animal_domestico)
isinstance(perro, Animal_de_granja)
isinstance(perro, Mamifero)

isinstance(cerdo, Animal_domestico)
isinstance(cerdo, Animal_de_granja)
isinstance(cerdo, Mamifero)

isinstance(ciervo, Animal_domestico)
isinstance(ciervo, Animal_de_granja)
isinstance(ciervo, Mamifero)

issubclass(Animal_domestico, Animal_de_granja)
issubclass(Animal_de_granja, Mamifero)
issubclass(Animal_domestico, Mamifero)

#############
# Ejercicio #
#___________#
# Si transferimos a nuestra aplicacion de personal, puedo crear la clase empleado
# y a partir de ella crear clases herederas según cargo.


# Las clases "hijo" serán Directivo, Oficinista, Peon

# El directivo, tiene coche de empresa, y métodos asociados a él.
# El oficinista tiene bonuses
# El peón tiene guardias... etc


from POO.empleado_class import Empleado
from POO.coche_class import Coche
import time

class Directivo(Empleado):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=10):
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        self.coche_empresa = None
        self.gasolina = 0




class Oficinista(Empleado):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=10):
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        self.bonus = 0

    def calcula_sueldo(self):
        sueldo_base = super().calcula_sueldo()
        sueldo_con_bonus = sueldo_base + self.bonus
        print (f"Sueldo con bonus: {sueldo_con_bonus}")
        return sueldo_con_bonus
    


class Peon(Empleado):
    def __init__(self, nombre, apellido1, apellido2, sueldo_hora=10):
        super().__init__(nombre, apellido1, apellido2, sueldo_hora)
        self.guardias = 0

    def cuenta_guardias(self):
        hora_limite = datetime.time(21,0)
        guardias_contadas = 0
        entradas = self.fichajes[::2]
        for entrada in entradas:
            if entrada.time() > hora_limite:
                guardias_contadas += 1
        self.guardias = guardias_contadas
        print(f"Las guardias son:{self.guardias}")
    
    def ficha(self):
        super().ficha()
        self.cuenta_guardias()

    def calcula_sueldo(self):
        sueldo_base = super().calcula_sueldo()
        if self.guardias:
            sueldo_total = sueldo_base + (self.guardias * 7000)
            print (f"El sueldo con guardias es: {sueldo_total}")
        else: print("El sueldo NO tiene guardias")
        return sueldo_total



jefe = Directivo("Juan", "Pérez", "López")
print(f"Directivo: {jefe.nombre} {jefe.apellido1} {jefe.apellido2}")
jefe.coche_empresa = Coche("Seat", "Leon", 4.5, 30000)
jefe.gasolina = 300
jefe.coche_empresa.presentarse()
jefe.gasolina


oficinista = Oficinista("Ana", "García", "Martínez")
oficinista.presentarse()
oficinista.ficha()
oficinista.bonus = 5000
oficinista.ficha()
oficinista.calcula_sueldo()

peon = Peon("Luis", "González", "Martínez")
peon.presentarse()
peon.ficha()
peon.cuenta_guardias()

#/***** SCRIPT PRUEBA OFICINISTA *****/
print(__name__)
if __name__ == "__main__":
    # Crear un oficinista
    oficinista = Oficinista("Ana", "García", "Martínez")
    
    # Mostrar presentación
    oficinista.presentarse()
    
    # Simular fichajes (entrada y salida)
    print("Fichando entrada...")
    oficinista.ficha()
    oficinista.bonus = 5000
    time.sleep(1)  # espera 1 segundo para simular tiempo trabajado
    print("Fichando salida...")
    oficinista.ficha()
    
    # Calcular sueldo con bonus
    oficinista.calcula_sueldo()


#/***** SCRIPT PRUEBA PEÓN *****/
import datetime
if __name__ == "__main__":
    peon = Peon("Luis", "Fernández", "Ruiz")
    peon.presentarse()

    # Simular fichaje temprano (antes de las 21h)
    print("\nFichaje temprano:")
    peon.ficha()
    peon.fichajes[-1] = peon.fichajes[-1].replace(hour=20)  # forzar hora
    peon.ficha()
    peon.fichajes[-1] = peon.fichajes[-1].replace(hour=20)  # salida
    
    # Simular fichaje tarde (después de las 21h)
    print("\nFichaje tarde (guardia):")
    peon.ficha()
    peon.fichajes[-1] = peon.fichajes[-1].replace(hour=22)  # forzar hora
    peon.ficha()
    peon.fichajes[-1] = peon.fichajes[-1].replace(hour=23)  # salida

    # Simular otro fichaje tarde
    print("\nOtro fichaje tarde (guardia):")
    peon.ficha()
    peon.fichajes[-1] = peon.fichajes[-1].replace(hour=22)  # forzar hora
    peon.ficha()
    peon.fichajes[-1] = peon.fichajes[-1].replace(hour=23)  # salida

    # Calcular sueldo final
    print("\n=== SUELDO FINAL ===")
    peon.calcula_sueldo()