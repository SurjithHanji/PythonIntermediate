zeros=[0]*10
print(zeros)

ones=[0,1]*10
print(ones)

se="ab"*10
print(se)

def food(a,b,*args,**kwargs):
    print(a,b)
    print(a)
    for arg in args:
        print(arg)

    for key in kwargs:
        print(key,kwargs[key])

food(1,2,3,4,six=6,seven=7)