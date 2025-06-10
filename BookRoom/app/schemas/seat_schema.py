from pydantic import BaseModel, Field
from typing import Optional

class SeatCreate(BaseModel):
    number: int = Field(..., example=1)
    available: bool = Field(..., example=True)
    space_id: int = Field(..., example=42)

class SeatOut(BaseModel):
    id: int
    number: int
    available: bool
    space_id: int

    class Config:
        orm_mode = True

class SeatUpdate(BaseModel):
    available: Optional[bool] = Field(None, example=True)