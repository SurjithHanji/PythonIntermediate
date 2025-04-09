from itertools import product

a=[1,2]
b=[3,4]
prod=product(a,b)
print(list(prod))

c=[5]
prod1=product(a,c,repeat=2)
print(list(prod1))