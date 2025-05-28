from POO.biblioteca.gestor_biblioteca import Gestor, biblioteca_de_ejemplo



if __name__ == "__main__":
    # biblio = Biblioteca("Central")
    biblio = biblioteca_de_ejemplo()
    # biblio.cargar_materiales_pickle()
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
        "9. Borrar elemento cón código\n"
        "10. Salir\n"))
    
        match opt:
            case 0:
                biblio.cargar_usuarios()
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
                print("Hasta la próxima")
                break
            case _:
                print ("Opción no válida")
