###############
# Decoradores #
###############
# Un decorador es una funcion que se dedica a modificar el resultado de otra función
# Tiene que recibir esa función como parámetro

def funcion_fea():
    return "deVUelVO aLgO FeO"

def funcion_camafeo():
    return "TENGO UN CAMAFEO"

def decoradora(funcion_poco_agraciada):
    def decorada():
        resultado_feo = funcion_poco_agraciada()
        resultado_bonito = resultado_feo.capitalize().replace("feo", "bonito")
        return resultado_bonito
    return decorada

funcion_fea()

funcion_fea_decorada = decoradora(funcion_fea)

funcion_fea_decorada()


funcion_camafeo_decorada = decoradora(funcion_camafeo)

funcion_camafeo_decorada()

funcion_fea()
funcion_camafeo()

# Lo bueno es que la función decoradora es reutilizable para cualquier otra 
# función que devuelva algo feo
@decoradora
def devuelvo_algo_feo():
    return "He hErEdaDO un CaMafeo mUy fEO"

devuelvelo_decorado = decoradora(devuelvo_algo_feo)
devuelvelo_decorado()

devuelvo_algo_feo()

# Representación compacta de una función decoradora
def decoradora(funcion_fea):
    def decorada():
        resultado_feo = funcion_fea()
        resultado_bonito = resultado_feo.capitalize().replace("feo", "bonito")
        return resultado_bonito
    return decorada


# Si declaro la decoradora inmediatamente sobre la definición de la funcion fea...
@decoradora
def funcion_fea():
    return "deVUelVO aLgO FeO"

# ésta se comporta siempre como la función decorada
funcion_fea()

# Lógicamente, las funciones decoradoras no están para modificar strings feos
# El objetivo es poder centrarse en operaciones en la "funcion_fea" y usar la
# decoradora para tratar entradas o salidas.


"""
# Esquema en pseudocódigo de una función decoradora

def funcion_decoradora(funcion_a_decorar):
    def funcion_decorada(parametro_1, parametro_2):
        parametro_1 = transformacion_entrada(parametro_1)
        parametro_2 = transformacion_entrada(parametro_2)
        resultado = funcion_a_decorar(parametro_1, parametro_2)
        resultado = transformacion_salida(resultado)
        return resultado
    return funcion_decorada
"""


# Ejemplo, controlar la entrada a una función
# Ahora la función fea es esta división que devuelve error con y = 0

def division(x, y):
    return x/y

division(8,0)

def comprueba_entradas(func):
    def comprobacion(x, y):
        if y == 0:
            return "La entrada de datos no es correcta"
        else:
            resultado = func(x, y)
            return resultado
    return comprobacion


@comprueba_entradas
def division(x, y):
    return x/y

division(1,0)


def comprueba_entradas(func):
    def comprobacion(x, y, mensaje):
        if y == 0:
            return "La entrada de datos no es correcta"
        else:
            resultado = func(x, y, mensaje)
            return resultado
    return comprobacion


@comprueba_entradas
def division_y_print(x, y, mensaje):
    print(mensaje)
    return x/y


division_y_print(2, 0)
division_y_print(2, 0, "Hola")

# La clave de definir bien un decorador es que reciba una función y devuelva
# otra función declarada dentro de ella y que añada algo a la recibida

# Función decoradora que se asegura de que una edad esté bien introducida
def corrige_datos(func):
    def corrector():
        edad = func()
        if not edad.isdigit():
            return "Error. Debes introducir un número"
        else:
            edad_entera = int(edad)
            if not (0 <= edad_entera <= 120):
                return("Edad fuera de los límites")
            else:
                return edad_entera
    return corrector


@corrige_datos
def introduce_edad():
    edad = input("Introduce tu edad: ")
    return edad


@corrige_datos
def introduce_area_garaje():
    edad = input("Introduce el área del garaje: ")
    return edad

introduce_edad()
introduce_area_garaje()


def comprueba_params(func):
    def comprobadora(x, y):
        if type(x) is str:
            x_verificada = x
        else:
            return "La primera variable no es un string"
        if type(y) is int:
            y_verificada = y
        else:
            return "La segunda variable no es un entero"
        return func(x_verificada, y_verificada)
    return comprobadora


@comprueba_params
def multiplica_texto(texto, num):
    return num * texto


