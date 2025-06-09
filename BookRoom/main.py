from fastapi import FastAPI
from app.routers import user_routes

app = FastAPI()

app.include_router(user_routes.router)

@app.get("/")
def read_root():
    return{"message": "API BookRoom on the way"}



