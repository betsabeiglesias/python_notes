from app.database import Base
from sqlalchemy import Column, Integer,  String, Date, Boolean, Enum, ForeignKey, DateTime, Float
from sqlalchemy.orm import relationship
from typing import TYPE_CHECKING


class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    seat_id = Column(Integer, ForeignKey("seats.id"))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    user = relationship("User", back_populates="reservation")
    seat = relationship("Seat", back_populates="reservation")