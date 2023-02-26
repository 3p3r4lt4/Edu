while True:
       Edad = int(input("Digite su Edad\n"))

       if Edad <0:
           print("Ingrese una Edad Correcta")

       else:
            
            if Edad <3 :
                Costo=0
                print(f"El costo de entrada al Cine es: {Costo} Soles")
                break
            elif Edad <=12:
                Costo=10
                print(f"El costo de entrada al Cine es: {Costo} Soles")
                break

            elif Edad >12:
                Costo=15
                print(f"El costo de entrada al Cine es: {Costo} Soles")
                break