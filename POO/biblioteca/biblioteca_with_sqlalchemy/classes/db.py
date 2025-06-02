
import mysql.connector
import pandas as pd
from datetime import timedelta, datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from classes.modelos_alchemy import *
import uuid

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
        self.Session = sessionmaker(bind=self.engine)


    # ALCHEMY
    def conectar_db(self):
        try:
            with self.engine.connect() as connection:
                print("Conexión exitosa")
        except mysql.connector.Error as e:
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

    def pedir_material_usuario(self):
        tipo = input("¿Qué tipo de material quieres agregar? (libro, revista, dvd): ").lower()
        
        titulo = input("Título: ")
        autor = input("Autor: ")
        codigo_inventario = uuid.uuid4().hex[:6].upper()
        prestado = False

        if tipo == 'libro':
            num_paginas = int(input("Número de páginas: "))
            item = Libro(
                catalogo=CatalogoBiblioteca(
                    tipo='Libro', titulo=titulo, autor=autor,
                    codigo_inventario=codigo_inventario, prestado=prestado
                ),
                num_paginas=num_paginas
            )

        elif tipo == 'revista':
            num_edicion = int(input("Número de edición: "))
            fecha_str = input("Fecha de publicación (YYYY-MM-DD): ")
            from datetime import datetime
            fecha_publicacion = datetime.strptime(fecha_str, '%Y-%m-%d').date()
            item = Revista(
                catalogo=CatalogoBiblioteca(
                    tipo='Revista', titulo=titulo, autor=autor,
                    codigo_inventario=codigo_inventario, prestado=prestado
                ),
                num_edicion=num_edicion,
                fecha_publicacion=fecha_publicacion
            )

        elif tipo == 'dvd':
            duracion = float(input("Duración (horas): "))
            formato = input("Formato: ")
            item = DVD(
                catalogo=CatalogoBiblioteca(
                    tipo='Dvd', titulo=titulo, autor=autor,
                    codigo_inventario=codigo_inventario, prestado=prestado
                ),
                duracion=duracion,
                formato=formato
            )
        else:
            print("❌ Tipo desconocido.")
            return None

        return item


    def insertar_material_bbdd(self, item):
        try:
            # Paso 1: agregar el registro general del catálogo
            self.session.add(item.catalogo)
            self.session.commit()
            self.session.refresh(item.catalogo)  # asegura que id_material esté disponible

            # Paso 2: conectar el id_material al objeto específico
            item.id_material = item.catalogo.id_material
            self.session.add(item)
            self.session.commit()

            print(f"✅ Material '{item.catalogo.titulo}' agregado correctamente a la base de datos.")

        except Exception as e:
            self.session.rollback()
            print(f"❌ Error al insertar material: {e}")


    def insertar_usuario(self):
        try:
            name = input("Introduce el nombre de socio: \n")
            nuevo = Usuarios_Alchemy(nombre=name)
            self.session.add(nuevo)
            self.session.commit()
        except Exception as e:
            print(f"❌ Error al insertar usuario: {e}")

    def prestar_elemento_bbdd(self, id_item, id_user):
        try:
            material = self.session.query(CatalogoBiblioteca).filter_by(id_material=id_item).first()
            if not material:
                print(f"❌ No se encontró material con ID {id_item}")
                return

            usuario = self.session.query(Usuarios_Alchemy).filter_by(id=id_user).first()
            if not usuario:
                print(f"❌ No se encontró usuario con ID {id_user}")
                return
            
            if material.prestado:
                print(f"❌ El material '{material.titulo}' ya está prestado.")
                return

            material.prestado = True
            fecha_prestamo = datetime.now()
            fecha_limite = fecha_prestamo + timedelta(days=14)
            prestamo = Prestamo(
                usuario=usuario,
                material=material,
                fecha_prestamo=fecha_prestamo,
                fecha_limite=fecha_limite,
                fecha_devolucion=None
            )
            self.session.add(prestamo)
            self.session.commit()

            print(f"✅ El material '{material.titulo}' ha sido prestado al usuario '{usuario.nombre}' hasta el {fecha_limite.date()}.")

        except Exception as e:
            print(f"❌ Error al prestar elemento: {e}")


    def devolver_elemento_bbdd(self, id_item, id_user):
        try:
            prestamo = self.session.query(Prestamo).filter_by(id_material=id_item).first()
            if not prestamo:
                print(f"❌ El material con ID '{id_item}' no tiene préstamo activo.")
                return

            if prestamo.id_usuario != id_user:
                print(f"El usuario {id_user} no había alquilado el elemento {id_item}")
                return
                     
            prestamo.material.prestado = False
            prestamo.fecha_devolucion = datetime.now()
           
            self.session.add(prestamo)
            self.session.commit()

            print(f"✅ El material '{prestamo.material.titulo}' ha sido devuelto po el usuario '{id_user}'.")

        except Exception as e:
            print(f"❌ Error al prestar elemento: {e}")
        

    def mostrar_catalogo(self):
        materiales = self.session.query(CatalogoBiblioteca).all()
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

    def mostrar_catalogo(self):
        materiales = self.session.query(CatalogoBiblioteca).all()
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


    def mostrar_usuarios(self):
        users = self.session.query(Usuarios_Alchemy).all()
        data =[{
            "id_usuario": u.id,
            "nombre": u.nombre,
        }
        for u in users]
        df = pd.DataFrame(data)
        print(df)

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

     