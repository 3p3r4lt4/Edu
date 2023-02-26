for _ in range(3):
    try:
        num = int(input("\t\nintroduce un número"))
        resultado = 100/num
        print(resultado)

    except:
        print('El valor es incorrecto')    