"""from mi_clase import MiClase

#help(MiClase)
print(MiClase.__doc__)
print(MiClase.__init__.__doc__) """

#help(str.split)

cursos ='Java Python JavaScript Angular Spring Excel'

lista_cursos =cursos.split()

print(f'Lista de cursos: {lista_cursos}')

cursos_separados_coma ='Java,Python,JavaScript,Angular,Spring,Excel'
se_comas=cursos_separados_coma.split(',')
print(f'Lista de cursos: {se_comas}')
