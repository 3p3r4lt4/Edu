texto = input("Introduce un texto\n")
num_vocales =0

for c in texto:
    if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
        num_vocales+=1
print(f'El numero de vocales del texto es {num_vocales}')        