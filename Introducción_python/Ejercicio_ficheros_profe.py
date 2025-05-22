# Ejercicios Ficheros

"""Recuerda marcar como directorio de trabajo el script donde estés ejecutando el fichero. 
También puedes crear una subcarpeta “archivos” donde meter todos los ficheros, para ello 
puedes usar rutas relativas: "./archivos/nombre_archivo.txt"
"""

# Ejercicio 1: Leer un fichero de texto
"""
Objetivo: Crea un script que lea el contenido de un fichero llamado poema.txt y muestre su contenido en la consola.
Abre el fichero en modo lectura ("r").
Lee todo el contenido del fichero.
Muestra el contenido en pantalla.
Pistas:
Usa la función open() para abrir el fichero.
Usa el método .read() para leer todo el contenido de una sola vez."""

fichero = open("datos/poema.txt", "r", encoding="utf-8")
contenido = fichero.read()
fichero.close() # Cierra el fichero manualmente
print(contenido)

# Alternativa usando with, que cierra el fichero automáticamente
with open("datos/poema.txt", "r", encoding="utf-8") as fichero:
    contenido = fichero.read()
    print(contenido)
    # Cierra el fichero automáticamente al salir del bloque with

#Ejercicio 2: Escribir en un fichero de texto
"""
Objetivo: Crea un script que escriba un mensaje en un fichero llamado notas.txt.
Abre el fichero en modo escritura ("w").
Si el fichero no existe, debe crearse automáticamente.
Escribe en el fichero: "Esta es mi primera nota en este archivo."
Pistas:
Recuerda que el modo "w" sobrescribe el contenido si el fichero ya existe.
Usa el método .write() para escribir en el fichero.
"""
with open("datos/notas.txt", "w", encoding="utf-8") as fichero:
    fichero.write("Esta es mi primera nota en este archivo.\n")   


# Ejercicio 3: Añadir contenido a un fichero
"""
Objetivo: Modifica el script del Ejercicio 2 para que no sobrescriba el contenido, 
sino que añada texto al final del fichero.
Abre el fichero notas.txt en modo añadir ("a").
Añade el siguiente mensaje: "Esta es otra línea añadida al archivo."
Pistas:
Usa el modo "a" para añadir contenido al final del fichero sin eliminar lo anterior.
"""
with open("datos/notas.txt", "a", encoding="utf-8") as fichero:
    fichero.write("Esta es otra línea añadida al archivo.\n")

"""
Ejercicio 4: Leer líneas de un fichero
Objetivo: Crea un script que lea y muestre cada línea de un fichero de texto, línea por línea.
Usa el fichero poema.txt del Ejercicio 1.
Abre el fichero en modo lectura.
Lee el contenido línea por línea y muestra cada línea por separado.
Pistas:
Usa un bucle for para recorrer cada línea del fichero.
"""
with open("datos/poema.txt", "r", encoding="utf-8") as fichero:
    for linea in fichero:
        print(linea.strip())  # strip() elimina los saltos de línea adicionales

# Alternativamente, podrías usar readlines() y un bucle for:
with open("datos/poema.txt", "r", encoding="utf-8") as fichero:
    lineas = fichero.readlines()
    for linea in lineas:
        print(linea.strip())  # strip() elimina los saltos de línea adicionales


"""
Ejercicio 5: Manejo de excepciones al leer un fichero
Objetivo: Crea un script que intente leer un fichero llamado archivo_inexistente.txt y capture el error si el fichero no existe.
Usa un bloque try-except para manejar el error FileNotFoundError.
Si el fichero no se encuentra, muestra el mensaje "Error: El archivo no existe.".
"""
try:
    with open("datos/archivo_inexistente.txt", "r", encoding="utf-8") as fichero:
        contenido = fichero.read()
        print(contenido)
except FileNotFoundError:
    print("Error: El archivo no existe.")



"""

Ejercicio 6: Contar líneas y palabras en un fichero
Objetivo: Crea un script que cuente el número de líneas y el número total de palabras en un fichero llamado texto.txt.
Abre el fichero en modo lectura.
Recorre cada línea del fichero, contando el número de líneas.
Para cada línea, cuenta cuántas palabras contiene y suma el total de palabras.
Muestra el número total de líneas y el número total de palabras.
Pistas:
Usa el método .split() para dividir una línea en palabras.
Utiliza un contador para sumar las palabras.
"""
with open("datos/poema.txt", "r", encoding="utf-8") as fichero:
    lineas = fichero.readlines()
    num_lineas = len(lineas)
    num_palabras = 0
    for linea in lineas:
        num_palabras += len(linea.split())
    print(f"Número total de líneas: {num_lineas}")
    print(f"Número total de palabras: {num_palabras}")  


"""
Ejercicio 7: Leer un fichero y buscar una palabra
Objetivo: Crea un script que lea un fichero llamado libro.txt y busque una palabra específica introducida por el usuario.
Solicita al usuario que introduzca la palabra a buscar.
Abre el fichero y recorre su contenido.
Muestra cuántas veces aparece la palabra en el fichero.
Pistas:
Usa el método .count() para contar las apariciones de la palabra en cada línea.

"""
def buscar_palabra_en_fichero(fichero, palabra):
    with open(fichero, "r", encoding="utf-8") as f:
        lineas = f.readlines()
        num_apariciones = 0
        for indice, linea in enumerate(lineas):
            lista_palabras = linea.split()
            veces = lista_palabras.count(palabra)
            print(indice, veces)
            num_apariciones += veces
    return num_apariciones

buscar_palabra_en_fichero("datos/poema.txt", "la")


# Ejercicio 8: Leer las lineas del poema y guardarlas en in pickle
"""
Objetivo: Crea un script que lea las líneas de un fichero llamado poema.txt 
y las guarde en un fichero binario usando pickle.
"""

import pickle

with open("datos/poema.txt", "r", encoding="utf-8") as fichero:
    lineas = fichero.readlines()

with open("datos/poema.pickle", "wb") as fichero_binario:
    pickle.dump(lineas, fichero_binario)


with open("datos/poema.pickle", "rb") as fichero_binario:
    lineas_recuperadas = pickle.load(fichero_binario)
print(lineas_recuperadas)
type(lineas_recuperadas)
lineas_recuperadas.append("Linea nueva\n")
