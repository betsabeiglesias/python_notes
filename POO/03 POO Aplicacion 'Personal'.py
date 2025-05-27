#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 17:46:48 2023

@author: laptop
"""

####################################
# Programación Orientada a Objetos #
####################################
# Creamos una aplicación para gestionar el "Personal" de una empresa

import datetime

#----------------------------------
# Etapa1: Creo una clase "Persona"
#----------------------------------

class Persona:
    def __init__(self, nombre, apellido1, apellido2):
        # Características
        self.nombre = nombre
        self.apellido1 = apellido1
        self.apellido2 = apellido2
        self.sueldo_hora = 10
        # Estados
        self.trabajando = False
        self.ubicacion = "Rentería"
        self.fichajes = {"entrada": [], "salida": []}

    # Los métodos son funciones con "self"
    def presentarse(self):
        print(
            f'Hola, mi nombre es {self.nombre} {self.apellido1} {self.apellido2}')

    def ficha(self):
        print("Biip, Biiiiip")
        ahora = datetime.datetime.now()
        # self.trabajando = not self.trabajando
        if not self.trabajando:
            print(f"[{self.nombre}] Hora de entrada: {ahora}")
            self.fichajes["entrada"].append(ahora)
            self.trabajando = True
        else:
            print(f"[{self.nombre}] Hora de salida: {ahora}")
            self.fichajes["salida"].append(ahora)
            self.trabajando = False

    def viaja(self, nueva_ubicacion):
        print(f"{self.ubicacion} -----> {nueva_ubicacion}")
        self.ubicacion = nueva_ubicacion

    # def registrofichajes(self):
    #     if self.ficha and not self.trabajando: 
    #         return print(f"hora de entrada: {datetime.datetime.now()}")
    #     if self.ficha and self.trabajando:
    #         return print(f"hora de salida: {datetime.datetime.now()}")

    def tiempo_trabajado(self):
        total = datetime.timedelta()
        for i, entrada in enumerate(self.fichajes["entrada"]):
            if i < len(self.fichajes["salida"]):
                salida = self.fichajes["salida"][i]
                duracion = salida - entrada
                total += duracion
        print(f"Tiempo trabajado por {self.nombre}: {total}")
        return total

    def sueldo(self):
        tiempo = self.tiempo_trabajado()
        horas = tiempo.total_seconds() / 3600
        sueldo = round(horas * self.sueldo_hora, 2)
        dietas = 1 * self.dieta()
        total = sueldo + dietas       
        return total
    
    def dieta(self):
        entradas = len(self.fichajes["entrada"])
        return int(entradas)
                

director = Persona('Juan', 'Pérez', 'López')
secretario = Persona('Juanito', 'Pérez', 'García')

print(type(director))
print(type(secretario))

director.presentarse()
secretario.presentarse()

director.trabajando
print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")

secretario.ficha()
director.registrofichajes()
secretario.registrofichajes()

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Dónde está el director? {director.ubicacion}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
print(f"¿Dónde está el secretario? {secretario.ubicacion}")

director.viaja("Albacete")
director.ubicacion

print(f"¿Está trabajando {director.nombre}? {director.trabajando}")
print(f"¿Dónde está el director? {director.ubicacion}")
print(f"¿Está trabajando {secretario.nombre}? {secretario.trabajando}")
print(f"¿Dónde está el secretario? {secretario.ubicacion}")


#----------------------------------------------------------
# Etapa1: Vamos a llevar una contabilidad de los fichajes
#----------------------------------------------------------

director.ficha()
director.fichajes
secretario.ficha()
secretario.fichajes



print (f"Funciona {director.registrofichajes()}")

#----------------------------------------------------------
# Etapa2: Vamos a llevar una contabilidad del tiempo trabajado
#----------------------------------------------------------

director.tiempo_trabajado()
secretario.tiempo_trabajado()


#----------------------------------------------------------
# Etapa2: Vamos a llevar una contabilidad del sueldo acumulado
#----------------------------------------------------------

director.sueldo()
secretario.sueldo()


# Crear un método que asigne una dieta de transporte de un euro cada vez que una persona fiche

director.dieta()


# Modificar el método que calcula el sueldo para que añada la dieta de transporte.
