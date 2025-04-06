odd={1,3,5,7,9}
eveb={2,4,6,8}
primes={2,3,5,7,11}

u=odd.union(eveb)
print(u)

i=odd.intersection(eveb)
print(i)

evp=eveb.intersection(primes)
print(evp)

new=u.difference(odd)
print(new)

sysdiff=u.symmetric_difference(eveb)
print(sysdiff)

eveb.update(primes)
print(eveb)

print(eveb.issubset(u))
print(eveb)