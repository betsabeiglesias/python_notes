### 🧠 1. **Definir el Alcance (Scope)**

Antes de tocar código, aclaremos:

* ¿Qué puede hacer un usuario? (reservar, cancelar, ver)
* ¿Quién gestiona los espacios? (¿hay rol admin?)
* ¿Qué datos mínimos necesita cada entidad?


---

### 🧱 2. **Diseñar el Modelo de Datos (entidades y relaciones)**

Haz un pequeño diagrama o lista de tablas:



* El `Usuario` podrá:
- Ver los espacios
- Reservar
- Cancelar

Datos usuario: id, nombre, nickname, saldo en horas, rol.

Habrá un administrador que tendrá superpoderes para:
- ver todos los espacios y reservas
- cancelar y modificar reservas
- gestionar espacios (añadir, editar)
No necesito crear una tabla separada. Basta con que el admin sea un usuario con rol = 'admin'

`Espacio`, datos:
- id
- nombre
- ubicación
- capacidad total
- tipo(Estudio, reunión, silencio)
- disponible


`Seat`, datos:
- id
- número
- disponibilidad
- espacio id


`Reserva`:
- id
- id usuarios (FK)
- id espacio (FK)
- fecha incio, fecha fin (con hora)
- estado: activa, cancelada, modificada
- modificada_por_admin (bool)

---

### 📦 3. **Organizar el Proyecto**


```
bookroom/                     ← Carpeta raíz del proyecto
│
├── app/                      ← Lógica principal de la aplicación (código backend)
│   ├── models/               ← Modelos SQLAlchemy (User, Seat, Space, Reservation)
│   │   ├── user.py
│   │   ├── seat.py
│   │   ├── space.py
│   │   └── reservation.py
│   │
│   ├── schemas/              ← Esquemas Pydantic para validar entrada/salida
│   │   ├── user_schema.py
│   │   ├── seat_schema.py
│   │   ├── space_schema.py
│   │   └── reservation_schema.py
│   │
│   ├── routers/              ← Rutas / endpoints de la API REST
│   │   ├── user_routes.py
│   │   ├── seat_routes.py
│   │   ├── space_routes.py
│   │   └── reservation_routes.py
│   │
│   ├── database.py           ← Configuración del motor y Base de SQLAlchemy
│   ├── dependencies.py       ← Dependencias inyectables para FastAPI (ej. get_db)
│   └── __init__.py           ← Hace que `app/` sea un paquete Python válido
│
├── venv/                     ← Entorno virtual de Python (no subir a Git)
│
├── .env                      ← Variables de entorno (ej. DATABASE_URL)
├── create_tables.py          ← Script temporal/manual para crear tablas
├── main.py                   ← Punto de entrada de FastAPI (inicia la app)
└── requirements.txt          ← Lista de dependencias instaladas con pip


---

### ⚙️ 4. **Configurar el entorno**

* Crear entorno virtual: `python -m venv venv`
* Instalar FastAPI, Uvicorn, SQLAlchemy, Pydantic, etc.

```bash
pip install fastapi uvicorn sqlalchemy pydantic psycopg2-binary pymongo
```

* Crear tu archivo `.env` con la cadena de conexión.

---

### 🚀 5. **Desarrollar por módulos**

Empieza por los modelos + endpoints más esenciales:

1. 🔐 **Usuarios**

   * Crear usuario
   * Obtener usuarios
2. 🧩 **Espacios**

   * Añadir, listar, filtrar por disponibilidad
3. 📅 **Reservas**

   * Crear reserva
   * Ver reservas por usuario
   * Cancelar/modificar

---


### 🧪 **CREACION DATABASE POSTGRESQL**
postgres=# CREATE DATABASE library_space;
CREATE DATABASE
postgres=# CREATE USER lib_user WITH PASSWORD '123';
CREATE ROLE
postgres=# GRANT ALL PRIVILIGES ON DATABASE library_space TO lib_user;
ERROR:  syntax error at or near "PRIVILIGES"
LINE 1: GRANT ALL PRIVILIGES ON DATABASE library_space TO lib_user;



### 🧪 6. **Testear desde el principio**

Usa Swagger de FastAPI (`http://localhost:8000/docs`) para ir comprobando los endpoints.

---

### 📓 7. **Documentar**

Ve escribiendo en el `README.md`:

* Cómo instalarlo
* Qué hace
* Ejemplos de uso

---

### 🧠 Consejo extra:

Empieza sencillo. No intentes hacer todo a la vez. Con tener bien hecho el CRUD de usuarios, espacios y reservas, ya es un gran proyecto. Luego puedes ir añadiendo Mongo para logs, feedback, estadísticas, etc.

---

¿Quieres que empecemos ya con el primer archivo del proyecto (por ejemplo `database.py` o los modelos)?


¡Muy buena duda! Vamos a aclararlo con claridad práctica: **¿para qué sirve `app/database.py` en tu proyecto?**

---

## 📁 `app/database.py`: el corazón de la base de datos

Este archivo te sirve para **centralizar y controlar toda la configuración de SQLAlchemy** en un solo lugar. Incluye:

---

### ✅ 1. **`Base` y `metadata`**

```python
from sqlalchemy.orm import declarative_base
from sqlalchemy import MetaData

metadata = MetaData()
Base = declarative_base(metadata=metadata)
```

* Todos tus modelos (`User`, `Space`, `Reservation`) **heredan de `Base`**.
* SQLAlchemy usa `Base.metadata` para **crear todas las tablas de golpe**.

---

### ✅ 2. **Conexión al motor de la base de datos**

Más adelante, aquí crearás el **engine** y la **sesión de base de datos**:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./test.db"  # o PostgreSQL, etc.

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
```

Esto te permite:

* Conectarte a la base de datos
* Crear sesiones para hacer queries
* Ejecutar `Base.metadata.create_all(engine)` para **crear todas las tablas**

---

### ✅ 3. **Inicializar la base de datos**

También usarás este archivo para crear las tablas:

```python
# al final de database.py o en un script aparte
from app.models import user, space, reservation

Base.metadata.create_all(bind=engine)
```

> ⚠️ Es importante importar todos los modelos antes de llamar a `create_all` para que se registren.

---

### 💡 En resumen: ¿para qué sirve `app/database.py`?

| Función                           | ¿Por qué es útil?                          |
| --------------------------------- | ------------------------------------------ |
| Define `Base`                     | Para que todos los modelos hereden de ella |
| Define `engine` y `SessionLocal`  | Para conectarte a la base de datos         |
| Centraliza la configuración       | Para no repetir código en cada modelo      |
| Inicializa la BBDD (`create_all`) | Para crear todas las tablas de golpe       |

---

