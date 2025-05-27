# Expresiones regulares
"""
Las expresiones regulares son como una especie de mini lenguaje dentro de otro lenguaje de programación

Son secuencias de caracteres que forman un patrón que sirve para realizar búsquedas de texto.

Es importante conocerlas ya que en muchas ocasiones nos vamos a ver en la necesidad de buscar un mismo texto escrito de formas diferentes, o bien textos similares.
"""

import re
help(re)
# 'q' para salir si se ejecuta en spyder
# La traducción de esta ayuda está en la celda de abajo

"""## Los caracteres especiales para los patrones son:
(**Greedy** = **codicioso** significa que coincidirá con tantas repeticiones como sea posible.)
```
    "." Coincide con cualquier carácter excepto salto de línea.
    "^" Coincide con el inicio de la cadena.
    "$" Coincide con el final de la cadena o justo antes del salto de línea.

    "*"      Coincide con 0 o más repeticiones (codiciosos) de la ExpReg anterior.
    "+"      Coincide con 1 o más repeticiones (codiciosos) de la ExpReg anterior.
    "?"      Coincide con 0 o 1 (codicioso) de la ExpReg anterior.
    *?,+?,?? Versiones no codiciosas de los tres caracteres especiales anteriores.

    {m,n} Coincide con desde m a n repeticiones de la ExpReg anterior.
    {m,n}? Versión no codiciosa de lo anterior.
    "\\" Escapa caracteres especiales o señala una secuencia especial.
    [] Indica un conjunto de caracteres.
        Un "^" como primer carácter indica un conjunto complementario (es decir, los caracteres que NO estén entre los corchetes).
    "|" A|B, crea una ExpReg que coincidirá con A o B.
    (...) Coincide con la ExpReg dentro de los paréntesis.
    El contenido se puede recuperar o comparar más adelante en la cadena.
    (?aiLmsux) Las letras establecen las banderas correspondientes definidas a continuación.
    (?:...) Versión no agrupada de paréntesis regulares.
    (?P<nombre>...) La subcadena que coincide con el grupo es accesible por nombre.
    (?P=nombre) Coincide con el texto que coincidía anteriormente con el nombre del grupo.
    (?#...)  Un comentario; ignorado
    (?=...) Coincide si... coincide con el siguiente, pero no consume la cadena.
    (?!...) Coincide si... no coincide con el siguiente.
    (?<=...) Coincide si está precedido por... (debe ser de longitud fija).
    (?<!...) Coincide si no está precedido por... (debe ser de longitud fija).
    (?(id/nombre)yes|no) Coincide con el patrón sí si el grupo con id/nombre coincide,
        el (opcional) sin patrón de lo contrario.
```

    Las secuencias especiales constan de "\\" y un carácter de la lista
    abajo. Si el carácter ordinario no está en la lista, entonces la ExpReg resultante coincidirá con el segundo carácter.
        \number Coincide con el contenido del grupo del mismo número.
        \A Coincide solo al comienzo de la cadena.
        \Z Coincide solo al final de la cadena.
        \b Coincide con la cadena vacía, pero solo al principio o al final de una palabra.
        \B Coincide con la cadena vacía, pero no al principio ni al final de una palabra.
        \d Coincide con cualquier dígito decimal; equivalente al conjunto [0-9] en
                patrones de bytes o patrones de cadena con la bandera ASCII.
                En patrones de cadena sin la bandera ASCII, coincidirá con todo el
                rango de dígitos Unicode.
        \D Coincide con cualquier carácter que no sea un dígito; equivalente a [^\d].
        \s Coincide con cualquier carácter de espacio en blanco; equivalente a [\t\n\r\f\v] en
                patrones de bytes o patrones de cadena con la bandera ASCII.
                En patrones de cadena sin la bandera ASCII, coincidirá con todo el
                intervalo de caracteres de espacio en blanco Unicode.
        \S Coincide con cualquier carácter que no sea un espacio en blanco; equivalente a [^\s].
        \w Coincide con cualquier carácter alfanumérico; equivalente a [a-zA-Z0-9_]
                en patrones de bytes o patrones de cadena con la bandera ASCII.
                En patrones de cadenas sin el indicador ASCII, coincidirá con el
                rango de caracteres alfanuméricos Unicode (letras más dígitos
                más guión bajo).
                Con LOCALE, coincidirá con el conjunto [0-9_] más los caracteres definidos
                como letras para la configuración regional actual.
        \W Coincide con el complemento de \w.
        \\ Coincide con una barra invertida literal.

[Web para probar expresiones regulares](https://regex101.com/)

Este módulo exporta las siguientes funciones:


*   **match**: Coincide con un patrón de expresión regular al comienzo de una cadena.
*   **fullmatch**: Coincide con un patrón de expresión regular con toda una cadena.
*   **search**: Busca en una cadena la presencia de un patrón.
*   **findall**: Encuentra todas las apariciones de un patrón en una cadena.
*   **finditer**: Devuelve un iterador que genera un objeto Match para cada coincidencia.
*   **split**: Dividir una cadena por las ocurrencias de un patrón.
*   **sub**: Sustituye las ocurrencias de un patrón encontrado en una cadena.
*   **subn**: Igual que sub, pero también devuelve el número de sustituciones realizadas.
*   **escape**: Como colocar una barra invertida en todos los no alfanuméricos en una cadena.
*   **compile**: Compila un patrón en un objeto Pattern.
*   **purge**: Limpia la caché de expresiones regulares.
"""

