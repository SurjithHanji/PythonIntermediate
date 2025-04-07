str="i am a programmer"
print(str)
print("hlo")
ch=str[0]
print(ch)
for char in str:
    print(char,end=" ")

#######  Strings are immutable ########

print("\n",str[:7])

stri=str.strip()
print(stri)

up=str.upper()
print(up)

lw=str.lower()
print(lw)

a=str.count('a')
print(a)

print(str.replace("Hello",""))

print(str.split(","))
print(''.join(str))

list=['a']*6
print(list)

