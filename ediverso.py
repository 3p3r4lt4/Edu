lugares_favoritos ={'Juan':['huacachina','paracas'],'Pedro':['Chan Chan','Huacas del Sol y de la Luna','Huanchaco'],'saul':['Sacsayhuamán','Fortaleza de Ollantaytambo.'],'sebastian':['mancora','manglares de tumbes']}
i=1
l=0
z =len(lugares_favoritos.keys())
#Proceso e Impresion
for name, favoritos in lugares_favoritos.items():
    print(f"\nNro.{i}.- {name.title()}'s His favorite place is:")
    i+=1
  
    for f in favoritos:
        print(f"\t{f.title()}")


for m in    lugares_favoritos.values():
    l+=len(m)
p=l/z

print(f"El promedio de lugares favoritos por usuario es: {round(p,0)} ") 