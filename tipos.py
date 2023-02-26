#Area del circulo : PI*r2


pi= 3.1416
radio=2
a= 4
area=pi*radio**2

print('El area del circulo de radio',radio)
print("======================")
b=round(area,2)
print(b)
print('Area de circulo de radio'+' '+str(radio) + '=' + str(area))


plantilla_vars = 'a={} b={}'
print(plantilla_vars.format(a,b))

plantilla = f'a={a} , b={b} , a={a+b}'
print("========")
print(plantilla)

z= 123.455667
print(f'{z:.2f}')