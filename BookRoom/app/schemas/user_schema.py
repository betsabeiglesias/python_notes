from pydantic import BaseModel
from app.models.enum import RoleEnum

class UserCreate(BaseModel):
    name:str
    nickname:str
    credit: int = 0
    rol: RoleEnum=RoleEnum.user

class UserOut(BaseModel):
    id: int
    name: str
    nickname: str
    credit: int
    rol: RoleEnum

    class Config:
        orm_mode = True