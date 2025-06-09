from pydantic import BaseModel, Field


class SpaceCreate(BaseModel):
    name: str = Field(..., example="North Wing")
    location: str = Field(..., example="First Floor")
    capacity: int = Field(..., example=20, ge=1)
    type: str = Field(..., example="study")


class SpaceOut(BaseModel):
    id: int
    name: str
    location: str
    capacity: int
    type: str

    model_config = {
        "from_attributes": True  # Pydantic v2
    }