from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user_schema import UserCreate, UserOut
from app.models.user import User
from app.dependencies import get_db


# APIRouter: para definir rutas agrupadas.
# Depends: para usar dependencias como get_db.
# Session: para interactuar con la base de datos.

router = APIRouter(
    prefix="/user",         # Todas las rutas aquí empiezan por /users
    tags=["User"]           # Para la documentación de Swagger
)

# ¿Por qué UserOut?
# con esto: class User(Base):
#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     nickname = Column(String, unique=True)
#     credit = Column(Integer)
#     rol = Column(Enum(RoleEnum))
# desde el endpoint se hace:return new_user
# Esto devuelve una instancia de SQLAlchemy, que no es serializable directamente a JSON, 
# y puede exponer cosas internas del ORM (como claves foráneas, objetos relacionados, etc).
# Así que con UserOurt: Solo devuelves los campos necesarios.
# Evitas exponer cosas sensibles.
# FastAPI transforma automáticamente el objeto SQLAlchemy (User) en JSON usando ese esquema.


@router.post("/", response_model=UserOut)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    existing_user = db.query(User).filter(User.nickname == user.nickname).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Nickname already registered")
    
    new_user = User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)   # Actualiza el objeto con el ID generado por la base de datos

    return new_user  # FastAPI lo convierte a UserOut automáticamente