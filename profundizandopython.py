help(str.join)

tupla_str = ('hola','mundo','universidad','pyhton')

mensaje ='    '.join(tupla_str)
print(f'mensaje: {mensaje}')

cadena ='HolaMundo'
mensaje2='.'.join(cadena)
print(f'mensaje: {mensaje2}')

print("=======================")

diccionario ={'nombre':'juan','apellido':'perez','edad':'18'}
llaves='-'.join(diccionario.keys())
valores='-'.join(diccionario.values())

print(f'llaves: {llaves}, type: {type(llaves)}')
print(f'valores: {valores}, type: {type(valores)}')