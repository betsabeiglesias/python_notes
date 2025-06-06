
import mysql.connector
import pandas as pd
from datetime import timedelta, datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes.modelos_alchemy import *
import uuid
from fastapi import HTTPException
from pymongo import MongoClient

#mysql://root:IupkeoIwuJVczCxRpsSxBIPgaGqnLpES@nozomi.proxy.rlwy.net:50794/railway

class Gestor_BBDD:
    def __init__(self):
        self.user = "root"
        self.password = "IupkeoIwuJVczCxRpsSxBIPgaGqnLpES"
        self.host = "nozomi.proxy.rlwy.net"
        self.database = "railway"
        self.port = 50794
        self.conexion = None
        self.cursor = None
        self.URL = "mysql+pymysql://root:IupkeoIwuJVczCxRpsSxBIPgaGqnLpES@nozomi.proxy.rlwy.net:50794/railway"
        self.engine = create_engine(self.URL) # ALCHEMY
        

        self.mongo_string = "mongodb://mongo:NbMhazHHMzNqZZvJnKfAgapiJpAqKFsJ@crossover.proxy.rlwy.net:51738"
        
        self.cliente_mongo = MongoClient(self.mongo_string,  serverSelectionTimeoutMS=5000)


    # MONGO
    def conectar_mongo(self):
        try:
            self.cliente_mongo.admin.command("ping")
            print("✅ Conexión exitosa a MongoDB")
        except Exception as e:
            print("Error al conectar a MongoDB:", e)

    # crear tabla en mongo
    def crear_tabla_mongo(self):
        self.mongodb = self.cliente_mongo["reseñas_mongo"]

    def insertar_reseñas_mongo(self, id_item, review, autor):
        try:
            reseña = {
                "id_item": id_item,
                "opinion": review,
                "autor": autor,
                "fecha": datetime.now()
            }
            result = self.mongodb["reseñas"].insert_one(reseña)
            print(f"🟢 Reseña insertada con ID: {result.inserted_id}")
            return str(result.inserted_id)  
        except Exception as e:
            print("❌ Error al insertar la reseña:", e)
            raise e


    def buscar_reseñas_mongo(self, id_material):
        try:
            cursor = self.mongodb["reseñas"].find({"id_item": id_material},
                                {"autor": 1, "opinion": 1, "fecha": 1, "_id": 0} )
            reseñas = list(cursor)
            return reseñas                
        except Exception as e:
            print("❌ Error al recuperar reseñas:", e)
            raise e

    # ALCHEMY
    def conectar_db(self):
        try:
            with self.engine.connect() as connection:
                print("Conexión exitosa")
        except Exception as e:
            print(f"❌ Error de MySQL: {e}")

    def abrir_sesion(self):

        self.session = self.Session()
        print("✅ Sesión Abierta")

    # Con SQLAlchemy, no necesitas mantener abierta una conexión “global”.
    #El patrón recomendado es:
    #Abrir la conexión cuando la necesites.
    #Usarla (en un with o en una sesión).
    #Que se cierre automáticamente al terminar.
    #No es como mysql.connector donde a veces mantenías una conexión abierta durante todo el ciclo del objeto.
    
    def crear_tablas(self):
        try:
            Base.metadata.create_all(self.engine)
            print("✅ Tablas creadas correctamente (si no existían).")
        except Exception as e:
            print(f"❌ Error al crear las tablas: {e}")


