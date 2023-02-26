
catalogo= {'peliculas':{},'series':{},'documentales':{}}

catalogo['peliculas']['drama'] =['pelicula 1','pelicula 2']
catalogo['peliculas']['terror'] =['pelicula 3','pelicula 4']

catalogo['series']['comedia'] =['serie 1','serie 2','serie 3']


catalogo['documentales']['belicos'] =[]
catalogo['documentales']['animales'] =['documentales','documentales 2']

#print (catalogo)

for medio in catalogo:
    print('medio:' ,medio)
    for categoria , medios in catalogo[medio].items():
        print(f'Categoria: {categoria} > {medios}')
        print("===================================")
  