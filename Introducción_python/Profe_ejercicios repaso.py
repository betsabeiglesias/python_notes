# Ejercicio 1: Saludo Personalizado
"""
1. Pide al usuario que ingrese su nombre.
2. Pide al usuario que ingrese su fecha de nacimiento. (día/mes/año)
3. Convierte el dato aportado por el usuario en un objeto datetime (consulta la documentación)
4. Calcula la edad del usuario.
5. Muestra un mensaje de bienvenida formateado que incluya su nombre, edad y año de nacimiento.
    - Ejemplo: "¡Hola, [Nombre]! Tienes [Edad] años y naciste en [AñoNacimiento]."
"""
import datetime

datetime.datetime.now()

hoy = datetime.date.today()

nacimiento = datetime.date(2000, 5, 25)

# nacimiento.year = 2025

cumpleannos = datetime.date(hoy.year, nacimiento.month, nacimiento.day)

(hoy - cumpleannos).days

def calcular_edad(nacimiento: datetime.date) -> int:
    """
    Calcula la edad de una persona a partir de su fecha de nacimiento.
    :param nacimiento: Fecha de nacimiento en formato datetime.date.
    :return: Edad de la persona.
    """
    hoy = datetime.date.today()
    
    # Calcula la fecha del cumpleaños en el año actual
    cumpleannos = datetime.date(hoy.year, nacimiento.month, nacimiento.day)
    
    # Calcula la edad por diferencia de año de nacimiento
    edad = hoy.year - nacimiento.year
    
    # Si el cumpleaños no ha llegado aún este año, restar un año a la edad
    dias_desde_cumple = (hoy - cumpleannos).days
    edad -= 1 if dias_desde_cumple < 0 else 0
    
    # Si hoy es el cumpleaños, felicitar
    if dias_desde_cumple==0:
        print("¡Feliz cumpleaños!")
    return edad


def saludo_personalizado():
    print("Hola, bienvenido al programa de saludo personalizado.")
    nombre = input("Por favor, ingresa tu nombre: ")
    nacimiento_str = input("Ingresa tu fecha de nacimiento (día/mes/año): ")
    nacimiento_fecha = datetime.datetime.strptime(nacimiento_str, "%d/%m/%Y")
    edad = calcular_edad(nacimiento_fecha)
    print(f"¡Hola, {nombre}! Tienes {edad} años pero aparentas mucho menos y naciste en {nacimiento_fecha.year}.")

(4,30) < (5,1)

saludo_personalizado()
22

#Ejercicio 2: Operaciones con Cadenas#
"""
1. Pide al usuario que ingrese una frase.
2. Muestra:
    - La longitud de la frase.
    - La frase en mayúsculas.
    - La frase en minúsculas.
    - Las tres primeras letras de la frase.
    - Las tres últimas letras de la frase.
    - La frase con todas las 'a' reemplazadas por una 'e'.
"""
import re
def pide_frase():
    frase = input("Ingresa una frase: ")
    print(f"La longitud de la frase es: {len(frase)}")
    print(f"La frase en mayúsculas es: {frase.upper()}")
    print(f"La frase en minúsculas es: {frase.lower()}")
    print(f"Las tres primeras letras de la frase son: {frase[:3]}")
    print(f"Las tres últimas letras de la frase son: {frase[-3:]}")
    print(f"La frase con todas las 'a' reemplazadas por una 'e' es: {frase.replace('a', 'e')}")
    print(f"La frase con todas las 'a' reemplazadas por una 'e' son regex es: {re.sub('[aá]', 'e', frase)}")
    return frase

pide_frase()

#Ejercicio 3: Información de Contacto (Diccionario)#
"""
1. Crea un diccionario llamado `contacto` que almacene:
    - `nombre`: (pide al usuario que lo ingrese)
    - `telefono`: (pide al usuario que lo ingrese)
    - `email`: (pide al usuario que lo ingrese)
2. Muestra la información del contacto de forma clara (ej: "Nombre: Juan, Teléfono: 123456789, Email: [juan@example.com](mailto:juan@example.com)").
3. Pregunta al usuario si quiere añadir una `ciudad` al contacto. Si es así, pídela y añádela al diccionario.
4. Muestra todas las claves (keys) del diccionario.
5. Muestra todos los valores (values) del diccionario.
"""

def verifica_telefono(telefono):
    while True:
        telefono_num = "".join(filter(str.isdigit, telefono))
        if len(telefono_num) == 9 and telefono_num[0] in "679":
            return telefono_num
        else:
            telefono = input("El teléfono no es correcto. Introduce un teléfono correcto: ")

verifica_telefono("1234sdfsgsd .56e789")

