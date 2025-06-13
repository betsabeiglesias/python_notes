from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("base.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name, email, message = get_contact_form_data()
        print("Formulario recibido:")
        print(f"Nombre: {name}")
        print(f"Email: {email}")
        print(f"Mensaje: {message}")

        return render_template("contact_enviado.html")
        # return render_template("contact.html", success=True)
    return render_template("contact.html", success=False) 



def get_contact_form_data():
    name = request.form.get("name")
    email = request.form.get("email")
    message = request.form.get("message")
    return name, email, message

def extract_contact_data():
    return {
        "name": request.form.get("name"),
        "email": request.form.get("email"),
        "message": request.form.get("message")
    }



if __name__ == "__main__":
    app.run(debug=True)


