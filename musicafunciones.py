def menu():
    print("*** MENÚ PRINCIPAL ***")
    print("1. Stock por Género.")
    print("2. Búsqueda por Año de Lanzamiento.")
    print("3. Actualizar Cantidad de Stock.")
    print("4. Salir.")

def stock_genero(genero_buscado,albums,inventario):
    stock = 0
    for album in albums:
        if genero_buscado.lower() == albums[album][2].lower():
                stock += inventario[album][0]
    if stock == 0:
        print(f"El stock total para {genero_buscado} es: 0.")
    else:
        print(f"El stock total para {genero_buscado} es: {stock}")

def busqueda_anio(anio_minimo, anio_maximo,albums):
    lista_final =[]
    while True:
        try:
            for album in albums:
                if albums[album][3] in range(anio_minimo,anio_maximo):
                    lista_final.append(f"{albums[album][1]}--{albums[album][0]}")
            if lista_final == []:
                print("No hay álbumes en ese rango de años.")
                break
            else: 
                lista_final.sort()
                print (f"Los álbumes entre los años consultados son: {lista_final}")
                break
        except ValueError:
            print("Debe ingresar valores enteros!!")

def actualizar_stock(album_id, nueva_cantidad, inventario):
    flag_interior = True
    for album in inventario:
        if album_id == album:
            inventario[album][0] = nueva_cantidad
            print("Stock actualizado!!")
            flag_interior = False
    if flag_interior:
        print("El álbum no existe!!")