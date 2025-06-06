from classes.gestor_biblioteca import Gestor #,biblioteca_de_ejemplo
from classes.db import Gestor_BBDD




def main(): 
    biblio = Gestor("Central")
    
    db = Gestor_BBDD()
  
    # MySQL
    db.conectar_db()
    db.crear_tablas()

    # MongoDB
    db.conectar_mongo()
    db.crear_tabla_mongo()


    
    while True:
        opt = int(input("--- BIENVENIDO A LA BIBLIOTECA ---\n"
        "Elige tu opción:\n" \
        "0. Agregar usuario\n"\
        "1. Pedir y agregar material\n" \
        "2. Prestar material\n"\
        "3. Devolver material\n" \
        "4. Mostar Catálogo\n" \
        "5. Mostrar Usuarios\n" \
        "6. Mostrar Único Usuario\n" \
        # "4. Mostrar libros\n"
        # "5. Mostrar revistas\n"
        # "6. Mostrar DVD's\n" \1
        # "7. Pedir y agregar material\n" \
        # "8. Mostrar elemento cón código\n" \
        # "9. Borrar elemento cón código\n" \
        # "10.Mostrar usuario\n"
        "11.Salir\n"))
    
        match opt:
            case 0:
                db.insertar_usuario()
            case 1:
                item = db.pedir_material_usuario()
                if item:
                    db.insertar_material_bbdd(item)
            case 2:
                ind = int(input("Introduce el número de elemento: \n"))
                user = int(input("Introduce el nº de socio de la biblioteca: "))
                db.prestar_elemento_bbdd(ind,user)       
            case 3:
                ind = int(input("Introduce el número de elemento: \n"))
                user = int(input("Introduce el nº de socio de la biblioteca: "))
                db.devolver_elemento_bbdd(ind,user)    
            case 4:
                with db.Session() as session:
                    db.mostrar_catalogo(session)
            case 5:
                db.mostrar_usuarios()
            case 6:
                user = int(input("Introduce el nº de socio de la biblioteca: "))
                db.mostrar_unico_usuarios(user)
            #     biblio.mostrar_dvd()
            #     query_filtro_dvds ="""
            #     SELECT * FROM catalogo_biblioteca RIGHT JOIN dvds 
            #         ON catalogo_biblioteca.id_material = dvds.id_material;;"""
            #     db.select_query(query_filtro_dvds)
            # case 7:
            #     nuevo = biblio.pedir_y_agregar_material()
            #     db.insertar_material_bbdd(nuevo)
            
            # case 8:
            #     cod = input("Introduce código elemento; \n")
            #     biblio.mostrar_elemento_codigo(cod)
            # case 9:
            #     cod = input("Introduce código elemento; \n")
            #     biblio.borrar_elemento_codigo(cod)
            # case 10:
            #     usuarios = db.select_query("SELECT * FROM usuarios_biblioteca")
            #     # for us in usuarios:
            #     #     print (us) si no devolviesemos un db de panda, tendríamos que iterar sobre las tuplas que nos
            #                     #devuelve la consulta de fetchall.
            #     # if not biblio.usuarios:
            #     #     print("No hay usuarios registrados.")
            #     # else:
            #     #     for usuario in biblio.usuarios:
            #     #         usuario.mostrar_info()
            case 11:
                print("Hasta la próxima")
                break
            case _:
                print ("Opción no válida")


if __name__ == "__main__":
    main()