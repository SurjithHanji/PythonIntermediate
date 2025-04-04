list=["hlo",2,True]
print(list)

list2=["hlo","dfjh","asfjk"]
print(list2)

item=list2[2]
print(item)

for x in list2:
    print(x)

if "banana" in list2:
    print("yes")
else:
    print("no")

print(len(list2))

s=[]
s.append("lemon")
s.append("apple")
print(s)

s.insert(0,"banana")
print(s)


a=s.pop()
print(a)
print(s)

b=s.remove("banana")
print(b)
print(s)


print(s.clear())