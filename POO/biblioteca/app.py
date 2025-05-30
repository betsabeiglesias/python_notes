from classes.gestor_biblioteca import Gestor #,biblioteca_de_ejemplo
from classes.db import Gestor_BBDD


if __name__ == "__main__":

 
    biblio = Gestor("Central")
    
    db = Gestor_BBDD()
  
    db.conectar_db()
    db.borrar_tabla("prestamos")
    db.crear_tablas()
    # biblio.db.conectar_db()
    # biblio.cargar_materiales_pickle()
    # biblio.cargar_usuarios_pickle()
    while True:
        opt = int(input("--- BIENVENIDO A LA BIBLIOTECA ---\n"
        "Elige tu opción:\n" \
        "0. Agregar usuario\n"
        "1. Listar elementos\n" \
        "2. Mostar elemento único\n" \
        "3. Prestar elemento\n" \
        "4. Mostrar libros\n"
        "5. Mostrar revistas\n"
        "6. Mostrar DVD's\n" \
        "7. Pedir y agregar material\n" \
        "8. Mostrar elemento cón código\n" \
        "9. Borrar elemento cón código\n" \
        "10.Mostrar usuario\n"
        "11.Salir\n"))
    
        match opt:
            case 0:
                name = input("Introduce el nombre de socio: \n")
                user = biblio.agregar_usuario(name)
                db.insertar_usuario(user.nombre)
            case 1:
                biblio.listar_elementos()
            case 2:
                ind = int(input("Introduce el número de elemento: \n"))
                biblio.mostar_elemento(ind)          
            case 3:
                ind = int(input("Introduce el número de elemento: \n"))
                user = int(input("Introduce el nº de socio de la biblioteca: "))
                #biblio.prestar_elemento(ind, user)
                db.prestar_elemento_bbdd(ind,user)
            case 4:
                biblio.mostrar_libros()
                query_filtro_libros ="""
                SELECT * FROM catalogo_biblioteca RIGHT JOIN libros 
                    ON catalogo_biblioteca.id_material = libros.id_material;;"""
                db.select_query(query_filtro_libros)

            case 5:
                biblio.mostrar_revistas()
                query_filtro_revistas ="""
                SELECT * FROM catalogo_biblioteca RIGHT JOIN revistas 
                    ON catalogo_biblioteca.id_material = revistas.id_material;;"""
                db.select_query(query_filtro_revistas)
            case 6:
                biblio.mostrar_dvd()
                query_filtro_dvds ="""
                SELECT * FROM catalogo_biblioteca RIGHT JOIN dvds 
                    ON catalogo_biblioteca.id_material = dvds.id_material;;"""
                db.select_query(query_filtro_dvds)
            case 7:
                nuevo = biblio.pedir_y_agregar_material()
                db.insertar_material_bbdd(nuevo)
            
            case 8:
                cod = input("Introduce código elemento; \n")
                biblio.mostrar_elemento_codigo(cod)
            case 9:
                cod = input("Introduce código elemento; \n")
                biblio.borrar_elemento_codigo(cod)
            case 10:
                usuarios = db.select_query("SELECT * FROM usuarios_biblioteca")
                for us in usuarios:
                    print (us)
                # if not biblio.usuarios:
                #     print("No hay usuarios registrados.")
                # else:
                #     for usuario in biblio.usuarios:
                #         usuario.mostrar_info()
            case 11:
                print("Hasta la próxima")
                db.desconectar_db()
                break
            case _:
                print ("Opción no válida")
