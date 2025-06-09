from pydantic import BaseModel

class SpaceCreate(BaseModel):
    name: str
    location: str
    capacity: int
    type: str
    