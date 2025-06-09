from app.database import SessionLocal
from app.models import User

db = SessionLocal()
users = db.query(User).all()
print(f"Usuarios encontrados: {users}")