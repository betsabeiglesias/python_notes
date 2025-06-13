from flask import Blueprint, render_template, request, redirect, url_for
from app.database import get_db
from app.models.reservation import Reservation
from app.models.user import User
from app.models.seat import Seat
from app.models.enums import ReservationStatus
from datetime import datetime
from sqlalchemy.orm import joinedload

reservation_routes = Blueprint("reservation_routes", __name__, url_prefix="/reservation")

@reservation_routes.route("/new", methods=["GET", "POST"])
def reservation_create():
    with get_db() as db:
        users = db.query(User).all()

        if request.method == "POST":
            user_id = int(request.form.get("user_id"))
            seat_id = int(request.form.get("seat_id"))
            start_time = datetime.fromisoformat(request.form.get("start_time"))
            end_time = datetime.fromisoformat(request.form.get("end_time"))

            duration = int((end_time - start_time).total_seconds() / 60)

            # Verificar crédito
            user = db.query(User).filter_by(id=user_id).first()
            if user.credit < duration:
                return f"El usuario no tiene créditos suficientes. Necesita {duration} y tiene {user.credit}.", 400

            # Validación: asiento y usuario sin conflictos
            overlapping_user = db.query(Reservation).filter(
                Reservation.user_id == user_id,
                Reservation.end_time > start_time,
                Reservation.start_time < end_time
            ).first()

            if overlapping_user:
                return "El usuario ya tiene otra reserva en ese horario", 400

            overlapping_seat = db.query(Reservation).filter(
                Reservation.seat_id == seat_id,
                Reservation.end_time > start_time,
                Reservation.start_time < end_time
            ).first()

            if overlapping_seat:
                return "El asiento ya está reservado en ese horario", 400

            new_res = Reservation(
                user_id=user_id,
                seat_id=seat_id,
                start_time=start_time,
                end_time=end_time
            )
            db.add(new_res)
            db.commit()
            return redirect(url_for("reservation_routes.reservation_list"))

        # Si es GET con parámetros de fecha: calcular asientos disponibles
        start = request.args.get("start_time")
        end = request.args.get("end_time")
        selected_user_id = request.args.get("user_id", type=int)

        available_seats = []

        if start and end:
            start_dt = datetime.fromisoformat(start)
            end_dt = datetime.fromisoformat(end)

            # Subconsulta: IDs de asientos ocupados en ese rango
            subquery = db.query(Reservation.seat_id).filter(
                Reservation.end_time > start_dt,
                Reservation.start_time < end_dt
            )

            # Filtrar asientos que NO estén en esa subconsulta
            available_seats = db.query(Seat).options(joinedload(Seat.space)).filter(~Seat.id.in_(subquery)).all()

    return render_template(
            "reservation_create.html",
            users=users,
            seats=available_seats,
            selected_user_id=selected_user_id,
            start_time=start,
            end_time=end
        )


@reservation_routes.route("/view")
def reservation_list():
    with get_db() as db:
        now = datetime.now()

        expired = db.query(Reservation).filter(
            Reservation.status == ReservationStatus.active,
            Reservation.end_time < now
        )

        for r in expired:
            r.status = ReservationStatus.completed

        db.commit()
        
        reservations = db.query(Reservation).options(
            joinedload(Reservation.user),
            joinedload(Reservation.seat).joinedload(Seat.space)
        ).all()
    return render_template("reservation_list.html", reservations=reservations)
