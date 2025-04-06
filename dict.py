mydicg={
    "name":"Surjith",
    "usn":"1cr22cs197",
    "city":"Belgavi"
}
print(mydicg)

my=dict(name="abhi",age=19,address="kungatolli")
print(my)

values=mydicg["name"]
print(values)

mydicg["email"]="abc@gmail.com"
print(mydicg)

del my["age"]
print(my)

######## we can use pop,popitem() method also ##########

if "name" in mydicg:
    print(mydicg["name"])

try:
    print(mydicg["name"])
except:
    print("error")

for key in mydicg:
    print(key)

for values in mydicg.values():
    print(values,end=" ")


for key,values in mydicg.items():
    print(key,values)

modi=mydicg  #############   we can use .copy() method
print(modi)

modi["name"]="Akash"
print(modi)
print(mydicg)

my.update(mydicg)
print(my)