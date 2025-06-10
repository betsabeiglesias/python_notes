from fastapi import FastAPI
from app.routers import user_routes, space_routes, seat_routes, reservation_routes

app = FastAPI()


@app.get("/")
def read_root():
    return{"message": "API BookRoom on the way"}


def create_app() -> FastAPI:
    app = FastAPI(title="BookRoom API", version="1.0")

    app.include_router(user_routes.router)
    app.include_router(space_routes.router)
    app.include_router(seat_routes.router)
    app.include_router(reservation_routes.router)


    @app.get("/")
    def read_root():
       return{"message": "API BookRoom on the way"}
    
    return app

app = create_app()
