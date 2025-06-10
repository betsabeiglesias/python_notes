from app.database import Base
from sqlalchemy import Column, Integer, ForeignKey, DateTime, Enum as SQLAEnum
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_property
from app.models.enums import ReservationStatus


class Reservation(Base):
    __tablename__ = 'reservations'

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    seat_id = Column(Integer, ForeignKey("seats.id"))
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime, nullable=False)
    status = Column(SQLAEnum(ReservationStatus), default=ReservationStatus.active)

    @hybrid_property
    def calculated_duration(self):
        return (int((self.end_time - self.start_time).total_seconds() / 60))
    
    # @hybrid_property define una propiedad 
    # que puedes usar como atributo normal de instancia en tus objetos Python.
    # Permite calcular la duración de la reserva en código Python, usando atributos de la instancia.
    
    @calculated_duration.expression
    def calculated_duration(cls):
        return (
            extract('epoch', cls.end_time) - extract('epoch', cls.start_time)
        ) / 60

    #   @calculated_duration.expression define cómo se debe calcular esa propiedad 
    # cuando la usas en una consulta SQL (por ejemplo, en un filtro o un order_by).
    # Permite que SQLAlchemy traduzca la operación a SQL, usando funciones de la base de datos 
    # (como extract('epoch', ...) para obtener segundos desde el epoch).
    # Permite calcular la duración directamente en la base de datos cuando usas la propiedad 
    # en consultas SQL, optimizando el rendimiento y permitiendo filtros/ordenaciones eficientes.

    user = relationship("User", back_populates="reservation")
    seat = relationship("Seat", back_populates="reservation")