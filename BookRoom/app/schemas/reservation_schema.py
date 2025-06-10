from pydantic import BaseModel,Field
from datetime import datetime
from typing import Optional
from app.models.enums import ReservationStatus

class ReservationCreate(BaseModel):
    user_id: int = Field(..., example=42)
    seat_id: int = Field(..., example=1)
    start_time: datetime
    end_time: datetime
   
class ReservationOut(BaseModel):
    id: int
    user_id: int
    seat_id: int
    start_time: datetime
    end_time: datetime
    duration: int = Field(..., alias="calculated_duration")
    status: ReservationStatus

    model_config = {
        "from_attributes": True
    }


# ReservationUpdate, hay que permitir que los campos sean opcionales, 
# ya que en una actualización parcial no todos los campos tienen que estar presentes.
# Usamos Optional para permitir omitirlos 
# y Field(None) si queremos dar información adicional como ejemplos.

class ReservationUpdate(BaseModel):
    user_id: Optional[int] = Field(None, example=42)
    seat_id: Optional[int] = Field(None, example=1)
    start_time: Optional[datetime] = None
    end_time: Optional[datetime] = None
    duration: Optional[int] = None
    status: Optional[ReservationStatus] = None