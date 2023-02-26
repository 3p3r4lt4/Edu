class Mascota:
    def __init__(self,nombre,dueño):
        self.nombre=nombre
        self.dueño=dueño

    def jugar(self):
        print(f'Juega {self.nombre}')    

class Perro(Mascota):

    def __init__(self, nombre, dueño,raza):
        super().__init__(nombre, dueño)
        self.raza=raza



    def jugar(self):
        super().jugar()
        print('correr y ladrar')      


    def sonido(self):
        print('guauuu')


class PerroMordedor(Perro):

    def morder(self):
        print("mordiendo")


if __name__=='__main__':

    mascota = Mascota('nieve','maria')
    print(f'Nombre:{mascota.nombre}; Dueño:{mascota.dueño}')

    perro = Perro('sultan','manolo','samolledo')
    perro.jugar()
    print(f'Nombre:{perro.nombre}; Dueño:{perro.dueño}; raza :{perro.raza}')
    p_mordedor = PerroMordedor('rocky','alberto','caniche')
    p_mordedor.morder()
    print(f'Nombre:{p_mordedor.nombre}; Dueño:{p_mordedor.dueño}')
    print(f'Nombre:{p_mordedor.nombre}; Dueño:{p_mordedor.dueño} ; raza :{p_mordedor.raza}')

    print(isinstance(p_mordedor,Perro))
    print(isinstance(p_mordedor,Mascota))
    print(isinstance(Perro,PerroMordedor))
    print(issubclass(PerroMordedor,Mascota))


    if hasattr(mascota,'raza'):
        print(getattr(mascota,'raza',None))

    else:
        print('mascota no define el atributo raza')    
