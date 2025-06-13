
from dotenv import load_dotenv
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker
from app.instance.config import Config
from contextlib import contextmanager

load_dotenv()
# DATABASE_URL = os.getenv("DATABASE_URL")

metadata = MetaData()
Base = declarative_base(metadata=metadata)

engine = create_engine(Config.DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



# Crea una fábrica de sesiones: una especie de "molde" que te permite crear sesiones de conexión a la base de datos cuando las necesites.
# sessionmaker(...)
# Es una función de SQLAlchemy que devuelve una clase (no una sesión todavía) con ciertos parámetros predefinidos.

# autocommit=False
# SQLAlchemy no va a hacer commit automáticamente después de cada operación.
# Tú tendrás que hacer db.commit() manualmente cuando quieras guardar los cambios.

# autoflush=False
# SQLAlchemy no va a sincronizar automáticamente los cambios en objetos Python con la base de datos en cada query.
# Lo habitual es dejarlo en False para evitar que se envíen datos parcialmente modificados sin control.


# bind=engine
# “Esta sesión estará conectada al motor engine, que ya tiene la URL de la base de datos PostgreSQL configurada.”

# ¿Y qué es SessionLocal?
# Es una fábrica de sesiones.
# Cuando quieras hacer operaciones contra la base de datos (como en tus endpoints de FastAPI), usarás:
# db = SessionLocal()
# Así puedes hacer:
# db.add(objeto)
# db.commit()
# db.query(Model).filter(...).all()
# Y al terminar, siempre debes cerrar la sesión:
# db.close()