from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from classes.db import Gestor_BBDD

app = FastAPI()
gestor = Gestor_BBDD()

def get_db():
    db = gestor.Session()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
async def root():
    return {"message": "Hola caracola\n"}


# #### **Rutas generales**

# | Método | Ruta    | Descripción                             |
# | ------ | ------- | --------------------------------------- |
# | GET    | `/`     | Mensaje de bienvenida (“Hola caracola”) |
# | GET    | `/docs` | Documentación interactiva (Swagger UI)  |


# #### **Gestión de Material**

# | Método | Ruta           | Descripción                         |
# | ------ | -------------- | ----------------------------------- |
# | GET    | `/material`      | Listar todos los materiales             |
# | GET    | `/material/{id}` | Obtener detalles de un material por ID |
# | POST   | `/material`      | Añadir un material libro               |
# | PUT    | `/material/{id}` | Actualizar información de un material  |
# | DELETE | `/material/{id}` | Eliminar un material                   |


@app.get("/material")
async def get_material(db:Session = Depends(get_db)):
    try:
        data = gestor.mostrar_catalogo(db)
        return {"materiales": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))





# #### **Gestión de usuarios**

# | Método | Ruta             | Descripción                |
# | ------ | ---------------- | -------------------------- |
# | GET    | `/usuarios`      | Listar todos los usuarios  |
# | GET    | `/usuarios/{id}` | Ver detalles de un usuario |
# | POST   | `/usuarios`      | Registrar un nuevo usuario |
# | DELETE | `/usuarios/{id}` | Eliminar un usuario        |


# #### **Gestión de préstamos**

# | Método | Ruta              | Descripción                                     |
# | ------ | ----------------- | ----------------------------------------------- |
# | GET    | `/prestamos`      | Listar todos los préstamos                      |
# | GET    | `/prestamos/{id}` | Ver detalles de un préstamo                     |
# | POST   | `/prestamos`      | Registrar un nuevo préstamo                     |
# | PUT    | `/prestamos/{id}` | Actualizar estado (por ejemplo, devolver libro) |


# ### **Esquema visual simple**


# /material       --> [GET, POST]
# /material/{id}  --> [GET, PUT, DELETE]

# /usuarios       --> [GET, POST]
# /usuarios/{id} --> [GET, DELETE]

# /prestamos       --> [GET, POST]
# /prestamos/{id} --> [GET, PUT]
# 