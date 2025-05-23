# ===============================================
# ✅ Ejercicio 6: Lista de la Compra
# ===============================================
# 1. Lista vacía llamada lista_compra.
# 2. Pide 5 productos y añádelos.
# 3. Muestra la lista.
# 4. Permite eliminar un producto.
# 5. Muestra la lista final y cantidad restante.
# 6. Guarda los datos en tareas.txt usando with open().
# 7. Usa try-except para manejar FileNotFoundError.


def init_list():
    lista = []
    while len(lista) < 5:
        producto = input("Introduce un producto:\n")
        lista.append(producto)
    print("Ya tienes tus primeros 5 productos")
    show_list(lista)
    save(lista)
    return lista

def delete_item(lista):
    while True:
        opt = int(input("¿Quieres eliminar algún producto? Introduce:\n" \
                "0- No quiero borrar\n" \
                "El número del producto:\n"))
        if opt not in range(1, len(lista) + 1):
            print("El elemento no se encuentra en la lista")
            break
        lista.pop(opt - 1)
        show_list(lista)
        save(lista)


def show_list(lista):
    for i, producto in enumerate(lista, start=1):
        print(f"{i}. {producto}")

def save(lista):
    try:
        with open("datos/tareas.txt", "w") as file:
            for product in lista:
                file.write(product + "\n")
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
    
def add_element(lista):
    prod = input("Introduce el producto:\n")
    if prod in lista:
        print("El elemento está duplicado\n" \
        "¿Quieres añadirlo de todos modos?")
        opt = input("S: sí // N: no\n").capitalize()
        if opt == "S":
                lista.append(prod)
                print(f"Se ha añadido el producto: {prod}")
        else:
            print("No se ha añadido el producto")
    else:
        lista.append(prod)
    save(lista)
    



def shopping_list():
    lista = init_list()
    while True:
        try:
            opt = int(input("Elige una opción:\n" \
            "1. Borrar elemento\n" \
            "2. Añadir elemento\n" \
            "3. Mostar lista\n" \
            "4. Salir\n"))
            match opt:
                case 1:
                    delete_item(lista)
                case 2:
                    add_element(lista)
                case 3:
                    show_list(lista)
                case 4:
                    print("Saliendo...")
                    break
                case _:
                    print("Introduce una opción válida del 1 al 4.\n")
        except ValueError as e:
            print(f"ERROR: {e}")


if __name__ =="__main__":
    shopping_list()
    