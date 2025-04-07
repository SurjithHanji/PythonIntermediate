n=int(input())
num=n
l=len(str(n))
total=0
while n>0:
    n1=n%10
    total=total+(n1**l)
    n=n//10
if total==num:
    print("Armstrong number")
else:
    print("Not an Armstrong number")
