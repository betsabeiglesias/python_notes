"""
Spyder Editor

This is a temporary script file.
"""

# 1. Calculadora Simple:
"""
Crea una función que pueda realizar operaciones básicas como suma, resta, 
multiplicación y división. 
Pedirá al usuario elegir una operación a partir de un listado y luego pedirá los valores a operar.


Utiliza funciones separadas para cada operación.
"""
print("""
    Elige la operación a realizar:
      1 = Suma
      2 = Resta
      3 = Multiplicación
      4 = División
""")



def suma(x,y):
    return (x+y)

def resta(x,y):
    return (x-y)

def multiplicacion(x,y):
    return (x*y)

def division(x,y):
    if y == 0:
        return "Error: división entre cero"
    return (x/y)

def salir():
    pass

def calculadora(operacion, num1, num2):
    if operacion == 1:
        return print(f'El resultado {suma(num1, num2)}')
    elif operacion == 2:
        return print(f'El resultado {resta(num1, num2)}')
    elif operacion == 3:
        return print(f'El resultado {multiplicacion(num1, num2)}')
    else:
        return print(f'El resultado {division(num1, num2)}')


try:
    print("""
    Elige la operación a realizar:
        1 = Suma
        2 = Resta
        3 = Multiplicación
        4 = División
        """)
    operacion = int(input("Elige la operación (1/2/3/4): "))
    num1, num2 = int(input("Introduce el primer número: ")), int(input("Introduce el segundo número: "))
    calculadora(operacion, num1, num2)
except ValueError:
    print("Por favor, introduce solo números")


#OTRA FORMA
def calculadora(operacion, num1, num2):
    match operacion:
        case 1:
            print(f'El resultado es {suma(num1, num2)}')
        case 2:
            print(f'El resultado es {resta(num1, num2)}')
        case 3:
            print(f'El resultado es {multiplicacion(num1, num2)}')
        case 4:
            print(f'El resultado es {division(num1, num2)}')
        case _:
            print("Operación no válida")




#OTRA FORMA
while True:
    print("""
    Elige la operación a realizar:
        1 = Suma
        2 = Resta
        3 = Multiplicación
        4 = División
        5 = Salir
        """)
    operacion = int(input("Elige la operación (1/2/3/4): "))
    operaciones = {1: suma, 2: resta, 3: multiplicacion, 4: division, 5: salir}
    if operacion not in operaciones:
        print("Operación no válida")
        continue
    if operacion == 5:
        print("Saliendo de la calculadora...")
        break
    num1, num2 = int(input("Introduce el primer número: ")), int(input("Introduce el segundo número: "))
    resultado = operaciones[operacion](num1, num2)
    print(f'El resultado es {resultado}')


# 2. Número Primo:
"""
Escribe una función que determine si un número dado es primo o no. 
Pedirá al usuario que ingrese un número y muestra un mensaje 
indicando si es primo o no.
"""


def is_primo(num):
    if num < 2:
        return False
    i = 2
    while i <= num // 2:
        if num % i == 0:
                return False
        i += 1
    return True

      

def result_primo(num):
    if (is_primo(num) == True):
        print(f"El número {num} es primo")
    else:
        print(f"El número {num} no es primo")

num_primo =  int(input("Introduce un número: "))
result_primo(num_primo)




# 3. Cálculo del Área:
"""
Implementa funciones para calcular el área de diferentes formas geométricas 
como círculo, cuadrado y triángulo. Pide al usuario que elija la forma y 
luego ingrese los valores necesarios.
"""
print("""
Opcion
    1 : Circulo
    2 : Cuadrado
    3 : Triángulo

""")

from math import pi as PI


def area_circulo(radio):
    return (2 * PI *radio)

def area_cuadrado(lado):
    return lado * lado

def area_triangulo(base, altura):
    return base * altura / 2

def salir():
    print("Saliendo...")



def calculadora_area():
    while True:
        print("""
        Elige la forma:
            1 = Círculo
            2 = Cuadrado
            3 = Triángulo
            4 = Salir
            """)
        forma = int(input("Opción: "))
        match forma:
            case 1:
                radio = int(input("Introduce el radio: "))
                print(f"El área del círculo con radio {radio} es {area_circulo(radio)}")
            case 2:
                lado = int(input("Introduce el lado: "))
                print(f"El área del cuadrado con lado {lado} es {area_cuadrado(lado)}")
            case 3:
                base = int(input("Introduce el base: "))
                altura = int(input("Introduce el altura: "))
                print(f"El área del triángulo con base {base} y altura {altura} es {area_triangulo(base, altura)}")
            case 4:
                salir()

                break
            case _:
                print("La opción no es correcta")
    
calculadora_area()


# 4. Inversión de Cadena:
"""
Crea una función que tome una cadena como entrada y devuelva la cadena invertida. 
Por ejemplo, si la entrada es "python", la salida debería ser "nohtyp".
"""

def str_reverse(cadena):
    for char in cadena[::-1]:
        print(char,end="")
        
def str_reverse2(cadena):
    return cadena[::-1]

ejemplo = "python"
str_reverse(ejemplo)
str_reverse2(ejemplo)




# 5. Contador de Palabras:
"""
Desarrolla una función que cuente el número de palabras en una oración. 
Pide al usuario que ingrese una oración y muestra el resultado.
"""

def ft_split(str):
    word = 0
    flag_inword = False
    for char in str:
        if char.isspace():
            flag_inword = False
        else:
            if not flag_inword:
                word += 1
                flag_inword = True
    return word


ejemplo = "Aquí hay 6 palabras y         tabulaciones"
ft_split(ejemplo)


# 6. Fibonacci:
"""
Implementa una función para generar los primeros n números de la 
secuencia de Fibonacci. Pide al usuario que ingrese el valor de n.
"""

def ft_fibonacci(num):
    a = 0
    b = 1
    i = 0
    while i <= num:
        print(a)
        a, b = b, a + b          
        i += 1

ft_fibonacci(5)


# 7. Ordenar Lista:
"""
Escribe una función que ordene una lista de números de manera ascendente 
o descendente según la elección del usuario.
"""

def ft_sort(list):
    for i in range(len(list)):
        for j in range(i + 1, len(list)):
            if list[i] > list[j]:
                list[i], list[j] = list[j], list[i]
    return list
list = [5, 2, 9, 1, 5, 6]
print("Lista desordenada:", list)
print("Lista ordenada:", ft_sort(list))


# 8. Factorial:
"""
Crea una función para calcular el factorial de un número. 
Pide al usuario que ingrese un número y muestra el resultado.
"""

# 9. Conversión de Temperatura:
"""
Implementa funciones para convertir entre Celsius y Fahrenheit. 
Pide al usuario que ingrese la temperatura y la unidad, y luego 
realiza la conversión.
"""

# 10. Juego de Adivinanzas:
"""
Desarrolla un juego simple en el que el programa elige un número aleatorio 
y el jugador tiene que adivinarlo. 
Proporciona pistas sobre si el número es mayor o menor. 
Utiliza funciones para organizar el código.
"""
