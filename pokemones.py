# Diccionario para almacenar pokemones
pokemones = {}

# Tipos válidos
tipos_validos = {"fuego", "agua", "hierba", "veneno", "psiquico", "luchador", "eléctrico"}

def validar_codigo(codigo):
    return (
        len(codigo) >= 8
        and any(c.isdigit() for c in codigo)
        and any(c.isalpha() for c in codigo)
        and ' ' not in codigo
    )

def ingresar_pokemon():
    try:
        id_pokemon = int(input("Ingrese el Id de pokemon: "))
        nombre = input("Ingrese nombre de pokemon: ").strip().lower()

        if nombre in pokemones:
            print("Ese nombre de pokemon ya existe.")
            return

        codigo = input("Ingrese código: ").strip()
        tipo = input("Ingrese tipo: ").strip().lower()

        if tipo not in tipos_validos:
            print("Debe ingresar: “fuego”, “agua”, “hierba”, “veneno”, “psiquico”, “luchador”, “eléctrico”.")
            return

        if not validar_codigo(codigo):
            print("Código inválido. Debe tener al menos 8 caracteres, una letra, un número y sin espacios.")
            return

        pokemones[nombre] = {
            "id": id_pokemon,
            "codigo": codigo,
            "tipo": tipo
        }

        print("Pokemon ingresado con éxito!!")

    except ValueError:
        print("Id inválido. Debe ser un número entero.")

def buscar_pokemon():
    nombre = input("Ingrese pokemon a buscar: ").strip().lower()
    if nombre in pokemones:
        datos = pokemones[nombre]
        print(f"El tipo de pokemon es: {datos['tipo']} y su código es: {datos['codigo']}")
    else:
        print("El pokemon no se encuentra.")

def eliminar_pokemon():
    nombre = input("Ingrese usuario a buscar: ").strip().lower()
    if nombre in pokemones:
        pokemones.pop(nombre)
        print("Usuario eliminado con éxito!")
    else:
        print("No se pudo eliminar usuario!")

def listar_pokemones():
    if not pokemones:
        print("No hay pokemones registrados.")
    else:
        for nombre, datos in pokemones.items():
            print(f"ID: {datos['id']} - Nombre: {nombre}")

def menu():
    while True:
        print("\nMENU PRINCIPAL")
        print("1.- Ingresar pokemon.")
        print("2.- Buscar pokemon.")
        print("3.- Eliminar pokemon")
        print("4.- Listar pokemones")
        print("5.- Salir.")
        opcion = input("Ingrese opción: ").strip()

        if opcion == "1":
            ingresar_pokemon()
        elif opcion == "2":
            buscar_pokemon()
        elif opcion == "3":
            eliminar_pokemon()
        elif opcion == "4":
            listar_pokemones()
        elif opcion == "5":
            print("Saliendo del programa.")
            break
        else:
            print("Debe seleccionar una opción válida.")

# Código principal
if __name__ == "__main__":
    menu()
