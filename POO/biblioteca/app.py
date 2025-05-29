from classes.gestor_biblioteca import Gestor,biblioteca_de_ejemplo


if __name__ == "__main__":
    # biblio = Gestor("Central")
    biblio = biblioteca_de_ejemplo()
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
                biblio.agregar_usuario(name)
            case 1:
                biblio.listar_elementos()
            case 2:
                ind = int(input("Introduce el número de elemento: \n"))
                biblio.mostar_elemento(ind)          
            case 3:
                ind = int(input("Introduce el número de elemento: \n"))
                user = int(input("Introduce el nº de socio de la biblioteca: "))
                biblio.prestar_elemento(ind, user)
            case 4:
                biblio.mostrar_libros()
            case 5:
                biblio.mostrar_revistas()
            case 6:
                biblio.mostrar_dvd()
            case 7:
                biblio.pedir_y_agregar_material()
            case 8:
                cod = input("Introduce código elemento; \n")
                biblio.mostrar_elemento_codigo(cod)
            case 9:
                cod = input("Introduce código elemento; \n")
                biblio.borrar_elemento_codigo(cod)
            case 10:
                if not biblio.usuarios:
                    print("No hay usuarios registrados.")
                else:
                    for usuario in biblio.usuarios:
                        usuario.mostrar_info()
            case 11:
                print("Hasta la próxima")
                break
            case _:
                print ("Opción no válida")
