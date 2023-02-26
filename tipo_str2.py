
nombre='juan'
edad=28
sueldo =3000

mensaje_con_formato = 'Min nombre es %s y tengo %d años'%(nombre,edad)
#print(mensaje_con_formato)


persona=('karla','gomez',5000.00)
mensaje_con_formato ='hola %s %s . tu sueldo es %.2f'%persona
#print(mensaje_con_formato)

mensaje = 'Nombre {0} Edad {1} sueldo  {2:.2f}'.format(nombre,edad,sueldo)
#print(mensaje)


mensaje= 'Nombre {n} Edad {e}  Sueldo {s:.2f}'.format(n=nombre,e=edad,s=sueldo)
print(mensaje)