tup=(1,"dfh",34,True)
print(tup)
print(type(tup))

tup1=()
print(type(tup1))

tup2=tuple([1,2,"fd",2])
print(tup2)

print(tup2[0])

print(tup[-1])

########### Tuples are immutable ############


for i in tup2:
    print(i)

if 2 in tup2:
    print("yes")
else:
    print("no")


print(len(tup2))

print(tup2.count(2))

print(tup2.index(2))


########  slicing  #######

a=(12,34,41,"dfasjh",34)
print(a[0:])

print(a[:len(a)])

print(a[::-1])

print(a[::2])
my="max",23
name,age=my
print(name)
print(age)