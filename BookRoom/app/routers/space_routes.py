from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import SpaceCreate, SpaceOut
from app.models import Space
from app.dependencies import get_db
from typing import List

router = APIRouter(
    prefix="/space",
    tags=["Space"]
)

@router.post("/", response_model=SpaceOut)
def create_space(space: SpaceCreate, db: Session = Depends(get_db)):
    existing_space = db.query(Space).filter(Space.name == space.name, Space.location == space.location).first()
    if existing_space:
        raise HTTPException(status_code=400, detail="Nickname already registered")
    
    new_space = Space(**space.model_dump())

    db.add(new_space)
    db.commit()
    db.refresh(new_space)
    return new_space # FastAPI lo convierte a SpaceOut automáticamente

@router.get("/", response_model=List[SpaceOut])
def get_all_space(db:Session=Depends(get_db)):
    try:
        spaces = db.query(Space).all()
        return spaces
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{space_id}", response_model=SpaceOut)
def get_space(space_id: int, db: Session=Depends(get_db)):
    try:
        space = db.query(Space).filter(Space.id == space_id).first()
        if not space:
            raise HTTPException(status_code=404, detail=f"Space with id:{space_id} does not exist")
        return space
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    