from app.database import SessionLocal
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import Generator

def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# FastAPI usa el yield para trabajar con "dependencias de duración controlada".
# FastAPI ejecuta get_db() hasta el yield → y usa ese db en tu endpoint.
# Cuando el endpoint termina, FastAPI vuelve a entrar en la función y ejecuta el finally.


# Explicación de Generator[Session, None, None]:
# Session: lo que devuelve el yield
# None: no usamos send() en este caso
# None: la función no retorna nada al final


# ¿Qué es una función generadora en Python?
# Una función generadora es una función que en lugar de usar return usa yield.
# Cuando usas yield, la función no devuelve un valor y termina, sino que pausa su ejecución y guarda su estado para retomarlo más tarde.
# Para qué sirve?
# Para producir valores uno a uno (muy útil con listas grandes o infinitas).
# Para hacer flujos controlados, como FastAPI con get_db().
# Ejemplo básico:
# def contar_hasta_3():
#     yield 1
#     yield 2
#     yield 3

# for numero in contar_hasta_3():
#     print(numero)