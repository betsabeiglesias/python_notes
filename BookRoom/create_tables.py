from app.database import Base, engine
from app.models import *


def create_tables():
    Base.metadata.create_all(bind=engine)

# Reservation.__table__.drop(bind=engine)
# Seat.__table__.drop(bind=engine)


# Seat.__table__.drop(engine)
# Seat.__table__.create(engine)


# Base.metadata.reflect(bind=engine) #Refresca los metadatos en SQLAlchemy después de cambios estructurales

# Base.metadata.drop_all(bind=engine)


if __name__ == "__main__":
    create_tables()