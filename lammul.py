a=[1,2,3,4,5]
b=map(lambda x:x*2,a)
print(list(b))

c=[x*2 for x in a]
print(c)

d=filter(lambda x:x%2==0,a)
print(list(d))

e=[x for x in a if x%2==0]
print(e)