multiplica_texto("Hola", "Mundo")
multiplica_texto(2, "Mundo")
multiplica_texto("Hola", 3)


#Ejemplo: Decorador de Tiempo de Ejecución

import time
inicio = time.time()
fin = time.time()
tiempo_transcurrido = fin - inicio


def medir_tiempo(func):
    def funcion_medida(mensaje):
        mensaje = mensaje.replace("Hola", "Adiós")
        inicio = time.time()
        salida = func(mensaje)
        final = time.time()
        print(f"Tiempo de ejecución de la función {func.__name__}, {final - inicio} segundos")
        salida = salida.upper()
        return salida
    return funcion_medida


def medir_tiempo(func):
    def funcion_medida(**mensaje):
        inicio = time.time()
        for elemento in mensaje:
            print(elemento)
        salida = func(**mensaje)
        final = time.time()
        print(f"Tiempo de ejecución de la función {func.__name__}, {final - inicio} segundos")
        return salida
    return funcion_medida

@medir_tiempo
def ejemplo(m1, m2, m3):
    time.sleep(1)
    return m2

ejemplo(m1 = "Hola", m2 = "Adios", m3 = "Hasta Luego")

@medir_tiempo
def ejemplo3(mensaje):
    time.sleep(3)
    return mensaje

ejemplo3("Hola que tal")
ejemplo3("Hola como estás")


#Ejercicio 2: Decorador de Validación de Parámetros
"""
Crea un decorador llamado validar_parametros que tome una función y verifique si los parámetros 
cumplen ciertas condiciones antes de llamar a la función. 

Por ejemplo, puedes implementar una validación que asegure que los números ingresados son positivos.
"""


def validar_parametros(func):
    def validando_parametros(num):
        if not isinstance(num, (float, int)):
            raise ValueError ("El parámetro deber ser un número")
        if (num) < 0:
            print(f"El numero {num} no lo puedo usar")
            return
        return func(num)
    return validando_parametros


@validar_parametros
def print_num(num):
    return num


print_num(3)
print_num(-5)


def validar_varios_parametros(func):
    def validando_varios_parametros(*args):
        numeros_invalidos = [arg for arg in args if arg < 0]
        if numeros_invalidos:
            for num in numeros_invalidos:
                print(f"El número {num} no lo puedo usar")
                # raise ValueError ("El número debe ser positivo")
            return
        return func(*args)
    return validando_varios_parametros

@validar_varios_parametros
def print_varios_num(*num):
    return num


print_varios_num(5, -3, 8, 100, -55)


#Ejercicio 3: Decorador para Logs
"""
Implementa un decorador llamado registro que registre información sobre la llamada a la función, 
como el nombre de la función, los argumentos y el resultado. Imprime esta información en la consola 
cada vez que la función decorada se ejecuta.
"""

def registro_funcion(func):
    def registrando_ft(*args, **kwargs):
        print(f"El nombre de: {func.__name__}")
        print(f"Argumentos posicionales: {args}")
        print(f"Argumentos nombrados: {kwargs}")
        resultado = func(*args, **kwargs)
        print(f"El resultado es: {resultado}")
        return resultado
    return registrando_ft


@registro_funcion
@validar_varios_parametros
def print_varios_num(*num):
    return num


print_varios_num(5, -3, 8, 100, -55)



# Ejercicio 4: Decorador de Validación de Salida
"""
Construir un decorador que compruebe que la salida de una función sea un número
"""


def comprobar_salida(func):
    def comprobando_salida(arg):
        resultado = func(arg)
        if not isinstance(resultado, int):
            return print(f"El resultado: {resultado} NO es un número")
        return resultado
    return comprobando_salida

@comprobar_salida
def ft_test(option):
    if option == 1:
        return 5*2
    else:
        return ("esto es una string")


ft_test(1)
ft_test(10)



def comprobar_varias_salidas(func):
    def wrapper(*arg):
        resultado = func(*arg)
        if not isinstance(resultado, int):
            return print(f"El resultado: {resultado} NO es un número")
        return resultado
    return wrapper

@comprobar_varias_salidas
def ft_test2(*arg):
    if arg[0] == 1 and arg[1] == 2:
        return 3*5
    else:
        return "Soy una string"
    

ft_test2(1,2)
ft_test2(3,2)
ft_test2(1,2)
ft_test2(1,100)
    




