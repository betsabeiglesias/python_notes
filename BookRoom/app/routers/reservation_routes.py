from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
from app.schemas import ReservationCreate, ReservationOut, ReservationUpdate
from app.models import Reservation, User
from app.dependencies import get_db
from datetime import datetime

router = APIRouter(
    prefix="/reservation",
    tags=["Reservation"]
)

@router.post("/", response_model=ReservationOut)
def create_reservation(res: ReservationCreate, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == res.user_id).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    
    if res.start_time < datetime.now():
        raise HTTPException(
            status_code=409,
            detail="The reservation cannot start in the past."
        )

    if res.end_time <= res.start_time:
        raise HTTPException(
            status_code=409,
            detail="The end time must be later than the start time of the reservation."
        )

    new_reservation = Reservation(**res.model_dump())
    if new_reservation.calculated_duration < 30:
        raise HTTPException(status_code=400, 
        detail="Duration must be more than 30 minutes")
    if user.credit < new_reservation.calculated_duration:
        raise HTTPException(status_code=400, detail="Insufficient credit")
    
    user.credit -= new_reservation.calculated_duration
    
    overlapping_reservation = db.query(Reservation).filter(
        Reservation.user_id == res.user_id,
        Reservation.start_time < res.end_time,
        Reservation.end_time > res.start_time
    ).first()
    if overlapping_reservation:
        raise HTTPException(
            status_code=409,             
            detail=f"El usuario {res.user_id} ya tiene reservas entre {overlapping_reservation.start_time} y {overlapping_reservation.end_time}"
        )


    db.add(new_reservation)    
    try:
        db.commit()
        db.refresh(new_reservation)
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(
            status_code=400,
            detail=f"Error de integridad: {str(e.orig)}"
        )
    
    return new_reservation


@router.put("/{reservation_id}", response_model=ReservationOut)
def update_reservation(reservation_id: int, res_update: ReservationUpdate, db: Session=Depends(get_db)):
    try:
        res = db.query(Reservation).filter(Reservation.id == reservation_id).first()
        if not res:
            raise HTTPException(
                status_code=400,
                detail=f"Reservation id  {reservation_id} not found"
            )
        update_data = res_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(res, key, value)
        db.commit()
        db.refresh(res)
        return res
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
