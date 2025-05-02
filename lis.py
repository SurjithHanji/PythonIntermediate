def food(a,b,c):
    print(a,b,c)

my_lit=[0,1,2]
food(*my_lit)

my_dict={'a':1,'b':2,'c':3}
food(*my_dict)


nums=(1,2,3,4,5,6)
begin,*last=nums
print(begin)
print(last)

*beg,las=nums
print(beg)
print(las)

be,*mid,la=nums
print(be)
print(mid)
print(la)