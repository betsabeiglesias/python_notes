from flask import Flask, render_template
from .database import Base, engine
from .routes import register_routes
import os
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
 
    #crear tablas si no existen
    Base.metadata.create_all(bind=engine)

    #registrar blueprints
    register_routes(app)


    @app.route("/")
    def home():
        return render_template("base.html")

    return app





# from instance.config import Config

# load_dotenv()

# def create_app(config_class = Config):
#     app = Flask(__name__)
#     app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
#     app.config.from_object(config_class)

#     #crear tablas si no existen
#     Base.metadata.create_all(bind=engine)

#     #registrar blueprints
#     register_routes(app)


#     @app.route("/")
#     def home():
#         return render_template("base.html")

#     return app
