"""
nombre ='Juan'
edad = 28
sueldo =3000.525
mensaje = f'Nombre {nombre}  Edad {edad}  Sueldo {sueldo:.2f}'

print(mensaje)  """

# multiplicacion tuplas

#resultado = 5*('Hola',6)

#print(f'Resultado : {resultado}')

# multiplicacion de lista 


"""
resultado = 10*[7]

print(f'Resultado : {resultado} , largo: {len(resultado)}')

"""
"""
resultado ='Hola \'Mundo'
print(f'Resultado : {resultado}')
"""

"""
resultado ='Se va a eliminar el punto.\b\b'
print(f'Resultado : {resultado}')

"""

"""
#caracter
resultado='c:\\nuevo\\juan'

print(f'Resultado:{resultado}')
"""

#raw string

"""
resultado=r'Cadena con \n salto de linea'
print(f'Resultado:{resultado}')

"""


"""
#caracteres unicode 

print('Hola\u0020Mundo')

print('Notacion simple:','\u0041')

print('Notacion extendida:','\U00000041')

print('Notacion hexadecimal:','\x41')

print('Corazon:','\u2665')
print('Cara sonriendo:','\U0001f600')

print('Serpiente:','\U0001f40D')


#caracter ascii
print("==========================")
caracter = chr(65)

print('A mayuscula:' , caracter)

caracter = chr(64)

print('Simbolo @ :' , caracter)


"""

"""
mensaje =b'Universidad Python'

print(mensaje[0])
print(chr(mensaje[0]))

lista_caracteres = mensaje.split()

print(lista_caracteres)

"""

from urllib.request import urlopen

with urlopen('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt') as mensaje:
    #contenido = mensaje.read()
    contenido = mensaje.read().decode('utf-8')
    print(contenido)