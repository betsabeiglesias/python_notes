from classes.db import Gestor_BBDD

def test_mongo_connection():
    gestor = Gestor_BBDD()
    gestor.conectar_mongo()

if __name__ == "__main__":
    test_mongo_connection()