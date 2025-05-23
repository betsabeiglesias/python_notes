Aquí tienes el texto formateado en **Markdown**, listo para usar en un README, documento o presentación:

---

# Ejercicios de Repaso

_(Están pensados para ir aumentando ligeramente la complejidad y combinar temas.)_

## Instrucciones Generales

- Intenta resolver cada ejercicio por tu cuenta, con los apuntes y la documentación.
- Prueba tu código con diferentes entradas para asegurarte de que funciona correctamente.
- Si usas LLMs, comprueba dónde puedes aprender más sobre el código generado buscando los métodos usados en la documentación.

### Nota

A medida que resuelvas estos ejercicios, intenta:

- Escribir código limpio y modularizado (con funciones).
- Usar nombres de variables descriptivos.
- Añadir comentarios donde sea necesario para explicar la lógica.

---

## Ejercicio 1: Saludo Personalizado

1. Pide al usuario que ingrese su nombre.
2. Pide al usuario que ingrese su fecha de nacimiento (día/mes/año).
3. Convierte el dato aportado por el usuario en un objeto `datetime`.
4. Calcula la edad del usuario.
5. Muestra un mensaje de bienvenida formateado que incluya su nombre, edad y año de nacimiento.

> Ejemplo: `"¡Hola, [Nombre]! Tienes [Edad] años y naciste en [AñoNacimiento]."`

---

## Ejercicio 2: Operaciones con Cadenas

1. Pide al usuario que ingrese una frase.
2. Muestra:

   - La longitud de la frase.
   - La frase en mayúsculas.
   - La frase en minúsculas.
   - Las tres primeras letras de la frase.
   - Las tres últimas letras de la frase.
   - La frase con todas las 'a' reemplazadas por una 'e'.

---

## Ejercicio 3: Información de Contacto (Diccionario)

1. Crea un diccionario llamado `contacto` que almacene:

   - `nombre`: (pide al usuario que lo ingrese)
   - `telefono`: (pide al usuario que lo ingrese)
   - `email`: (pide al usuario que lo ingrese)

2. Muestra la información del contacto de forma clara, por ejemplo:
   `"Nombre: Juan, Teléfono: 123456789, Email: juan@example.com"`

3. Pregunta al usuario si quiere añadir una ciudad al contacto. Si es así, pídela y añádela al diccionario.

4. Muestra todas las claves (`keys`) del diccionario.

5. Muestra todos los valores (`values`) del diccionario.

---

## Ejercicio 4: Elementos Únicos (Sets)

1. Crea una lista con elementos duplicados, por ejemplo:
   `numeros = [1, 2, 2, 3, 4, 4, 4, 5]`
2. Convierte esta lista a un `set` para eliminar los duplicados.
3. Muestra el `set` resultante.
4. Crea otro `set` con algunos números, por ejemplo:
   `otros_numeros = {4, 5, 6, 7}`
5. Muestra la **unión** de ambos sets.
6. Muestra la **intersección** de ambos sets.

---

## Ejercicio 5: Menú de Opciones (con `match`)

1. Muestra un menú de opciones al usuario:

   1. Escribir texto en un archivo
   2. Mostrar el texto escrito en un archivo
   3. Mostrar fecha actual
   4. Salir del programa

2. Pide al usuario que elija una opción (1, 2 o 3).

3. Usa una estructura `match-case` para ejecutar la acción correspondiente.

4. Si la opción no es válida, muestra un mensaje de error.

---

## Ejercicio 6: Lista de la Compra

1. Crea una lista vacía llamada `lista_compra`.
2. Pide al usuario que ingrese 5 productos para añadir a la lista.
3. Muestra la lista completa.
4. Pregunta al usuario si quiere eliminar algún producto. Si dice que sí, pregúntale cuál y elimínalo.
5. Muestra la lista final.
6. Indica cuántos productos quedan en la lista.
7. Mantén sincronizada la lista con un archivo `tareas.txt`.
8. Utiliza el bloque `with open(...)` para asegurar que los archivos se cierren correctamente.
9. Utiliza `try-except` para manejar posibles `FileNotFoundError` si el archivo no existe (en ese caso, informa que no hay tareas).

---

## Desafío: Contador de Palabras en un Archivo

1. Pide al usuario el nombre de un archivo de texto.
2. Lee el contenido del archivo.
3. Limpia el texto: conviértelo a minúsculas y elimina signos de puntuación básicos (puedes usar `.replace()` para comas, puntos, etc.).
4. Divide el texto en palabras.
5. Usa un diccionario para contar la frecuencia de cada palabra.
6. Muestra las 10 palabras más frecuentes y su conteo.
7. Maneja la excepción `FileNotFoundError`.

---

¿Te gustaría que te lo exporte como `.md` para que lo copies fácilmente a un repositorio?