# Creación de patrones
"""
En este patrón las **s** son opcionales. Es opcional que se use la **o** o la **a** pero una de las dos debe estar presente.
"""

patron = r"mis? gat[o,a]s?"
texto = "mi gatos y tus gatas son bonitos"

# match
"""
Busca el patrón exclusivamente al principio del texto.
"""
# texto = "A mis gatos"
if re.match(patron, texto):
    print("Se encontró una coincidencia al inicio del texto")
else:
    print("No se encontró una coincidencia al inicio del texto")

x = re.match(patron, texto)
x.pos, x.endpos, x.re, x.string, x.start(), x.end(), x.span()

type(x)

dir(x)

"""los métodos `group`, `groupdict`, `groups`, `lastgroup` se usan cuando el patrón tiene grupos."""

resultado = re.match(r'(?P<saludo>\w+) (?P<nombre>\w+)', 'Hola Mundo')
resultado.group(), resultado.groupdict(), resultado.groups(), resultado.lastgroup

resultado = re.search(r'(?P<saludo>\w+) (?P<nombre>\w+)', '~~  Hola Mundo  ')
resultado.group(), resultado.groupdict(), resultado.groups(), resultado.lastgroup

# fullmatch
"""
Todo el texto se debe ajustar al patrón introducido
"""
patron = r"mi gat[o,a]s? y tus gat[o,a]s? son bonitos"
texto = "mi gatos y tus gatas son bonitos"

# texto = "mi gatos y tus gatas son bonitos."
if re.fullmatch(patron, texto):
    print("Se encontró una coincidencia exacta del texto")
else:
    print("No se encontró una coincidencia exacta del texto")

"""Observamos la salida del método `fullmatch`"""

x = re.fullmatch(patron, texto)
x.pos, x.endpos, x.re, x.string, x.start(), x.end(), x.span()

dir(x)


# search
patron = r"gat[o,a]s?"
texto = "mi gatos y tus gatas son bonitos"
x = re.search(patron, texto)

"""Posiciones inicial y final de **la primera coincidencia**"""

x.regs

((inicio, fin),) = x.regs

print("Inicio:", inicio)
print("Fin:", fin)

dir(x)

x.group(0), x.groupdict(), x.groups(), x.lastgroup, x.lastindex, x.pos, x.endpos, x.span(), x.start(), x.end()

"""
Podemos recuperar el string en el que estamos buscando y el patrón que hemos usado
"""

x.string, x.re

# findall
"""
Devuelve los substrings coincidentes
"""

patron = r"gat[o,a]s?"
texto = "mi gatos y tus gatas son bonitos"

lista_ocurrencias = re.findall(patron, texto)

lista_ocurrencias

# finditer
"""
Devuelve los substrings coincidentes
"""

patron = r"gat[o,a]s?"
texto = "mi gatos y tus gatas son bonitos"

iterable_ocurrencias = re.finditer(patron, texto)

next(iterable_ocurrencias).span()


# split
"""
Corta el string usando el patrón
"""

lista_cortada = re.split(patron, texto)

lista_cortada

# sub y subn
patron = r'gat'
x = re.sub(patron, "perr", texto)
x, veces = re.subn(patron, "perr", texto)

# escape
"""
Si alguno de los caracteres que se utilizan para escribir patrones fuera objeto de búsqueda debería "escaparlos" con la barra inclinada a la derecha "\". Usando `escape` me ahorro el esfuerzo.
"""

texto = "La cadena a buscar es: $a*b."

"""
Escapa los caracteres especiales de la cadena de búsqueda
"""

cadena_busqueda = re.escape("$a*b.")
patron = " es: " + cadena_busqueda

"""
Busca la cadena de búsqueda en el texto
"""

resultado = re.search(patron, texto)
((inicio, fin),) = resultado.regs
resultado.group()

resultado.re

# compile
"""
Los patrones pueden ser tan complejos y largos que para comprobar si un patrón ha sido correctamente creado, se compila
"""

patron_email = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')

if re.fullmatch(patron_email, "aitor.donado@gmail.com"):
    print("Es correcto")
else:
    print("Email incorrecto")


"""Usando una función."""
def validar_email(email, patron_email):
    print(re.fullmatch(patron_email, email))
    return re.fullmatch(patron_email, email) is not None

if validar_email("aitor.donado@gmail.com", patron_email):
    print("Es correcto")
else:
    print("Email incorrecto")


# Ejemplo
"""
Extraer todos los números de una cadena y mostrarlos como una lista.
Cadena de entrada
"""
texto = "La temperatura es 25 grados Centígrados y el precio es 19.99€."

"""
Patrón para encontrar números
"""
patron_numeros = r'\d+'
patron_num_decimales = r'\d+\.\d+|\d+'

"""
El orden importa (prioridad)
"""
patron_num_decimales = r'\d+|\d+\.\d+'

"""
Extraer números de la cadena
"""
numeros_encontrados = re.findall(patron_num_decimales, texto)

"""
Mostrar los números encontrados
"""
print("Números encontrados:", numeros_encontrados)