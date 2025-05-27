Muy buena pregunta. Vamos al grano:

---

### 📌 ¿Qué devuelve `open()` en Python?

La función `open()` devuelve un **objeto archivo** (`file object`), también llamado:

```python
_io.TextIOWrapper
```

Este objeto representa un **canal de comunicación con un archivo** del sistema. Con él puedes:

- Leer el contenido (`read()`, `readline()`, `readlines()`)
- Escribir (`write()`, `writelines()`)
- Recorrer línea a línea con un bucle `for`
- Cerrar el archivo (`close()`), aunque con `with` se hace automáticamente

---

### 🧠 Ejemplo:

```python
archivo = open("datos/poema.txt", "r")
print(type(archivo))
# ⟶ <class '_io.TextIOWrapper'>
```

---

### ✅ ¿Qué métodos tiene ese objeto?

Aquí algunos comunes:

| Método               | Qué hace                                       |
| -------------------- | ---------------------------------------------- |
| `.read()`            | Lee todo el contenido del archivo como `str`   |
| `.readline()`        | Lee solo una línea (hasta el primer `\n`)      |
| `.readlines()`       | Devuelve una lista con todas las líneas        |
| `.write(texto)`      | Escribe `texto` en el archivo (modo escritura) |
| `.writelines(lista)` | Escribe una lista de líneas tal cual           |
| `.close()`           | Cierra el archivo manualmente                  |
| `.seek(n)`           | Mueve el puntero a la posición `n`             |
| `.tell()`            | Devuelve la posición actual del puntero        |

---

### ✅ ¿Cómo se usa normalmente?

```python
with open("archivo.txt", "r") as f:
    contenido = f.read()
```

→ Aquí, `f` es el objeto archivo
→ `f.read()` te da el **contenido como cadena** (`str`)

---

### 🧪 ¿Por qué `.count()` no funciona sobre `f`?

Porque `f` es el archivo, no una cadena.
Si quieres usar `.count()`, primero tienes que hacer:

```python
texto = f.read()
texto.count("palabra")
```

---

¿Quieres que te muestre cómo inspeccionar todos los métodos del objeto `file` con `dir()` o que hagamos una mini clase explicativa de lo que hace `open()` por dentro?
