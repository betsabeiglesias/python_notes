# Ejercicio 1
"""
Crea una lista llamada 'dias' con los días de la semana.
Luego imprime el primer y el último elemento de la lista.
"""

dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
dias[0]
dias[-1]



# Ejercicio 2
"""
Modifica el segundo y el quinto elemento de la lista 'dias' para que estén en inglés.
Imprime la lista modificada.
"""

dias[1] = "tuesday"
dias[5] = "saturday"
dias


# Ejercicio 3
"""
Extrae los tres primeros elementos de la lista 'dias' y guárdalos en una nueva lista llamada 'inicio_semana'.
Imprime esa nueva lista.
"""

inicio_semana = dias[0:3]
inicio_semana


# Ejercicio 4
"""
Desempaqueta la lista 'dias' en tres variables"""
inicio, medio, fin = dias[0:3], dias[3:5], dias[5:]
inicio
medio
fin


# Ejercicio 5
"""
Crea una lista llamada 'numeros' con los números del 1 al 5.
Agrega el número 6 al final de la lista.
Luego imprime la longitud de la lista.
"""
# numeros =[1,2,3,4,5]
numeros = list(range(1,6))
numeros
numeros.append(6)
numeros
len(numeros)


# Ejercicio 6
"""
Concatena la lista [8, 9, 10] a la lista 'numeros'.
Imprime la nueva lista.
"""

numeros2 = [8,9,10]
new_numeros = numeros + numeros2
new_numeros

# otro modo
numeros.extend(numeros2) #extend modifica la lista, con la concatenación + hay que guardalo en una variable
print(numeros)


# Ejercicio 7
"""
Cuenta cuántas veces aparece el número 3 en la lista 'numeros'.
Imprime el resultado.
"""

number_3 = numeros.count(3)
number_3



# Ejercicio 8
"""
Crea una lista anidada con datos de 3 estudiantes: nombre, estatura y peso.
Llama a esta lista 'estudiantes'. Luego imprime la estatura del segundo estudiante.
"""

estudiantes = [["Ana", 170, 75], ["Luis", 150, 55], ["Maite", 160, 65]]
estudiantes[1][1]

estudiante1 = {"nombre": "Ana", "estatura": 170, "peso": 75}
estudiante2 = {"nombre": "Luis", "estatura": 150, "peso": 55}
estudiante3 = {"nombre": "Maite", "estatura": 160, "peso": 65}
estudiantes = [estudiante1, estudiante2, estudiante3]
estudiantes[1]["estatura"]
# otra forma de hacerlo
estudiantes = [
    {"nombre": "Ana", "estatura": 170, "peso": 75},
    {"nombre": "Luis", "estatura": 150, "peso": 55},
    {"nombre": "Maite", "estatura": 160, "peso": 65}
]
estudiantes[1]["estatura"]  # Acceder a la estatura del segundo estudiante
# otra forma de hacerlo



# Ejercicio 9
"""
Usa el método .pop() para eliminar el último elemento de la lista 'numeros'.
Imprime la lista resultante.
"""

numeros.pop()
numeros


# Ejercicio 10
"""
Ordena alfabéticamente la lista 'dias'.
Imprime la lista ordenada.
"""

dias.sort(reverse=False)
dias