def contacto():
    # 1. Crear el diccionario contacto
    contacto = {
        'nombre': input("Ingrese el nombre: "),
        'telefono': verifica_telefono(input("Ingrese el teléfono: ")),
        'email': input("Ingrese el email: ")
    }

    # 2. Mostrar la información del contacto
    print(f"\nInformación del contacto:")
    print(f"Nombre: {contacto['nombre']}, Teléfono: {contacto['telefono']}, Email: {contacto['email']}")

    # 3. Preguntar por ciudad
    agregar_ciudad = input("\n¿Desea añadir una ciudad al contacto? (s/n): ").lower()
    if agregar_ciudad == 's':
        contacto['ciudad'] = input("Ingrese la ciudad: ")
        print("¡Ciudad añadida correctamente!")

    # 4. Mostrar todas las claves
    print("\nClaves del diccionario:", list(contacto.keys()))  # Convertimos a lista para mejor visualización

    # 5. Mostrar todos los valores
    print("\nValores del diccionario:", list(contacto.values()))

    return contacto

contacto_resultante = contacto()
print("Diccionario final completo:", contacto_resultante)


#Ejercicio 4: Elementos Únicos (Sets)#
"""
1. Crea una lista con elementos duplicados, por ejemplo: `numeros = [1, 2, 2, 3, 4, 4, 4, 5]`.
2. Convierte esta lista a un `set` para eliminar los duplicados.
3. Muestra el `set` resultante.
4. Crea otro `set` con algunos números, por ejemplo: `otros_numeros = {4, 5, 6, 7}`.
5. Muestra la unión de ambos sets.
6. Muestra la intersección de ambos sets.
"""

# 1. Lista con elementos duplicados
numeros = [1, 2, 2, 3, 4, 4, 4, 5]
print(f"\n1. Lista original con duplicados: {numeros}")

# 2. Convertir a set para eliminar duplicados
numeros_sin_duplicados = set(numeros)

# 3. Mostrar el set resultante (ya hecho en el paso anterior)
print(f"2. Set sin duplicados: {numeros_sin_duplicados}")

# 4. Crear otro set
otros_numeros = {4, 5, 6, 7}
print(f"\n4. Segundo set creado: {otros_numeros}")

# 5. Mostrar unión de ambos sets
union = numeros_sin_duplicados.union(otros_numeros)
print(f"5. Unión de ambos sets: {union}")

# 6. Mostrar intersección de ambos sets
interseccion = numeros_sin_duplicados.intersection(otros_numeros)
print(f"6. Intersección de ambos sets: {interseccion}")
    

#Ejercicio 5: Menú de Opciones (con `match`)#
"""
1. Muestra un menú de opciones al usuario:
    
    ```
    1. Escribir texto en un archivo
    2. Mostrar el texto escrito un archivo
    3. Mostrar fecha actual
    4. Salir del programa
    ```
    
2. Pide al usuario que elija una opción (1, 2 o 3).
3. Usa una estructura `match-case` para ejecutar la acción correspondiente a la opción elegida.
4. Si la opción no es válida, muestra un mensaje de error.
"""
import datetime

def escribir_archivo():
    """Función para escribir texto en un archivo"""
    nombre_archivo = input("Ingrese el nombre del archivo: ")
    texto = input("Escriba el texto a guardar: ")
    with open(nombre_archivo, 'w') as archivo:
        archivo.write(texto)
    print(f"Texto guardado correctamente en {nombre_archivo}")

def leer_archivo():
    """Función para leer y mostrar contenido de un archivo"""
    nombre_archivo = input("Ingrese el nombre del archivo a leer: ")
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
        print("\nContenido del archivo:")
        print(contenido)
    except FileNotFoundError:
        print("Error: El archivo no existe")

def mostrar_fecha():
    """Función para mostrar la fecha y hora actual"""
    ahora = datetime.datetime.now()
    print(f"\nFecha y hora actual: {ahora.strftime('%d/%m/%Y %H:%M:%S')}")

def mostrar_menu():
    """Muestra el menú de opciones"""
    print("\n--- MENÚ PRINCIPAL ---")
    print("1. Escribir texto en un archivo")
    print("2. Mostrar el texto escrito en un archivo")
    print("3. Mostrar fecha actual")
    print("4. Salir del programa")

def aplicacion():
    """Función principal del programa"""
    while True:
        mostrar_menu()
        opcion = input("\nSeleccione una opción (1-4): ")
        
        match opcion:
            case '1':
                escribir_archivo()
            case '2':
                leer_archivo()
            case '3':
                mostrar_fecha()
            case '4':
                print("\nSaliendo del programa... ¡Hasta luego!")
                break
            case _:
                print("\nOpción no válida. Por favor ingrese un número del 1 al 4")

aplicacion()

