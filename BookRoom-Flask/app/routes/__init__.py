from .user_routes import user_routes
from .space_routes import space_routes
from .seat_routes import seat_routes
from .reservation_routes import reservation_routes

def register_routes(app):
    app.register_blueprint(user_routes)
    app.register_blueprint(space_routes)
    app.register_blueprint(seat_routes)
    app.register_blueprint(reservation_routes)