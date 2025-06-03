from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session, sessionmaker
from classes.db import Gestor_BBDD
from modelos_pydantic import *
from typing import Union
from sqlalchemy.exc import IntegrityError
from classes.modelos_alchemy import Usuarios_Alchemy


#IntegrityError es una excepción específica que lanza SQLAlchemy 
# 🔍 ¿Qué significa una “violación de integridad”?
# Son errores típicos del nivel base de datos, como:
# Insertar un registro con una clave primaria ya existente.
# Romper una restricción UNIQUE (por ejemplo, un nombre de usuario único que ya existe).
# Violaciones de FOREIGN KEY (insertar algo que referencia una clave que no existe).



app = FastAPI()
gestor = Gestor_BBDD()
SessionLocal = sessionmaker(bind=gestor.engine)


def get_db():
    db_ses = SessionLocal()
    try:
        yield db_ses
    finally:
        db_ses.close()

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
async def get_material(db_ses:Session = Depends(get_db)):
    try:
        data = gestor.mostrar_catalogo(db_ses)
        return {"materiales": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# ✅ ¿Qué hace Depends() internamente?
# Depends() es un marcador especial.
# Le dice a FastAPI:
# Este argumento no lo proporciona el cliente, ni viene del path, ni de la query, ni del body.
# Este argumento lo tienes que inyectar tú (FastAPI), resolviendo lo que devuelva la función que te paso.
# Por eso db no lo manda nadie en la petición; lo resuelve internamente FastAPI.


@app.get("/material/{id_item}")
async def get_material_unico(id_item: int,db_ses:Session = Depends(get_db)):
    material = gestor.mostrar_material_unico(db_ses, id_item)
    if not material:
        raise HTTPException(status_code=404, detail=f"Material con ID {id_item} no encontrado")
    return {"material": material}


@app.post("/material")
async def post_material(material:Union[LibroCreate, RevistaCreate, DvdCreate], db_ses:Session = Depends(get_db)):
    try:
        if isinstance(material, LibroCreate):
            nuevo = gestor.agregar_material_catalogo(
                db_ses,
                tipo = "libro",
                titulo=material.titulo,
                autor=material.autor,
                extra_data={"paginas": material.paginas}
            )
        elif isinstance(material, RevistaCreate):
            nuevo = gestor.agregar_material_catalogo(
                db_ses,
                tipo="revista",
                titulo=material.titulo,
                autor=material.autor,
                extra_data={"edicion": material.edicion, "fecha publicacion": material.fecha}
            )
        elif isinstance(material, DvdCreate):
            nuevo = gestor.agregar_material_catalogo(
                db_ses,
                tipo="dvd",
                titulo=material.titulo,
                autor=material.autor,
                extra_data={"duracion": material.duracion, "formato": material.formato}
            )
        else:
            raise HTTPException(status_code=400, detail="Tipo de material no válido")
    
        gestor.insertar_material_bbdd(db_ses, nuevo)
        return {"message": f"{material.tipo.capitalize()} '{material.titulo}' agregado correctamente"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# #### **Gestión de usuarios**

# | Método | Ruta             | Descripción                |
# | ------ | ---------------- | -------------------------- |
# | GET    | `/usuarios`      | Listar todos los usuarios  |
# | GET    | `/usuarios/{id}` | Ver detalles de un usuario |
# | POST   | `/usuarios`      | Registrar un nuevo usuario |
# | DELETE | `/usuarios/{id}` | Eliminar un usuario        |


@app.get("/usuarios")
async def get_usuarios(db_ses:Session = Depends(get_db)):
    try:
        data = gestor.mostrar_usuarios(db_ses)
        return {"usuarios": data}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/usuarios")
async def post_usuarios(user: UsuarioCreate, db_ses:Session = Depends(get_db)):
    try:
        # nuevo = gestor.crear_usuario()
        nuevo = Usuarios_Alchemy(nombre=user.nombre)
        gestor.insertar_usuario(db_ses, nuevo)
        return {"message": f"Usuario {nuevo.nombre}' agregado correctamente"}
    except IntegrityError:
        raise HTTPException(status_code=400, detail="El usuario ya existe")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error inesperado: {str(e)}")


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