#Ejercicio 6: Lista de la Compra#
"""
1. Crea una lista vacía llamada `lista_compra`.
2. Pide al usuario que ingrese 5 productos para añadir a la lista.
3. Muestra la lista completa.
4. Pregunta al usuario si quiere eliminar algún producto. Si dice que sí, pregúntale cuál y elimínalo.
5. Muestra la lista final.
6. Indica cuántos productos quedan en la lista.
7. Mantén sincronizada la lista con un archivo `tareas.txt`
8. Utiliza el bloque `with open(...)` para asegurar que los archivos se cierren correctamente.
9. Utiliza `try-except` para manejar posibles `FileNotFoundError` si el archivo no existe al intentar leerlo por primera vez (en ese caso, simplemente informa que no hay tareas).
"""
def mostrar_lista_compra(lista_compra):
    print("\nLista de compra completa:")
    for indice, producto in enumerate(lista_compra, start=1):
        print(f"{indice}. {producto}")
    print(f"\nTotal de productos: {len(lista_compra)}")
    with open('lista_compra.txt', 'w') as archivo:
        for producto in lista_compra:
            archivo.write(producto + '\n')

def cargar_lista_compra():
    try:
        with open('lista_compra.txt', 'r') as archivo:
            return [linea.strip() for linea in archivo]
    except FileNotFoundError:
        return []


def llena_lista_compra(lista_compra):
    for i in range(5):
        producto = input(f"Ingrese el producto {i+1} (c=cancelar): ")
        if producto.lower() == 'c':
            mostrar_lista_compra(lista_compra)
            break
        lista_compra.append(producto)
    mostrar_lista_compra(lista_compra)

def eliminar_producto(lista_compra):
    producto_eliminar = input("Ingrese el número del producto a eliminar: ")
    if producto_eliminar in lista_compra:
        lista_compra.remove(producto_eliminar)
    else:
        lista_compra.pop(int(producto_eliminar)-1)
    mostrar_lista_compra(lista_compra)
    return input("\n¿Desea eliminar algún producto más? (s/n): ").lower()

def mostrar_menu():
    print("\nMenú:")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Mostrar lista")
    print("4. Salir")
    return input("Ingrese una opción: ")

def menu(lista_compra):
    while True:
        opcion = mostrar_menu()
        match opcion:
            case '1':
                llena_lista_compra(lista_compra)
                mostrar_lista_compra(lista_compra)
            case '2':
                eliminar_producto(lista_compra)
            case '3':
                mostrar_lista_compra(lista_compra)
            case '4':
                print("Saliendo del programa...")
                break
            case _:
                print("Opción no válida. Intente de nuevo.")


def gestor_lista_compra():
    lista_compra = cargar_lista_compra()
    if not lista_compra:
        print("La lista está vacía, ingrese 5 productos")
        llena_lista_compra(lista_compra)
    else: 
        mostrar_lista_compra(lista_compra)
        menu(lista_compra)

        
gestor_lista_compra()


#Desafío: Contador de Palabras en un Archivo#
"""
1. Pide al usuario el nombre de un archivo de texto.
2. Lee el contenido del archivo.
3. Limpia el texto: conviértelo a minúsculas y elimina signos de puntuación básicos (puedes usar `replace()` para comas, puntos, etc.).
4. Divide el texto en palabras.
5. Usa un diccionario para contar la frecuencia de cada palabra.
6. Muestra las 10 palabras más frecuentes y su conteo.
7. Maneja la excepción `FileNotFoundError`.
"""

def carga_archivo(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            return contenido
    except FileNotFoundError:
        print("El archivo no existe.")
        return None

def limpiar_texto(texto):
    texto = texto.lower()
    texto = texto.replace(",", "").replace(".", "").replace(";", "").replace(":", "").replace("!", "").replace("?", "")
    texto = texto.replace("\n", " ")
    return texto

def dividir_texto(texto):
    palabras = texto.split()
    return palabras

dividir_texto(limpiar_texto(carga_archivo("lista_compra.txt")))

def contar_palabras(palabras):
    frecuencia = {}
    for palabra in palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1
    return frecuencia

"""
frecuencia.items():
    Convierte el diccionario en una lista de tuplas (clave, valor).

    Ejemplo: {'a': 5, 'b': 3} → [('a', 5), ('b', 3)]

sorted() con key=lambda item: item[1]:
    Ordena la lista de tuplas según los valores (frecuencias).

    item[1] se refiere al segundo elemento de cada tupla (el valor numérico).

    lambda es una función anónima que define el criterio de ordenación.

reverse=True:
    Ordena en orden descendente (de mayor a menor frecuencia).

[:n]:
    Toma los primeros n elementos de la lista ordenada.

Retorno:
    Devuelve una lista con las n tuplas (palabra, frecuencia) más frecuentes.
"""

def palabras_mas_frecuentes(frecuencia, n=10):
    palabras_ordenadas = sorted(frecuencia.items(), key=lambda item: item[1], reverse=True)
    return palabras_ordenadas[:n]

palabras_mas_frecuentes(contar_palabras(dividir_texto(limpiar_texto(carga_archivo("lista_compra.txt")))))
