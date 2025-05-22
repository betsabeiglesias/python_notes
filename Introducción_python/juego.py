from random import randint

def adivina_numero():
    numero_aleatorio = randint(0, 100)

    # Pedir al usuario que adivine el número
    while True:
        intento = int(input("Adivina el número (entre 1 y 100): "))
        if intento == numero_aleatorio:
            print("¡Correcto! Adivinaste el número.")
            break
        elif intento < numero_aleatorio:
            print("El número a adivinar es mayor que", intento)
        else:
            print("El número a adivinar es menor que", intento)
