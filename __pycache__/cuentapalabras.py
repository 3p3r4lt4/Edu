# usando diccionarios 
cuentapalabras = dict()
texto = "En un día como hoy, estamos viendo el uso de diccionarios en Python con un valor por defecto".split(" ")
#print(texto)

for p in texto:
    # hacemos la palabra lowercase
    palabra = p.lower()
    print(cuentapalabras)
    if palabra in cuentapalabras:
        cuentapalabras[palabra] += 1
    else:
        cuentapalabras[palabra] = 1
print(cuentapalabras)