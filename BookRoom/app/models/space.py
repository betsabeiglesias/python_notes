from app.database import Base
from sqlalchemy import Column, Integer,  String, UniqueConstraint, Enum as SQLAEnum
from sqlalchemy.orm import relationship
from app.models.enums import SpaceType

class Space(Base):
    __tablename__ = 'spaces'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(30), nullable=False)
    location = Column(String(30), nullable=False)
    capacity = Column(Integer, nullable=False)
    type = Column(SQLAEnum(SpaceType), nullable=False)
    seat = relationship("Seat", back_populates="space")


    __table_args__ = (
        UniqueConstraint('name', 'location', name='uq_name_location'),
    )