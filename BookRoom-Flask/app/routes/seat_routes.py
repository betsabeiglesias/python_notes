# app/routes/seat_routes.py

from flask import Blueprint, render_template, request, redirect, url_for
from app.database import get_db
from app.models.seat import Seat
from app.models.space import Space
from sqlalchemy.orm import joinedload

seat_routes = Blueprint("seat_routes", __name__, url_prefix="/seat")

@seat_routes.route("/view", methods=["GET"])
def get_all_seats():
    with get_db() as db:
        seats = db.query(Seat).options(joinedload(Seat.space)).all()
    return render_template("seat_list.html", seats=seats)

@seat_routes.route("/new", methods=["GET", "POST"])
def create_seat():
    with get_db() as db:
        spaces = db.query(Space).all()

    if request.method == "POST":
        number = request.form.get("number")
        space_id = request.form.get("space_id")

        with get_db() as db:
            new_seat = Seat(
                number=int(number),
                space_id=int(space_id),
                available=True
            )
            db.add(new_seat)
            db.commit()

        return redirect(url_for("seat_routes.get_all_seats"))

    return render_template("seat_create.html", spaces=spaces)
