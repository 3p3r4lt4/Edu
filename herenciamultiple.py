class A:

    def saludar(self,nombre):
        print('hola',nombre)



    def ma(self):
        print('soy A')

class B:

    def saludar(self,nombre):
        print('nos vamos de fiesta')

    def mb(self):
        print('soy B')        

class C(A,B):

    def saludar(self,nombre):
        print('parece que va llover')

    def mc(self):
        print('soy c')        


if __name__=='__main__':
    ob_c= C()
    ob_c.ma()    
    ob_c.mb()    
    ob_c.mc()
    ob_c.saludar('hhghhg')