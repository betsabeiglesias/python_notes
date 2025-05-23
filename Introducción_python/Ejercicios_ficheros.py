# Ejercicios Ficheros
# Recuerda marcar como directorio de trabajo el script donde estés ejecutando el fichero. También puedes crear una subcarpeta “archivos” donde meter todos los ficheros, para ello puedes usar rutas relativas: "./archivos/nombre_archivo.txt"

# Ejercicio 1: Leer un fichero de texto
# Objetivo: Crea un script que lea el contenido de un fichero llamado poema.txt y muestre su contenido en la consola.
# Abre el fichero en modo lectura ("r").
# Lee todo el contenido del fichero.
# Muestra el contenido en pantalla.
# Pistas:
# Usa la función open() para abrir el fichero.
# Usa el método .read() para leer todo el contenido de una sola vez.


with open('datos/poema.txt', 'r', encoding="utf-8") as poema:
    contenido = poema.read()
print(contenido)


# Ejercicio 2: Escribir en un fichero de texto
# Objetivo: Crea un script que escriba un mensaje en un fichero llamado notas.txt.
# Abre el fichero en modo escritura ("w").
# Si el fichero no existe, debe crearse automáticamente.
# Escribe en el fichero: "Esta es mi primera nota en este archivo."
# Pistas:
# Recuerda que el modo "w" sobrescribe el contenido si el fichero ya existe.
# Usa el método .write() para escribir en el fichero.


with open('datos/notas.txt', 'w') as f:
    data = f.write("Esta es mi primera nota en este archivo")
  
#write qué devuelve??? el número de caracteres que se han escrito
print(f'y esto es data: {data}') 

# si quisiera escribir y también leer

with open('datos/notas.txt', 'w+') as f:
    f.write("Esta es mi primera nota3 en este archivo")
    f.seek(0)
    f.read()



# Ejercicio 3: Añadir contenido a un fichero
# Objetivo: Modifica el script del Ejercicio 2 para que no sobrescriba el contenido, sino que añada texto al final del fichero.
# Abre el fichero notas.txt en modo añadir ("a").
# Añade el siguiente mensaje: "Esta es otra línea añadida al archivo."
# Pistas:
# Usa el modo "a" para añadir contenido al final del fichero sin eliminar lo anterior.

with open('datos/notas.txt', 'a') as f:
    f.write("\nEsta es otra línea añadida al archivo.")




# Ejercicio 4: Leer líneas de un fichero
# Objetivo: Crea un script que lea y muestre cada línea de un fichero de texto, línea por línea.
# Usa el fichero poema.txt del Ejercicio 1.
# Abre el fichero en modo lectura.
# Lee el contenido línea por línea y muestra cada línea por separado.
# Pistas:
# Usa un bucle for para recorrer cada línea del fichero.

with open('datos/poema.txt', 'r') as poema:
    for linea in poema:
        print(linea, end="")


# Ejercicio 5: Manejo de excepciones al leer un fichero
# Objetivo: Crea un script que intente leer un fichero llamado archivo_inexistente.txt y capture el error si el fichero no existe.
# Usa un bloque try-except para manejar el error FileNotFoundError.
# Si el fichero no se encuentra, muestra el mensaje "Error: El archivo no existe.".
# Pistas:
# Usa try-except para manejar la excepción FileNotFoundError.


try:
    with open('datos/fichero_inexistente.txt',"r") as file:
        print(file.read())
except Exception as e:
    print("Error: El archivo no existe.")
    print(f"Mensaje del sistema: {e}")


# Ejercicio 6: Contar líneas y palabras en un fichero
# Objetivo: Crea un script que cuente el número de líneas y el número total de palabras en un fichero llamado texto.txt.
# Abre el fichero en modo lectura.
# Recorre cada línea del fichero, contando el número de líneas.
# Para cada línea, cuenta cuántas palabras contiene y suma el total de palabras.
# Muestra el número total de líneas y el número total de palabras.
# Pistas:
# Usa el método .split() para dividir una línea en palabras.
# Utiliza un contador para sumar las palabras.

with open('datos/poema.txt', 'r') as poema:
    lineas = 0
    palabras = 0
    for linea in poema:
        lineas += 1
        cantidad_palabras = len(linea.split())
        palabras += cantidad_palabras

    print(f"Número de lineas {lineas}")
    print(f"Número de palabras {palabras}")



# Ejercicio 7: Leer un fichero y buscar una palabra
# Objetivo: Crea un script que lea un fichero llamado libro.txt y busque una palabra específica introducida por el usuario.
# Solicita al usuario que introduzca la palabra a buscar.
# Abre el fichero y recorre su contenido.
# Muestra cuántas veces aparece la palabra en el fichero.
# Pistas:
# Usa el método .count() para contar las apariciones de la palabra en cada línea.

def busca_cuenta_palabra():
    palabra = input("Introduce la palabra a buscar: ")
    with open("datos/quijote.txt") as file:
        texto = file.read()
        ocurrencias = texto.count(palabra)
    print(f"{palabra} aparece {ocurrencias} veces.")
    
busca_cuenta_palabra()


def busca_pablabra(fichero, palabra):
    with open("datos/quijote.txt") as file:
        lineas = f.readlines()
        num_apariciones = 0
        for indice, linea in enumerate(lineas):
            lista_palabras = linea.split()
            veces = lista_palabras.count(palabra)
            print(indice, veces)
            num_apariciones += veces
        return num_apariciones

busca_pablabra("datos/quijote.txt", "Sancho")


# Ejercicio 8: Leer las líneas del poema y guardarlas en pickle
# Objetivo: Crea un script que lea las líneas de un fichero y las
# guarde en un fichero binario usando pickle

import pickle

def guardar_pickle(archivo_txt, archivo_pkl):
    with open(archivo_txt, "r") as file:
        listalineas = file.readlines()
    with open(archivo_pkl, "wb") as f_pickle:
        pickle.dump(listalineas, f_pickle)
       
guardar_pickle("datos/poema.txt", "datos/poema.pkl")

with open("datos/poema.pkl", "rb") as file_binary:
    lineas = pickle.load(file_binary)
print(lineas)
type(lineas)




