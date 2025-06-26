deuda = 100000
saldo = 1000000
diferencia = 0
montoIngresado = 0
totalSimulacion = 0
simulacionActual = 1
while True:
    print("Bienvenido a la App del Banco. ¿Qué desea hacer?")
    print("1. Pagar con tarjeta de crédito.")
    print("2. Simular compras.")
    print("3. Salir. \n")
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print("Opcion no válida. Por favor seleccione una opción del 1 al 3.")
        continue
    if opcion == 1:
        print(f"Su deuda es de ${deuda} y su saldo es de ${saldo}.")
        try:
            montoIngresado = int(input("Ingrese el monto a pagar con su tarjeta: "))
        except ValueError:
            print("El monto ingresado no es válido. ")
            continue
        if montoIngresado >= 0 and montoIngresado <= saldo and montoIngresado <= deuda:
            deuda -= montoIngresado
            if deuda == 0:
                print("Has saldado tu deuda.")
        elif montoIngresado >= 0 and montoIngresado <= saldo and montoIngresado > deuda:
            if deuda == 0:
                saldo -= montoIngresado
            else: 
                diferencia = montoIngresado - deuda
                saldo -= diferencia
                deuda -= montoIngresado - diferencia
                print(f"Has saldado tu deuda, y tu nuevo saldo es ${saldo}.")
        else: 
            print("El monto ingresado no es válido.")
    elif opcion == 2:
        while simulacionActual != 0:
            try:
                simulacionActual = int(input("Ingrese el monto de su compra. Si desea finalizar su simulacion ingrese 0: "))
            except ValueError:
                print("Monto no válido.")
                continue
            if simulacionActual > 0:
                totalSimulacion += simulacionActual
                print(f"Su simulación de compra actualmente acumula un monto de ${totalSimulacion}")
            elif simulacionActual < 0:
                print("Monto no válido.")
            elif simulacionActual == 0:
                saldo -= totalSimulacion
                print(f"Simulacion de compra exitosa. Su nuevo saldo en la tarjeta es ${saldo}")
                totalSimulacion = 0
            else:
                print("Monto no valido. ")
    elif opcion == 3:
        print("Gracias por usar la app del banco.")
        break
    else: 
        print("La opcion ingresada no es valida. ")
            