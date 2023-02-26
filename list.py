conjunto =['uno','dos',1,'python',[3,5]]

print(conjunto)
print('dos' in conjunto)
print(f'El numero de formatos soportados es {len(conjunto)}')
print(conjunto[2])
conjunto.append(9)
print(conjunto)
conjunto.remove(9)
print(conjunto)

del conjunto[0]
print(conjunto)

conjunto[0]='hola'
print(conjunto)