##### MATERIAL #####

    def crear_material_catalogo(self, tipo, titulo, autor, extra_data): 
    # Aquí, extra_data es un diccionario (o mejor aún, un objeto Pydantic) que contiene los datos adicionales según el tipo.
        codigo_inventario = uuid.uuid4().hex[:6].upper()
        prestado = False
        if tipo == 'libro':
            item = Libro(
                catalogo=CatalogoBiblioteca(
                   tipo='Libro', 
                   titulo=titulo, 
                   autor=autor, 
                   codigo_inventario=codigo_inventario, 
                   prestado=prestado
                ),
                num_paginas=extra_data["paginas"]
            )
        elif tipo == 'revista':
            item = Revista(
                catalogo=CatalogoBiblioteca(
                    tipo='Revista', 
                    titulo=titulo, 
                    autor=autor,
                    codigo_inventario=codigo_inventario, 
                    prestado=prestado
                ),
                num_edicion=extra_data["edicion"],
                fecha_publicacion=extra_data["fecha"]
            )
        elif tipo == 'dvd':   
            item = DVD(
                catalogo=CatalogoBiblioteca(
                    tipo='Dvd', 
                    titulo=titulo, 
                    autor=autor,
                    codigo_inventario=codigo_inventario, 
                    prestado=prestado
                ),
                duracion=extra_data["duracion"],
                formato=extra_data["formato"]
            )
        else:
            raise ValueError("Tipo de material no válido")

        return item


    def insertar_material_bbdd(self, session, item):
        try:
            # Paso 1: agregar el registro general del catálogo
            session.add(item.catalogo)
            session.commit()
            session.refresh(item.catalogo)  # asegura que id_material esté disponible

            # Paso 2: conectar el id_material al objeto específico
            item.id_material = item.catalogo.id_material
            session.add(item)
            session.commit()

            print(f"✅ Material '{item.catalogo.titulo}' agregado correctamente a la base de datos.")


        except Exception as e:
            session.rollback()
            raise HTTPException(status_code=500, detail=(f"❌ Error al insertar material: {e}"))



    def mostrar_catalogo_df(self, session):
        materiales = session.query(CatalogoBiblioteca).all()
        data = [
        {
            "id_material": m.id_material,
            "tipo": m.tipo,
            "titulo": m.titulo,
            "autor": m.autor,
            "codigo_inventario": m.codigo_inventario,
            "prestado": m.prestado
        }
        for m in materiales
        ]
        df = pd.DataFrame(data)
        print(df)


    def mostrar_catalogo(self, session):
        materiales = session.query(CatalogoBiblioteca).all()
        data = [
        {
            "id_material": m.id_material,
            "tipo": m.tipo,
            "titulo": m.titulo,
            "autor": m.autor,
            "codigo_inventario": m.codigo_inventario,
            "prestado": m.prestado
        }
        for m in materiales
        ]
        return {"materiales": data}
    
    def mostrar_material_unico(self, session, id_item):
        item = session.query(CatalogoBiblioteca).filter(CatalogoBiblioteca.id_material == id_item).first()
        if not item:
            return None
        return {
            "id_material": item.id_material,
            "tipo": item.tipo,
            "titulo": item.titulo,
            "autor": item.autor,
            "código_inventario": item.codigo_inventario,
            "prestado": item.prestado
        }

    def modificar_material(self, session, id_item, extra_data:dict):
        item = session.query(CatalogoBiblioteca).filter(CatalogoBiblioteca.id_material == id_item).first()

        if not item:
            raise HTTPException(status_code=404, detail="Material no encontrado")
        
        for clave, valor in extra_data.items():
            if hasattr(item, clave):
                setattr(item, clave, valor)
            if item.tipo == "libro" and hasattr(item.libro, clave):
                setattr(item.libro, clave, valor)
            elif item.tipo == "revista" and hasattr(item.revista, clave):
                setattr(item.revista, clave, valor)
            elif item.tipo == "dvd" and hasattr(item.dvd, clave):
                setattr(item.dvd, clave, valor)
            else:
                print (f"Campo no reconocido: {clave}")
        session.commit()


