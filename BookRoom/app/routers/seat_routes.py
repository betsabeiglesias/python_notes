from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas import SeatCreate, SeatUpdate, SeatOut
from app.dependencies import get_db
from app.models import Seat, Space
from typing import List


router = APIRouter(
    prefix="/seat",
    tags=["Seat"]
)

@router.post("/", response_model=SeatOut)
def create_seat(seat: SeatCreate, db: Session = Depends(get_db)):
    space = db.query(Space).filter(Space.id == seat.space_id).first()
    if not space:
        raise HTTPException(
            status_code=404,
            detail=f"Space ID {seat.space_id} does not exist"
        )

    existing_seat = db.query(Seat).filter(Seat.number == seat.number, Seat.space_id == seat.space_id).first()
    if existing_seat:
        raise HTTPException(status_code=400, detail= f"Seat number {seat.number} already exists in space {seat.space_id}")
    
    new_seat = Seat(**seat.model_dump())
    db.add(new_seat)
    db.commit()
    db.refresh(new_seat)

    return new_seat



@router.get("/", response_model=List[SeatOut])
def get_all_seat(db: Session = Depends(get_db)):
    try:
        seats = db.query(Seat).all()
        return seats
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{seat_id}", response_model=SeatOut)
def get_seat(seat_id: int, db: Session = Depends(get_db)):
    try:
        seat = db.query(Seat).filter(Seat.id == seat_id).first()
        if not seat:
             raise HTTPException(status_code=404, detail=f"Space with id:{seat_id} does not exist")
        return seat
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    





