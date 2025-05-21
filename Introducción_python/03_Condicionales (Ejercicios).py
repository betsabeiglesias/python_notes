#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 14:45:24 2023

@author: Aitor Donado
"""
from random import sample

# 1. Crear una lista con 10 elementos numéricos.

lista = sample(range(1, 100), 10)
lista


# 2. Comprobar si el tercer elemento es mayor que el séptimo y crear una frase que
# muestre por escrito si el número es mayor o menor y el valor que toma el tercer elemento.

if lista[2] > lista[6]:
    print(f'El número {lista[2]} es mayor que {lista[6]}')
else:
    print(f'El número {lista[2]} es menor que {lista[6]}')


# 3. Invertir el orden de la lista y realizar la misma comprobación.

lista.reverse() #reverse modifica la lista original


if lista[2] > lista[6]:
    print(f'El número {lista[2]} es mayor que {lista[6]}')
else:
    print(f'El número {lista[2]} es menor que {lista[6]}')

#otra opción sin modificar la lista original sería:
lista_reverse = lista[::-1]  # slicing para invertir



# 4. Añadir la posibilidad de que sea igual.

if lista[2] > lista[6]:
    print(f'El número {lista[2]} es mayor que {lista[6]}')
elif lista[2] == lista[6]:
    print(f'El número en la posición 3 es {lista[2]} y es igual al número en la posición 7, que es {lista[6]}')
else:
    print(f'El número {lista[2]} es menor que {lista[6]}')


# 5. Transformar el séptimo número para que se satisfaga la igualdad.
lista[6] = lista[2]


# 6. Realizar la comprobación.
if lista[2] > lista[6]:
    print(f'El número {lista[2]} es mayor que {lista[6]}')
elif lista[2] == lista[6]:
    print(f'El número en la posición 3 es {lista[2]} y es igual al número en la posición 7, que es {lista[6]}')
else:
    print(f'El número {lista[2]} es menor que {lista[6]}')
