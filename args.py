def f(a,*args,b,**kwargs):
    print(f'a={a};b={b};args={args};kwargs={kwargs}')

    for a in args:
        print(a)

    for k,v in kwargs.items():
        print(f'key={k};value={v}')    

f(1,2,3,4,3,5,b=5,x=1,y=2,z=3)