# -*- coding: utf-8 -*-
"""
Created on Fri Mar  2 10:03:25 2023

@author: Aitor Donado.
"""

#########################
#          CSV          #
#########################

import json
import csv

# _____________________________
# Escritura de listas en CSV
contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

with open("datos/contactos.csv", "w", newline="\n") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    for contacto in contactos:
        writer.writerow(contacto)

# _____________________________
# Lectura de listas en CSV

with open("datos/contactos.csv", newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for nombre, empleo, email in reader:
        print(nombre, empleo, email)

with open("datos/contactos.csv", newline="\n") as csvfile:
    reader = csv.reader(csvfile, delimiter=",")
    for linea in reader:
        print(linea)


# _____________________________
# Escritura de diccionarios en CSV

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

with open("datos/contactos.csv", "w", newline="\n") as csvfile:
    campos = ["nombre", "empleo", "email"]
    writer = csv.DictWriter(csvfile, fieldnames=campos)
    writer.writeheader()
    for nombre, empleo, email in contactos:
        writer.writerow({
            "nombre": nombre, "empleo": empleo, "email": email
        })


# _____________________________
# Lectura de diccionarios en CSV

with open("datos/contactos.csv", newline="\n") as csvfile:
    reader = csv.DictReader(csvfile)
    for contacto in reader:
        print(contacto["nombre"], contacto["empleo"], contacto["email"])



#########################
#          JSON         #
#########################

# _____________________________
# Escritura de datos en JSON

contactos = [
    ("Manuel", "Desarrollador Web", "manuel@ejemplo.com"),
    ("Lorena", "Gestora de proyectos", "lorena@ejemplo.com"),
    ("Javier", "Analista de datos", "javier@ejemplo.com"),
    ("Marta", "Experta en Python", "marta@ejemplo.com")
]

datos = []

for nombre, empleo, email in contactos:
    datos.append({"nombre": nombre, "empleo": empleo, "email": email})

with open("datos/contactos.json", "w") as jsonfile:
    json.dump(datos, jsonfile)

# _____________________________
# Lectura de datos en JSON

with open("datos/contactos.json") as jsonfile:
    datos = json.load(jsonfile)
    for contacto in datos:
        print(contacto["nombre"], contacto["empleo"], contacto["email"])


#############################################
# Ejercicio

with open("datos/NotasMod1.csv", newline="\n") as csvfile:
    reader = csv.DictReader(csvfile)
    for alumno in reader:
        print(alumno["Nombre"], alumno["Apellidos"], alumno["Email"])
