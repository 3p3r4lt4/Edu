
config ={'tipo':'par','num_elementos':3,'solo_positivos':True}

for k in config.keys():
    print(k)

for k,v in config.items():
    print(f'Clave ={k} ; Valor ={v}')

"""
config['tipo'] ='impar'

config['print_error'] = True

print(config)

del config['print_error']
print(config)

v = config.pop('tipo')
print(v)
print(config)

print('num_elementos' in config) """

