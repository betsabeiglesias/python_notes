from flask import Flask, render_template, request, session, redirect, url_for, make_response
import os
from dotenv import load_dotenv
from flask_wtf import CSRFProtect, FlaskForm

load_dotenv()

app = Flask(__name__) # Estás creando una instancia de la aplicación Flask.👉 Crea la aplicación Flask
# 👉 Le indica a Flask cómo encontrar rutas y recursos en tu proyecto
app.secret_key = os.getenv("SECRET_KEY")
csrf = CSRFProtect(app)

@app.route("/")
def inicio():
    nombre = session.get("nombre")
    color = request.cookies.get("color", "white") #color por defecto
    return render_template("inicio.html", nombre=nombre, color=color)

# @app.route("/inicio")
# def inicio():
#     nombre = session.get("nombre")
#     color = request.cookies.get("color", "white")
#     return render_template("inicio.html", nombre=nombre, color=color)


@app.route("/configurar", methods = ["GET", "POST"])
def pagina_configuracion():
    if request.method == "POST":
        #1. Obtener datos del formulario
        nombre = request.form.get("nombre")
        color = request.form.get("color")

        #2.Guardar nombre en la sesión
        session["nombre"] = nombre

        #3.Guardar el color en la cookie
        response = make_response(redirect(url_for("inicio")))
#redirect(url_for("base")) crea una respuesta de redirección 
#(status 302) hacia la ruta / (porque "base" es tu función para la página de inicio).
# make_response(...) convierte esa redirección en un objeto de respuesta editable,
# para que puedas añadir cookies, cabeceras, etc.
        
        response.set_cookie("color", color)
# Esto añade una cookie llamada "color" con el valor que introdujo el usuario (por ejemplo, "pink" o "#ffcc00").
# El navegador guardará esa cookie y la enviará de vuelta automáticamente en cada nueva petición al servidor.
        
        return response
# Finalmente, devuelves la respuesta modificada con:
# la redirección al inicio (/)
# la cookie establecida

     # Si es GET, simplemente renderizamos el formulario
    return render_template("configurar.html")


@app.route("/olvidar")
def olvidar_preferencias():
    #1.Eliminar el "nombre" de la sesión
    session.pop("nombre", None)

    #2.Crear una respuesta para eliminar la cookie "color"
    response = make_response(redirect(url_for("inicio")))
    response.set_cookie("color", "", expires=0)

    return response



#  Teoría rápida
# request.method == "POST" → indica que se está enviando el formulario.
# request.form.get("nombre") → obtiene el valor del input nombre.
# session['nombre'] = valor → guarda el valor en la sesión.
# response.set_cookie("color", valor) → guarda el valor en una cookie.



if __name__ == "__main__":
    app.run(debug=True)



