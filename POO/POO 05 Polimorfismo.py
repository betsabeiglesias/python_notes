#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:46:48 2023

@author: laptop
"""

################
# Polimorfismo #
################
class Mamifero:
    def __init__(self, nombre):
        self.nombre = nombre
        self.patas = 4
        self.cola = True

    def hablar(self):
        pass


class Perro(Mamifero):
    def hablar(self):
        print('¡Guau!')


class Gato(Mamifero):
    def hablar(self):
        print('¡Miau!')


class Cerdo(Mamifero):
    def hablar(self):
        print('¡Oink!')

# No es necesario que se herede la función
class Gallo():
    def __init__(self, nombre):
        self.nombre = nombre
        self.patas = 2
        self.alas = True

    def hablar(self):
        print("¡Kikiriki!")

lassie = Perro('Lassie')
pluto = Perro("Pluto")

garfield = Gato('Garfield')
don_gato = Gato('Don Gato')

porky = Cerdo('Porky')

claudio = Gallo("Claudio")
# Esto es el polimorfismo. Podemos crear comportamientos ligeramente distintos
# a una misma función dependiendo de la clase

lassie.patas
porky.patas
claudio.patas

lassie.hablar()
garfield.hablar()
porky.hablar()
claudio.hablar()

# Y me permite no tener que comprobar el tipo de un objeto a la hora de usar un método.
def dime_algo(objeto):
    objeto.hablar()

dime_algo(lassie)
dime_algo(garfield)
dime_algo(porky)
dime_algo(claudio)

lista_animales = [lassie, porky, claudio]
for animal in lista_animales:
    animal.hablar()


#############
# Ejercicio #
#___________#

# Reutilizamos el código que hemos visto en herencia.
# Vamos a crear una función/método que se llame en_activo que se ejecuta cuando el empleado ficha
# Lo único que hará será imprimir strings de una lista de actividades (4 como mucho) cada 3 segundos
# A pesar de que se llama igual, veremos distintos mensajes en función de la clase de la instancia

