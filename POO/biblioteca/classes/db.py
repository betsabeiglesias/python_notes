
import mysql.connector
import pandas as pd
from datetime import timedelta, datetime

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

    def conectar_db(self):
        try:
            self.conexion  = mysql.connector.connect(user=self.user,
                password=self.password,
                host=self.host,
                port=self.port,
                database=self.database
            )
            self.cursor = self.conexion.cursor()
            print("✅ Conexión correcta de SQL")

        except mysql.connector.Error as e:
            print(f"❌ Error de MySQL: {e%s}")


    def desconectar_db(self):
        if self.cursor:
            self.cursor.close()
        if self.conexion:
            self.conexion.close()
            print("🔗 Conexión cerrada")

    def crear_tablas(self):
        try:
            # Tabla de usuarios
            query_usuarios = """
            CREATE TABLE IF NOT EXISTS usuarios_biblioteca (
                id_usuario INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) NOT NULL
            )
            """

            # Tabla general del catálogo
            query_catalogo = """
            CREATE TABLE IF NOT EXISTS catalogo_biblioteca (
                id_material INT AUTO_INCREMENT PRIMARY KEY,
                tipo ENUM('Libro', 'Revista', 'Dvd') NOT NULL,
                titulo VARCHAR(255) NOT NULL,
                autor VARCHAR(255),
                codigo_inventario VARCHAR(100) UNIQUE NOT NULL,
                prestado BOOLEAN DEFAULT FALSE
            )
            """

            query_catalogo = """
            CREATE TABLE IF NOT EXISTS catalogo_biblioteca (
                id_material INT AUTO_INCREMENT PRIMARY KEY,
                tipo ENUM('Libro', 'Revista', 'Dvd') NOT NULL,
                titulo VARCHAR(255) NOT NULL,
                autor VARCHAR(255),
                codigo_inventario VARCHAR(100) UNIQUE NOT NULL,
                prestado BOOLEAN DEFAULT FALSE
            );"""


            query_libro = """
            CREATE TABLE IF NOT EXISTS libros (
                id_material INT PRIMARY KEY,
                num_paginas INT NOT NULL,
                FOREIGN KEY (id_material) REFERENCES catalogo_biblioteca(id_material) ON DELETE CASCADE
            );"""

            query_revista = """
            CREATE TABLE IF NOT EXISTS revistas (
                id_material INT PRIMARY KEY,
                num_edicion INT NOT NULL,
                fecha_publicacion DATE NOT NULL,
                FOREIGN KEY (id_material) REFERENCES catalogo_biblioteca(id_material) ON DELETE CASCADE
            );"""

            query_dvd = """
            CREATE TABLE IF NOT EXISTS dvds (
                id_material INT PRIMARY KEY,
                duracion FLOAT NOT NULL,
                formato VARCHAR(50) NOT NULL,
                FOREIGN KEY (id_material) REFERENCES catalogo_biblioteca(id_material) ON DELETE CASCADE
            );"""
            # Ejecutar las queries
            self.cursor.execute(query_usuarios)
            self.cursor.execute(query_catalogo)
            self.cursor.execute(query_libro)
            self.cursor.execute(query_revista)
            self.cursor.execute(query_dvd)
            self.conexion.commit()

            print("✅ Tablas 'usuarios_biblioteca' y 'catalogo_biblioteca' creadas correctamente (si no existían).")

        except mysql.connector.Error as e:
            print(f"❌ Error al crear las tablas: {e}")


    def insertar_material_bbdd(self, item):
        try:

            query_insert_general =  """INSERT INTO catalogo_biblioteca (codigo_inventario, tipo, titulo, autor, prestado)
                VALUES (%s, %s, %s, %s, %s)"""
            tipo = item.__class__.__name__.lower()
            self.cursor.execute(query_insert_general, (item.codigo_inventario, tipo, item.titulo, item.autor, item.prestado))
            self.conexion.commit()
            id_material = self.cursor.lastrowid

            if tipo == "libro":
                query_insert_libro = """INSERT INTO libros (id_material, num_paginas)
                    VALUES (%s, %s)"""
                self.cursor.execute(query_insert_libro, (id_material, item.num_paginas))
            
            elif tipo == "revista":
                query_insert_revista = """ INSERT INTO revistas (id_material, num_edicion, fecha_publicacion)
                    VALUES (%s, %s, %s)"""
                fecha_str = item.fecha_publicacion.strftime('%Y-%m-%d')
                self.cursor.execute(query_insert_revista, (id_material, item.num_edicion, fecha_str))

            elif tipo == "dvd":
                query_insert_dvd = """INSERT INTO dvds (id_material, duracion, formato)
                    VALUES (%s, %s, %s)"""
                self.cursor.execute(query_insert_dvd, (id_material, item.duracion, item.formato))

            self.conexion.commit()
            print(f"✅ Material '{item.titulo}' agregado correctamente a la base de datos.")
        
        except mysql.connector.Error as e:
            print(f"❌ Error al insertar material: {e}")



    def ejecucion_query(self, query, params=None):
        try:
            if params:
                self.cursor.execute(query, params)
            else:
                self.cursor.execute(query)
            self.conexion.commit()
            print("✅ Ejecución correcta de query")
        except mysql.connector.Error as e:
            print(f"❌ Error de MySQL: {e}")

    def select_query(self, query):
        try:
            self.cursor.execute(query)
            results = self.cursor.fetchall()
            df = pd.DataFrame(results, columns=[col[0] for col in self.cursor.description])
            # print (df)
            return print (df)
        except mysql.connector.Error as e:
            print(f"❌ Error de MySQL: {e}")
            return []

    def insertar_usuario(self, user):
        try:
            query = "INSERT INTO usuarios_biblioteca (nombre) VALUES (%s)"
            self.cursor.execute(query, (user,))
            self.conexion.commit()
            print(f"✅ Usuario '{user}' insertado correctamente en la base de datos.")
        except mysql.connector.Error as e:
            print(f"❌ Error al insertar usuario: {e}")

    def prestar_elemento_bbdd(self, id_item, id_user):
        # si no existe la tabla préstamo se crea
        query_tabla_prestamo = """
            CREATE TABLE IF NOT EXISTS prestamos(
            id_item INT NOT NULL,
            id_user INT NOT NULL,
            fecha_prestamo DATETIME NOT NULL,
            fecha_devolucion DATETIME NOT NULL,
            PRIMARY KEY (id_item, id_user, fecha_prestamo),
            FOREIGN KEY (id_item) REFERENCES catalogo_biblioteca(id_material) ON DELETE CASCADE,
            FOREIGN KEY (id_user) REFERENCES usuarios_biblioteca(id_usuario) ON DELETE CASCADE 
            );"""
        self.ejecucion_query(query_tabla_prestamo)

        query_item = "SELECT * FROM catalogo_biblioteca WHERE id_material = %s"
        query_user = "SELECT * FROM usuarios_biblioteca WHERE id_usuario = %s"
        try:            
            self.cursor.execute(query_item, (id_item,))
            item = self.cursor.fetchone()
            if not item:
                print(f"❌ No se encontró material con ID {id_item}")
                return
            
            self.cursor.execute(query_user, (id_user,))
            user = self.cursor.fetchone()
            if not user:
                print(f"❌ No se encontró usuario con ID {id_user}")
                return
        
            # Marcar como prestado
            self.cursor.execute("UPDATE catalogo_biblioteca SET prestado = TRUE WHERE id_material = %s", (id_item,))
            self.conexion.commit()
           
            query_insert_ptmo = "INSERT INTO prestamos (id_item, id_user, fecha_prestamo, fecha_devolucion) VALUES (%s, %s, %s, %s)"
            fecha_prestamo = datetime.now()
            fecha_devolucion = fecha_prestamo + timedelta(days=14)
            self.ejecucion_query(query_insert_ptmo, (id_item, id_user, fecha_prestamo, fecha_devolucion))
        
        except mysql.connector.Error as e:
            print(f"❌ Error al prestar elemento: {e}")
        
    def borrar_tabla(self, tabla):
        query_borrar = f"DROP TABLE IF EXISTS {tabla}"
        self.ejecucion_query(query_borrar)

