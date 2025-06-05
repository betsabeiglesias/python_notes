from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session, sessionmaker
from classes.db import Gestor_BBDD
from modelos_pydantic import *
from typing import Union
from sqlalchemy.exc import IntegrityError
from classes.modelos_alchemy import Usuarios_Alchemy
from fastapi.middleware.cors import CORSMiddleware


#IntegrityError es una excepción específica que lanza SQLAlchemy 
# 🔍 ¿Qué significa una “violación de integridad”?
# Son errores típicos del nivel base de datos, como:
# Insertar un registro con una clave primaria ya existente.
# Romper una restricción UNIQUE (por ejemplo, un nombre de usuario único que ya existe).
# Violaciones de FOREIGN KEY (insertar algo que referencia una clave que no existe).


app = FastAPI()
gestor = Gestor_BBDD()
SessionLocal = sessionmaker(bind=gestor.engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # o ["http://127.0.0.1:5500"]
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
            nuevo = gestor.crear_material_catalogo(
                tipo = "libro",
                titulo=material.titulo,
                autor=material.autor,
                extra_data={"paginas": material.paginas}
            )
        elif isinstance(material, RevistaCreate):
            nuevo = gestor.crear_material_catalogo(
                tipo="revista",
                titulo=material.titulo,
                autor=material.autor,
                extra_data={"edicion": material.edicion, "fecha publicacion": material.fecha}
            )
        elif isinstance(material, DvdCreate):
            nuevo = gestor.crear_material_catalogo(
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
    

@app.put("/material/{id_material}")
async def put_material(id_material: int, 
                       cambios: MaterialUpdate,
                       db_ses:Session=Depends(get_db)):
    try:
        extra_data = cambios.model_dump(exclude_unset=True)
        gestor.modificar_material(db_ses, id_material, extra_data)
        return {"message": "✅ Material actualizado correctamente"}
    except Exception as e:
        raise e
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


@app.get("/prestamos")
async def get_prestamos(db_ses:Session = Depends(get_db)):
    try:
        data = gestor.mostrar_prestamos(db_ses)
        return {"prestamos": data}
    except Exception as e:
        print(f"Error al buscar préstamos {e}")

@app.get("/prestamos/{id_prestamo}")
async def get_prestamos(id_prestamo: int, db_ses:Session = Depends(get_db)):
    try:
        data = gestor.mostrar_unico_prestamo(db_ses, id_prestamo)
        return data
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Error interno al buscar préstamo: {str(e)}")


@app.post("/prestamos")
async def post_prestamo(prestamo: PrestamosRequest, db_ses:Session = Depends(get_db)):
    try:
        gestor.prestar_elemento_bbdd(db_ses, prestamo.id_item, prestamo.id_usuario)
        return {"message": "✅ Préstamo registrado correctamente"}
    except HTTPException as e:
        raise # Deja pasar excepciones personalizadas
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Error interno: {str(e)}")
    
@app.put("/prestamos")
async def put_prestamo(update: PrestamoUpdate, db_ses:Session = Depends(get_db)):
    try:
        gestor.actualizar_prestamo(
            session=db_ses,
            id_prestamo=update.id_prestamo,
            fecha_limite=update.fecha_limite,
            devolver=update.devuelto
            )
        return{"message": "✅ Préstamo actualizado correctamente"}
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"❌ Error interno: {str(e)}")
    

# ### **Esquema visual simple**

# /material       --> [GET, POST]
# /material/{id}  --> [GET, PUT, DELETE]

# /usuarios       --> [GET, POST]
# /usuarios/{id} --> [GET, DELETE]

# /prestamos       --> [GET, POST]
# /prestamos/{id} --> [GET, PUT]
# 