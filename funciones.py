def menu():
    print("*** MENU PRINCIPAL ***")
    print("1.- Turistas por país.")
    print("2.- Turista por mes.")
    print("3.- Eliminar turista.")
    print("4.- Salir")

def turistas_por_pais(pais, turistas):
    turistas_encontrados = []
    for turista in turistas:
        #print(turistas[turista][1])
        if turistas[turista][1] == pais:
            turistas_encontrados.append(turistas[turista][0])
    return turistas_encontrados    

def turistas_por_mes(mes, turistas):
    turistas_mensuales = 0
    for turista in turistas:
        mes_turista = int(turistas[turista][2][3] + turistas[turista][2][4])
        if mes_turista == mes:
            turistas_mensuales += 1
    proporcion_turistas = round((turistas_mensuales / len(turistas)),1) * 100
    print(f"el numero de turistas equivale a {proporcion_turistas}%")

def eliminar_turista(turistas):
    turista_a_eliminar = input("Ingrese el nombre del turista que desea eliminar de la lista: ")
    turista_a_eliminar = turista_a_eliminar.lower()
    for turista in turistas:
        turista_seleccionado = (turistas[turista][0]).lower()
        if turista_a_eliminar == turista_seleccionado:
            turistas.pop(turista)
            print("Turista eliminado con éxito.")
            return 0
    print("Turista no encontrado. No se pudo eliminar.")
    return 0