##### PRÉSTAMOS #####

    def mostrar_prestamos(self, session):
        try:
            prestamos = session.query(Prestamo_Alchemy).all()
            data = [
            {
                "id_prestamo": p.id_prestamo,
                "id_usuario": p.id_usuario,
                "id_material": p.id_material,
                "fecha_prestamo": p.fecha_prestamo,
                "fecha_limite": p.fecha_limite,
                "fecha_devolucion": p.fecha_devolucion
            }
            for p in prestamos
            ]
            return {"prestamos": data}
        except Exception as e:
            print(f"Error al recuperar prestamos {e}")
            raise

    def mostrar_unico_prestamo(self, session, id_prestamo):
        try:
            prestamo = session.query(Prestamo_Alchemy).filter_by(id_prestamo=id_prestamo).first()
            if not prestamo:
                raise HTTPException(status_code=404, detail=f"❌ No se encontró el préstamo con ID {id_prestamo}")

            data ={
                "id_prestamo": prestamo.id_prestamo,
                "id_usuario": prestamo.id_usuario,
                "id_material": prestamo.id_material,
                "fecha_prestamo": prestamo.fecha_prestamo,
                "fecha_limite": prestamo.fecha_limite,
                "fecha_devolucion": prestamo.fecha_devolucion
            }
            return {"prestamo": data}
        
        except Exception as e:
            print(f"Error al recuperar prestamos {e}")
            raise HTTPException(status_code=500, detail=f"❌ Error interno: {str(e)}")



    def prestar_elemento_bbdd(self, session, id_item, id_user):
        try:
            material = session.query(CatalogoBiblioteca).filter_by(id_material=id_item).first()
            if not material:
                print(f"❌ No se encontró material con ID {id_item}")
                return

            usuario = session.query(Usuarios_Alchemy).filter_by(id=id_user).first()
            if not usuario:
                print(f"❌ No se encontró usuario con ID {id_user}")
                return
            
            if material.prestado:
                raise HTTPException(
                status_code=409,
                detail=f"El material '{material.titulo}' ya está prestado"
                )

            material.prestado = True
            fecha_prestamo = datetime.now()
            fecha_limite = fecha_prestamo + timedelta(days=14)
            prestamo = Prestamo_Alchemy(
                usuario=usuario,
                material=material,
                fecha_prestamo=fecha_prestamo,
                fecha_limite=fecha_limite,
                fecha_devolucion=None
            )
            session.add(prestamo)
            session.commit()

            print(f"✅ El material '{material.titulo}' ha sido prestado al usuario '{usuario.nombre}' hasta el {fecha_limite.date()}.")

        except HTTPException:
        # Re-lanza las HTTPException sin modificarlas
            raise

        except Exception as e:
            print(f"❌ Error al prestar elemento: {e}")



    def actualizar_prestamo(self, session, id_prestamo, fecha_limite=None, devolver=False ):
        ptmo = session.query(Prestamo_Alchemy).filter_by(id_prestamo=id_prestamo).first()
            
        if not ptmo:
            raise HTTPException(status_code=404, detail="❌ Préstamo no encontrado")

        if ptmo.fecha_devolucion:
            raise HTTPException(status_code=400, detail="⚠️ Este préstamo ya fue devuelto")
            
        if devolver:
            ptmo.fecha_devolucion = datetime.now()
            ptmo.material.prestado = False
        
        elif fecha_limite:
            ptmo.fecha_limite = ptmo.fecha_limite + timedelta(days=14)
        
        else:
            raise HTTPException(status_code=400, detail="⚠️ No se proporcionó información de devolución")

        session.commit()
        


##### USUARIOS #####

    def mostrar_usuarios(self, session):
        users = session.query(Usuarios_Alchemy).all()
        data =[{
            "id_usuario": u.id,
            "nombre": u.nombre,
        }
        for u in users]
        return {"usuarios": data}
    
    def crear_usuario(self, nombre):
        nuevo = Usuarios_Alchemy(nombre)
        return{ "nombre": nuevo.nombre}
    
    def insertar_usuario(self, session, new_user):
        try:
            # nuevo = Usuarios_Alchemy(user)
            session.add(new_user)
            session.commit()
        except Exception as e:
            print(f"❌ Error al insertar usuario: {e}")



    def mostrar_unico_usuarios(self, id_user):
        user = self.session.query(Usuarios_Alchemy).filter(Usuarios_Alchemy.id == id_user).first()
        if not user:
            print(f"❌ No se encontró usuario con ID {id_user}")
            return
        
        # if len(user.prestamos) == 0:
        #     print(f"❌ El usuario {user.nombre} no tienen ningún prestamo")
        #     return

        
        data = [{
            "id_usuario": user.id,
            "nombre": user.nombre,
            "prestamos en vigor": [p.material.titulo for p in user.prestamos if p.material.prestado == True],
            "prestamos pasados": [p.material.titulo for p in user.prestamos]
        }]

        df = pd.DataFrame(data)
        print(df)

    