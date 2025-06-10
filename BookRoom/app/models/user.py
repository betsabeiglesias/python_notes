from sqlalchemy import Column, Integer,  String, Enum as SQLAEnum
from sqlalchemy.orm import relationship
from app.database import Base
from app.models.enums import RoleEnum


# Base => “Todos mis modelos van a heredar de mí, así sabrás que forman parte del mismo sistema de tablas.”
# Base es la mamá de las tablas, metadata es el libro donde mamá apunta todo


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    nickname = Column(String(10), nullable=False, unique=True)
    credit = Column(Integer, default=0, nullable=False)
    rol = Column(SQLAEnum(RoleEnum), default=RoleEnum.user)

    reservation = relationship("Reservation", back_populates="user")

