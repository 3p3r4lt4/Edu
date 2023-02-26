
from led import Led

if __name__=='__main__':
    l1 =Led('rojo',3)
    print(type(l1))

    print(l1.get_color())

    l2 =Led('azul',2)

    l2.set_color('amarillo')
    print(l2.get_color())


 
