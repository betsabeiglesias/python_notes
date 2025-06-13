# app/routes/space_routes.py
from flask import Blueprint, render_template, request, redirect, url_for
from app.database import get_db
from app.models.space import Space
from app.models.seat import Seat

space_routes = Blueprint("space_routes", __name__, url_prefix="/space")

@space_routes.route("/view", methods=["GET"])
def get_all_spaces():
    with get_db() as db:
        spaces = db.query(Space).all()
    return render_template("space_list.html", spaces=spaces)

@space_routes.route("/new",methods=["GET", "POST"])
def create_space():
    if request.method == "POST":
        name_space = request.form.get("name_space")
        location = request.form.get("location")
        capacity = int(request.form.get("capacity"))
        type = request.form.get("type")
    
        with get_db() as db:
            existing = db.query(Space).filter_by(name=name_space).first()
            if existing:
                return f"Ya existe un espacio con el nombre '{name_space}'.", 400

            new_space = Space(
            name=name_space,
            location=location,
            capacity=int(capacity), 
            type=type)
            db.add(new_space)
            db.commit()
            db.refresh(new_space)

        for i in range(1, capacity + 1):
            seat = Seat(
                number=i,
                available=True,
                space_id=new_space.id
            )
            db.add(seat)

        db.commit()

        return redirect(url_for("space_routes.get_all_spaces"))
    
    return render_template("space_create.html")
