def f(a,b,c):
    print(f'a={a};b={b};c={c}')

lista = [4,5,6]    
tupla = 7,8,9

f(*lista)
f(*tupla)
dicc={'b':2,'c':3,'a':1}
f(**dicc)