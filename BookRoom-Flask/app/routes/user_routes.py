from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.database import get_db
from app.models.user import User
from app.models.reservation import Reservation

user_routes = Blueprint("user_routes", __name__, url_prefix="/user")

# Desglose de Blueprint(...)
# Blueprint(nombre, import_name, **opciones)
# nombre: nombre interno del blueprint.
# import_name: generalmente se pone __name__, para que Flask pueda localizar recursos relativos como templates.
# url_prefix (opcional): prefijo que se agregará a todas las rutas del blueprint.

@user_routes.route("/new", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        name = request.form.get("name")
        nickname = request.form.get("nickname")
        credit = request.form.get("credit")
        rol = request.form.get("rol")
    
        with get_db() as db:
            existing_user = db.query(User).filter(
                (User.name == name) | (User.nickname == nickname)
            ).first()

            if existing_user:
                flash("Ya existe un usuario con ese nombre o nickname", "error")
                return render_template("create_user.html", name=name, nickname=nickname, credit=credit, rol=rol)

            new_user = User(name=name, nickname=nickname, credit=int(credit), rol=rol)
            db.add(new_user)
            db.commit()
        
        return redirect(url_for("user_routes.get_all_users"))

    return render_template("create_user.html")


@user_routes.route("/view", methods=["GET"])
def get_all_users():
    with get_db() as db:
        users = db.query(User).all()
    return render_template("user_list.html", users=users)


@user_routes.route("/view/<int:id_user>", methods=["GET"])
def get_only_user(id_user):
    with get_db() as db:
        user = db.query(User).filter(User.id == id_user).first()
    if not user:
        return "Usuario no encontrado", 404
    return render_template("user_detail.html", user=user)

@user_routes.route("/search", methods=["GET"])
def search_user_form():
    return render_template ("user_search.html")


@user_routes.route("/view/search", methods=["GET"])
def get_user_by_param():
    id_user = request.args.get("id_user", type=int)
    if not id_user:
        return "ID no proporcionado", 400
    with get_db() as db:
        user = db.query(User).filter(User.id == id_user).first()
    if not user:
        return "Usuario no encontrado", 404
    return render_template("user_detail.html", user=user)