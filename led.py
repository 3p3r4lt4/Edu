from turtle import color


class Led:

    intensidad =[1,2,3]

    def __init__(self, color, intensidad=1):
        self.__color =color
        self.__intensidad = intensidad
        self.__encendido=False

    def aumentar_intensidad(self):
        if self.__encendido and self.__intensidad <3:
            self.__intensidad+=5    

    def disminuir_intensidad(self):
        if self.__encendido and self.__intensidad > 1:
            self.__intensidad-=1        

    def get_color(self):
        return self.__color   
    def set_color(self,color):
        self.__color =color  

    def get_intensidad(self):
        return self.__intensidad   

    def set_intensidad(self,intensidad):
        print("no permitido")    

    def get_encendido(self):
        return self.__encendido  

    def set_encendido(self,encendido):
        self.__encendido =encendido                