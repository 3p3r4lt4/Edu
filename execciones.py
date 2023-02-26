def divide(num):
    try:
        num=int(num)
        if num %2 !=0:
            raise RuntimeError('El valor introducido no es par')
        resultado = 100/num
        print(resultado)

    except (ValueError,ZeroDivisionError):
        print('el valor no es valido')  
    except RuntimeError as re:  
        print(re)      