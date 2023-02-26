from itertools import count
from operator import index


saludo ="hola mundo"
list =[1,3,[3,4],6,"hola"]
print(saludo.capitalize())
print(saludo.title())
print(saludo.upper())
print(saludo.split())
list.append(7)
list.__delitem__(1)
print(list)

