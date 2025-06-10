from app.database import Base
from sqlalchemy import Column, Integer,  String, Date, Boolean, Enum, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship

class Seat(Base):
    __tablename__ = 'seats'

    id = Column(Integer, primary_key=True, nullable=False)
    number = Column(Integer)
    available = Column(Boolean, default=True)
    space_id = Column(Integer, ForeignKey("spaces.id"), nullable=False)
    space = relationship("Space", back_populates="seat")
    reservation = relationship("Reservation", back_populates="seat")



# relationship("NombreDelOtroModelo", back_populates="atributo_en_el_otro_modelo")
