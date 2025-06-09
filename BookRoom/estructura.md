## Estructura del Proyecto: BookRoom (FastAPI + PostgreSQL)

```text
bookroom/                     ← Carpeta raíz del proyecto
|
├── app/                      ← Lógica principal de la aplicación (código backend)
│   ├── models/               ← Modelos SQLAlchemy (User, Seat, Space, Reservation)
│   │   ├── user.py
│   │   ├── seat.py
│   │   ├── space.py
│   │   └── reservation.py
│   |
│   ├── schemas/              ← Esquemas Pydantic para validar entrada/salida
│   │   ├── user_schema.py
│   │   ├── seat_schema.py
│   │   ├── space_schema.py
│   │   └── reservation_schema.py
│   |
│   ├── routers/              ← Rutas / endpoints de la API REST
│   │   ├── user_routes.py
│   │   ├── seat_routes.py
│   │   ├── space_routes.py
│   │   └── reservation_routes.py
│   |
│   ├── database.py           ← Configuración del motor y Base de SQLAlchemy.define `engine`,`Base`, y `SessionLocal`
│   ├── dependencies.py       ← Dependencias inyectables para FastAPI (ej. get_db)
│   └── __init__.py           ← Hace que `app/` sea un paquete Python válido
|
├── venv/                     ← Entorno virtual de Python (no subir a Git)
|
├── .env                      ← Variables de entorno (ej. DATABASE_URL)
├── create_tables.py          ← Script temporal/manual para crear tablas
├── main.py                   ← Punto de entrada de FastAPI (inicia la app)
└── requirements.txt          ← Lista de dependencias instaladas con pip
```
