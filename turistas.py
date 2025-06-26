from funciones import menu,turistas_por_pais, turistas_por_mes, eliminar_turista

turistas = {"001": ["John Doe", "Estados Unidos", "12-01-2024"],
                  "002": ["Emily Smith", "Estados Unidos", "23-03-2024"],
      "012": ["Julian Martinez", "Argentina", "19-09-2023"],
      "014": ["Agustin Morales", "Argentina", "28-03-2024"],
                  "005": ["Carlos Garcia", "Mexico", "10-05-2024"],
      "006": ["Maria Lopez", "Mexico", "08-12-2023"],
      "007": ["Joao Silva", "Brasil", "20-06-2024"],
	      "003": ["Michael Brown", "Estados Unidos", "05-07-2023"],
	      "004": ["Jessica Davis", "Estados Unidos", "15-11-2024"],
                  "008": ["Ana Santos", "Brasil", "03-10-2023"],
      "010": ["Martin Fernandez", "Argentina", "13-02-2023"],
      "011": ["Sofia Gomez", "Argentina", "07-04-2024"],
     }

menu()
while True:  
     try:
          opcion = int(input("Ingrese una opcion: "))
          if opcion == 1:
               pais = input("Ingrese pais a buscar: ")
               print(turistas_por_pais(pais, turistas))
          elif opcion == 2:
               while True:
                    try:  
                         mes = int(input("Ingrese mes a buscar: "))
                         if mes > 12 or mes < 1:
                              print("Ingrese un mes del 1 al 12")
                         else:
                              turistas_por_mes(mes,turistas)
                              break
                    except ValueError:
                         print("Ingrese un mes del 1 al 12, con numeros enteros.")
          elif opcion == 3:
               eliminar_turista()
          elif opcion == 4:
               print("Programa terminado...")
               break
          else:
               print("Ingrese una opcion válida del 1 al 4.")
     except ValueError:
          print("Ingrese un numero entero del 1 al 4.")
#print(turistas_por_pais("Mexico", turistas))
#turistas_por_mes(3, turistas)
#eliminar_turista(turistas)