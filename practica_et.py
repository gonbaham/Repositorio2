from musicafunciones import menu, stock_genero, busqueda_anio, actualizar_stock

albums = {
    "ALB001":["A Night at the Opera","Queen","Rock",1975,"Vinilo"],
    "ALB002":["Thriller","Michael Jackson","Pop",1982,"CD"],
    "ALB003":["Dark Side of the Moon","Pink Floyd","Rock",1973,"Vinilo"],
    "ALB004":["21","Adele","Pop",2011,"Digital"],
    "ALB005":["Abbey Road","The Beatles","Rock",1969,"Vinilo"],
    "ALB006":["Back in Black","AC/DC","Rock",1980,"CD"],
    "ALB007":["The Wall","Pink Floyd","Rock",1979,"CD"],
    "ALB008":["Lemonade","Beyoncé","R&B",2016,"Digital"]
    #...
}

inventario = {
    "ALB001":[6],
    "ALB002":[7],
    "ALB003":[8],
    "ALB004":[9],
    "ALB005":[10],
    "ALB006":[0],
    "ALB007":[11],
    "ALB008":[12],
}




while True:
    menu()
    try:    
        opt = int(input("Ingrese una opción: "))
        if opt == 1:
            genero_ingresado= input("Ingrese género a consultar: ")
            stock_genero(genero_ingresado, albums, inventario)
        elif opt == 2:
            while True:
                try:
                    anio_min = int(input("Ingrese año mínimo: "))
                    anio_max = int(input("Ingrese año máximo: "))
                    busqueda_anio(anio_min,anio_max,albums)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros!!")
        elif opt == 3:
            flag_ciclo = True
            while flag_ciclo:
                flag_interior = True
                id_album = input("Ingrese ID de álbum a actualizar: ")
                cantidad_nueva = int(input("Ingrese nueva cantidad: "))
                actualizar_stock(id_album,cantidad_nueva,inventario)
                continuar = input("¿Desea actualizar otro stock (s/n)?: ")
                if continuar.lower() == "no":
                    flag_ciclo = False
        elif opt == 4:
            print("Programa finalizado.")
            break
        else: 
            print("Debe seleccionar una opción válida!!")
    except ValueError:
        print("Debe ingresar valores enteros!!")