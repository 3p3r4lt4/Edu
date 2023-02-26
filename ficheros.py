"""

f=open('ejemplo.txt','w')

try:
    f.write('primera linea\n')
    f.write('\n')
    f.write('Tercera linea\n')
    f.write('Cuarta linea\n')
    f.write('\n')
    f.write('Sexta linea')

finally:
    f.close()    

with open('ejemplo.txt','w')     as f:
    f.write('primera linea\n')
    f.write('\n')
    f.write('Tercera linea\n')
    f.write('Cuarta linea\n')
    f.write('\n')
    f.write('Sexta linea')

    """
with open('ejemplo.txt','r') as f  :
   ## contenido = f.read(3)
   ## print(contenido)
   for linea in f :
       #print(f'+{linea}+')
       print(linea.rstrip())
