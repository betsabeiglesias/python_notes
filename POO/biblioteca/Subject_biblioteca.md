# Ejercicio POO

## Caso de uso de programación orientada a objetos (POO) que involucra herencia, encapsulamiento y polimorfismo.

---

## Sistema de Gestión de Biblioteca

### Descripción:

Crea un sistema para gestionar una biblioteca.  
El sistema debe permitir la gestión de diferentes tipos de materiales de la biblioteca, como **libros**, **revistas** y **DVDs**.  
Cada tipo de material tendrá atributos y métodos específicos, pero todos deben compartir algunos atributos y métodos comunes.

---

## Requisitos:

### 1. Clases Abstractas:

- Define una clase abstracta `MaterialBiblioteca` que contenga atributos y métodos comunes a todos los materiales de la biblioteca.
- Incluye al menos un método abstracto que deba ser implementado por las subclases.

### 2. Herencia:

- Crea subclases para cada tipo de material (`Libro`, `Revista`, `DVD`) que hereden de la clase `MaterialBiblioteca`.
- Cada subclase debe implementar los métodos abstractos y puede agregar atributos y métodos específicos.

### 3. Encapsulamiento:

- Utiliza encapsulamiento para proteger los atributos de las clases, proporcionando métodos **getters** y **setters** según sea necesario.

### 4. Métodos Comunes:

- Implementa métodos comunes como `mostrar_info` que varíen según el tipo de material.

### 5. Polimorfismo:

- Utiliza polimorfismo para permitir que diferentes tipos de materiales sean tratados de manera uniforme en ciertas operaciones.

### 6. Interfaz de Usuario:

- Crea una interfaz de usuario simple (por ejemplo, un menú en la consola) que permita al usuario:
  - Agregar materiales.
  - Listar materiales.
  - Mostrar información detallada de un material específico.

---

## Pasos para la Resolución del Ejercicio

### 1. Definir la Clase Abstracta `MaterialBiblioteca`

- **Atributos comunes**: `titulo`, `autor`, `codigo_inventario`.
- **Métodos comunes**: `mostrar_info` (método abstracto).

---

### 2. Crear Subclases para Cada Tipo de Material

#### Libro:

- Atributos adicionales: `numero_paginas`.
- Implementar el método `mostrar_info`.

#### Revista:

- Atributos adicionales: `numero_edicion`, `fecha_publicacion`.
- Implementar el método `mostrar_info`.

#### DVD:

- Atributos adicionales: `duracion`, `formato`.
- Implementar el método `mostrar_info`.

---

### 3. Implementar Encapsulamiento

- Proteger los atributos con `__` (doble guion bajo) y proporcionar métodos **getters** y **setters**.

---

### 4. Utilizar Polimorfismo

- Crear una lista de materiales de la biblioteca que pueda contener instancias de `Libro`, `Revista` y `DVD`.
- Implementar una función que recorra la lista y llame al método `mostrar_info` en cada material, aprovechando el polimorfismo.

---

### 5. Crear la Interfaz de Usuario

Menú principal con opciones para:

- Agregar un nuevo material (libro, revista o DVD).
- Listar todos los materiales en la biblioteca.
- Mostrar información detallada de un material específico.
- Salir del programa.
