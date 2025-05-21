# Ejercicio 1
"""
Crea una lista llamada 'dias' con los días de la semana.
Luego imprime el primer y el último elemento de la lista.
"""

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
print("Primer día:", dias[0])
print("Último día:", dias[-1])

# Ejercicio 2
"""
Modifica el segundo y el quinto elemento de la lista 'dias' para que estén en inglés.
Imprime la lista modificada.
"""

dias[1] = "Tuesday"
dias[4] = "Friday"
print(dias)

# Ejercicio 3
"""
Crea una lista vacía llamada 'numeros'.
Usa un bucle for para llenarla con los números del 1 al 5.
Luego imprime la lista.
"""

numeros = []
for i in range(1, 6):
    numeros.append(i)
print(numeros)

# Ejercicio 4
"""
Extrae los tres primeros elementos de la lista 'dias' y guárdalos en una nueva lista llamada 'inicio_semana'.
Imprime esa nueva lista.
"""

inicio_semana = dias[:3]
print("Inicio de la semana:", inicio_semana)

# Ejercicio 5
"""
Verifica si "Domingo" está en la lista 'dias'.
Si está, imprime "¡Encontrado!".
Si no está, imprime "No está en la lista.".
"""

if "Domingo" in dias:
    print("¡Encontrado!")
else:
    print("No está en la lista.")

# Ejercicio 6
"""
Concatena la lista [8, 9, 10] a la lista 'numeros'.
Imprime la nueva lista.
"""

numeros = numeros + [8, 9, 10]
print("Lista extendida:", numeros)

# Ejercicio 7
"""
Cuenta cuántas veces aparece el número 3 en la lista 'numeros'.
Imprime el resultado.
"""

cantidad = numeros.count(3)
print("El número 3 aparece", cantidad, "veces.")

# Ejercicio 8
"""
Crea una lista anidada con datos de 3 estudiantes: nombre, estatura y peso.
Llama a esta lista 'estudiantes'. Luego imprime la estatura del segundo estudiante.
"""

estudiantes = [["Laura", 1.65, 60], ["Pedro", 1.80, 75], ["Sofía", 1.70, 68]]
print("Estatura de Pedro:", estudiantes[1][1])

# Ejercicio 9
"""
Usa el método .pop() para eliminar el último elemento de la lista 'numeros'.
Imprime la lista resultante.
"""

numeros.pop()
print("Lista después de eliminar el último elemento:", numeros)

# Ejercicio 10
"""
Ordena alfabéticamente la lista 'dias'.
Imprime la lista ordenada.
"""

dias.sort()
print("Días ordenados alfabéticamente:", dias)
