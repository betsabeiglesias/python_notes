#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:48:07 2023

@author: laptop
"""

# 1. Contador de números pares e impares:
"""
Escribe un programa que utilice un bucle for o while para contar y mostrar 
la cantidad de números pares e impares en un rango específico, 
por ejemplo, del 1 al 100.
"""
pair = 0
odd = 0
list_pair =list()
list_odd =list()

for i in range(1,101):
    if i % 2 == 0:
        pair += 1
        list_pair.append(i)
    else:
        odd += 1
        list_odd.append(i)
print(f'Hay {pair} números PARES y {odd} IMPARES entre el 1 y el 100')
print(list_pair)
print(list_odd)

# 2. Suma de números primos:
"""
Crea un programa que solicite al usuario un número y utilice un bucle 
while para sumar todos los números primos menores o iguales al número 
ingresado.
"""
number = int(input("Introduce un número: "))

i = 2
count = 0
while i <= number:
    j = 2
    while j <= i // 2:
        if i % j == 0:
            break
        j += 1
    else:
        count += i 
    i += 1
print(f'La suma de los números primos hasta {number} es {count}')





# 3. Tabla de multiplicar:
"""
Pide al usuario que ingrese un número y luego muestra la tabla de 
multiplicar de ese número del 1 al 10 utilizando un bucle for.
"""

number = int(input("Introduce un número: "))


print(f'La tabla de multiplicar del {number}')
for i in range(0, 11):
     print(f'{number} x {i} = {number*i}')





# 4. Generador de patrones:
"""
Escribe un programa que solicite al usuario un número y utilice 
un bucle for o while para generar patrones como el siguiente, donde 
el número ingresado determine la cantidad de filas:
"""
1
22
333
4444
55555

patron = int(input("Introduce un número: "))

for i in range(1,  patron + 1):
    for j in range(i):
        print(i, end="")
    print()

#otra forma de hacerlo
for i in range(1,  patron + 1):
    print(str(i) * i)



# 5. Adivina el número:
"""
Crea un juego en el que el programa genera un número aleatorio y el 
usuario tiene que adivinarlo. Utiliza un bucle while para que el usuario 
pueda seguir intentando hasta que adivine el número. Proporciona pistas 
para indicar si el número a adivinar es mayor o menor que el intento del 
usuario.
"""
from random import randint

guess = randint(0, 100)
print(guess)


# bet = int(input("Introduce un número: "))
while True:
    if bet < guess:
        print(f'El número {bet} introducido es menor que el que tienes que adivinar')
    elif bet > guess:
        print(f'El número {bet} introducido es mayor que el que tienes que adivinar')
    else:
        print('¡HAS ACERTADO!')
        break
    bet = int(input("Inténtalo otra vez: "))

while True:
    bet = int(input("Introduce un número: "))
    if bet < guess:
        print(f'El número {bet} introducido es menor que el que tienes que adivinar')
    elif bet > guess:
        print(f'El número {bet} introducido es mayor que el que tienes que adivinar')
    else:
        print('¡HAS ACERTADO!')
        break