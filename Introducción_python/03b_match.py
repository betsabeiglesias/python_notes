"""
Python Match (Sentencia match)
--------------------------------
La sentencia `match` se utiliza para realizar diferentes acciones basadas en diferentes condiciones.

En lugar de escribir muchas sentencias `if..else`, puedes usar la sentencia `match`.
La sentencia `match` selecciona uno de muchos bloques de código para ser ejecutado.
"""

# Ejemplo básico de match
# -------------------------
# La expresión se evalúa y se compara con cada caso
# Cuando encuentra coincidencia, ejecuta el bloque correspondiente

dia = 4
print("\nEjemplo básico:")
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miércoles")
    case 4:
        print("Jueves")
    case 5:
        print("Viernes")
    case 6:
        print("Sábado")
    case 7:
        print("Domingo")

# Caso por defecto con _
# -------------------------
# El guión bajo _ actúa como caso por defecto
# Debe colocarse al final porque siempre hace match

print("\nEjemplo con caso por defecto:")
dia = 8
match dia:
    case 6:
        print("Hoy es Sábado")
    case 7:
        print("Hoy es Domingo")
    case _:
        print("Esperando el fin de semana")

# Combinar valores con |
# -------------------------
# El operador | permite hacer match con múltiples valores

print("\nEjemplo combinando valores:")
dia = 3
match dia:
    case 1 | 2 | 3 | 4 | 5:
        print("Hoy es día laboral")
    case 6 | 7:
        print("¡Me encantan los fines de semana!")

# Guardias con if
# -------------------------
# Se pueden agregar condiciones adicionales con if

print("\nEjemplo con guardias:")
mes = 5
dia = 4
match dia:
    case 1 | 2 | 3 | 4 | 5 if mes == 4:
        print("Un día laboral en Abril")
    case 1 | 2 | 3 | 4 | 5 if mes == 5:
        print("Un día laboral en Mayo")
    case _:
        print("Sin coincidencia")

# Match con patrones más complejos
# -------------------------------
# También funciona con listas, tuplas y diccionarios

print("\nEjemplo con patrones complejos:")
punto = (2, 3)
match punto:
    case (0, 0):
        print("Origen")
    case (0, y):
        print(f"En el eje Y, coordenada {y}")
    case (x, 0):
        print(f"En el eje X, coordenada {x}")
    case (x, y):
        print(f"Punto en ({x}, {y})")
    case _:
        print("No es un punto válido")

"""
Notas importantes:
1. La sentencia match está disponible desde Python 3.10
2. El orden de los casos es importante (se evalúan en orden)
3. _ siempre debe ir al final como caso por defecto
4. Se puede hacer match con patrones complejos (no solo valores simples)
"""