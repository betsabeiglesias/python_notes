from sqlalchemy import MetaData, Column, Integer,  String, Date, Boolean, Enum, ForeignKey, DateTime, Float
from sqlalchemy.orm import declarative_base, relationship
import enum

metadata = MetaData
Base = declarative_base(metadata=metadata) 
# Base => “Todos mis modelos van a heredar de mí, así sabrás que forman parte del mismo sistema de tablas.”
# Base es la mamá de las tablas, metadata es el libro donde mamá apunta todo

class RoleEnum(str, enum.Enum):
    user = "user"
    admin = "admin"


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    nickname = Column(String(10), nullable=False, unique=True)
    credit = Column(Integer, default=0, nullable=False)
    rol = Column(Enum(RoleEnum), default=RoleEnum.user)