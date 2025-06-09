from app.database import Base
from sqlalchemy import Column, Integer,  String, Date, Boolean, Enum, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship

class Space(Base):
    __tablename__ = 'spaces'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    location = Column(String(30), nullable=False)
    capacity = Column(Integer, nullable=False)
    type = Column(String(30))
    seat = relationship("Seat", back_populates="space")

    # type habrá que cambiarlo a enum

