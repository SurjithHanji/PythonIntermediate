import secrets
a=secrets.randbelow(10)
print(a)

b=secrets.randbits(4)
print(b)

mylist=list("ABCDEFGHIJK")
c=secrets.choice(mylist)
print(c)