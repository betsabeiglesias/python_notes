# ===============================================
# 🚀 Desafío: Contador de Palabras en Archivo
# ===============================================
# 1. Pide nombre de archivo.
# 2. Lee el contenido.
# 3. Limpia texto: minúsculas, quita puntuación.
# 4. Divide en palabras.
# 5. Usa diccionario para contar frecuencias.
# 6. Muestra top 10 palabras más frecuentes.
# 7. Maneja FileNotFoundError si el archivo no existe.


def get_namefile():
    name = input("Introduce el nombre del archivo a leer:")
    name_ext = name + ".txt"
    try:
        with open(name_ext, "r") as file:
            contenido = file.read()
            print("EXITO")

    except FileNotFoundError as e:
        print(f"ERROR: {e}")

def clean_content(contenido):
    contenido = contenido.lower()
    

    


def desafio():
    get_namefile()




if __name__ == "__main__":
    desafio()