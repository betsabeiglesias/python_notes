from pydantic import BaseModel, Field
from app.models.enums import SpaceType

class SpaceCreate(BaseModel):
    name: str = Field(..., example="North Wing")
    location: str = Field(..., example="First Floor")
    capacity: int = Field(..., example=20, ge=1)
    type: SpaceType= Field(...,example=SpaceType.study)


class SpaceOut(BaseModel):
    id: int
    name: str
    location: str
    capacity: int
    type: str

    model_config = {
        "from_attributes": True  # Pydantic v2
    }