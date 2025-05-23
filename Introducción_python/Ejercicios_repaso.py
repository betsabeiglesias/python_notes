# ===============================================
# 📝 EJERCICIOS DE REPASO - Python Básico
# ===============================================
# Están pensados para ir aumentando ligeramente la complejidad
# y combinar distintos temas vistos en clase.
# -----------------------------------------------

# 🧠 Instrucciones Generales:
# - Intenta resolver cada ejercicio por tu cuenta.
# - Usa apuntes y documentación oficial como referencia.
# - Prueba tu código con distintos inputs.
# - Si usas un LLM, investiga los métodos que aparecen.
# - Escribe código limpio, con funciones, nombres descriptivos y comentarios.

# ===============================================
# ✅ Ejercicio 1: Saludo Personalizado
# ===============================================
# 1. Pide al usuario que ingrese su nombre.
# 2. Pide la fecha de nacimiento (día/mes/año).
# 3. Convierte la fecha a objeto datetime.
# 4. Calcula la edad.
# 5. Muestra un mensaje como:
#    "¡Hola, [Nombre]! Tienes [Edad] años y naciste en [AñoNacimiento]."

from datetime import datetime


def greet_personalized():

    name = get_name()
    birth = get_birth()
    age = get_age(birth)
    print(f'¡Hola {name.capitalize()}. Tienes {age} años y naciste el {birth.strftime('%d/%m/%Y')}!.')

def get_birth():
    while True: 
        date = input("Introduce tu fecha de nacimiento (dd/mm/aaaa): ")
        try:
            birth = datetime.strptime(date, "%d/%m/%Y")
        except ValueError:
            print("Formato inválido o fecha no existente")
        else:
            break
    return birth

def get_name():
    while True:
        name = input("Introduce tu nombre: ").strip()
        if not all(part.isalpha() for part in name.split()) or len(name) == 0:
            print("introduce un nombre correcto")
            continue
        else:
            break
    return " ".join(part.capitalize() for part in name.split())

def get_age(date):
    today = datetime.today()
    days = (today - date).days
    age = (days // 365)
    return age
    

greet_personalized()

# ===============================================
# ✅ Ejercicio 2: Operaciones con Cadenas
# ===============================================
# 1. Pide una frase al usuario.
# 2. Muestra:
#    - Longitud
#    - En mayúsculas y minúsculas
#    - 3 primeras y 3 últimas letras
#    - 'a' reemplazada por 'e'

def change_string():
    string = input("Introduce una frase: ")
    print(f"La longitud de la frase es: {len(string)}")
    print(f"En mayúsculas: {string.capitalize()}")
    print(f"En minúsculas: {string.lower()}")
    print(f"Las 3 primeras letras: {string[:3]}")
    print(f"Las 3 últimas letras: {string[::-3]}")
    print(f"Cambio la a por la e: {string.replace("a", "e")}")
    return string
  
change_string()

# ===============================================
# ✅ Ejercicio 3: Información de Contacto (Diccionario)
# ===============================================
# 1. Crea un diccionario con:
#    - nombre, teléfono, email
# 2. Muestra los datos del contacto con formato.
# 3. Pregunta si quiere añadir ciudad. Si sí, añadirla.
# 4. Muestra las claves y los valores.


def get_name():
    while True:
        name = input("Introduce tu nombre: ").strip()
        if not all(part.isalpha() for part in name.split()) or len(name) == 0:
            print("introduce un nombre correcto")
            continue
        else:
            break
    return " ".join(part.capitalize() for part in name.split())

def get_phone():
    while True:
        phone = input("Introduce tu número de teléfono (666666666): ")
        if phone.isdigit() and len(phone) == 9:
            return phone
        print("Introduce un número válido (9 dígitos).")

def get_email():
    email = input("Introduce tu email:")
    return email

def get_city():
    while True:
        try:
            res = int(input("¿Quieres introducir la ciudad? (0-SÍ // 1-NO): "))
            if res == 0:
                city = input("Introduce tu ciudad: ").strip().capitalize()
                break
            elif res == 1:
                city = "No disponible"
                break
            else:
                print("Introduce una opción válida (0 o 1).")
        except ValueError:
            print("Debes introducir un número (0 o 1).")
    return city

def get_contact():
    contact = {
        "nombre": get_name(),
        "teléfono": get_phone(),
        "email": get_email(),
        "city": get_city()
    }
    return contact

def show_contact(contact):
    for key, value in contact.items():
        print(f"{key}: {value}")


contacto = get_contact()
show_contact(contacto)


# ===============================================
# ✅ Ejercicio 4: Elementos Únicos (Sets)
# ===============================================
# 1. Crea una lista con duplicados: [1,2,2,3,...]
# 2. Convierte a set y muestra el resultado.
# 3. Crea otro set con {4,5,6,7}
# 4. Muestra unión e intersección.


numeros = [1, 2, 2, 3, 4, 4, 4, 5, 6, 6, 7, 8, 8, 9, 10, 10]
set1 = set(numeros)
set1

otros_numeros = [4, 5, 6, 7, 11, 12, 13, 14, 10]
set2 = set(otros_numeros)
set2


union = set1 | set2
union

interseccion = set1 & set2
interseccion


# ===============================================
# ✅ Ejercicio 5: Menú de Opciones (con match-case)
# ===============================================
# 1. Muestra un menú:
#    1. Escribir en archivo
#    2. Leer archivo
#    3. Mostrar fecha actual
#    4. Salir
# 2. Pide opción al usuario.
# 3. Usa match-case para ejecutar acciones.
# 4. Si opción no válida, muestra error.

def choose_option():
    while True:
        try:
            opt = int(input(
                "Elige una opción:\n"
                "1. Escribir en archivo\n"
                "2. Leer archivo\n"
                "3. Mostrar fecha actual\n"
                "4. Salir\n"
                ))
            match opt:
                case 1:
                    print("w")
                case 2:
                    try:
                        with open("datos/poema.txt","r") as file:
                            contenido = file.read()
                            print(contenido)
                    except FileNotFoundError:
                        print("Archivo no encontrado\n")
                case 3:
                    print(f"Hoy es {datetime.today().strftime("%d/%m/%Y")}")
                case 4:
                    print("Saliendo...\n")
                    break
                case _:
                    print("Elige una opción válida\n")
        except ValueError as e:
            print("Opción no válida, introduce un número del 1 al 4")
            print(f"Error técnico {e}")

choose_option()



# ===============================================
# ✅ Ejercicio 6: Lista de la Compra
# ===============================================
# 1. Lista vacía llamada lista_compra.
# 2. Pide 5 productos y añádelos.
# 3. Muestra la lista.
# 4. Permite eliminar un producto.
# 5. Muestra la lista final y cantidad restante.
# 6. Guarda los datos en tareas.txt usando with open().
# 7. Usa try-except para manejar FileNotFoundError.


# ===============================================
# 🚀 Desafío: Contador de Palabras en Archivo
# ===============================================
# 1. Pide nombre de archivo.
# 2. Lee el contenido.
# 3. Limpia texto: minúsculas, quita puntuación.
# 4. Divide en palabras.
# 5. Usa diccionario para contar frecuencias.
# 6. Muestra top 10 palabras más frecuentes.
# 7. Maneja FileNotFoundError si el archivo no existe.
