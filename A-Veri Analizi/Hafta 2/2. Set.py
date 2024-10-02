# Set - Kumeler
kume1 = set([1,3,5])
kume2 = set([1,2,3])

#difference : iki kumenin farki
print(kume1.difference(kume2))
print(kume2.difference(kume1))

print(kume1-kume2)
print(kume2-kume1)

#intersection : ortak olanlari verir
print(kume1.intersection(kume2))
print(kume2.intersection(kume1))

print(kume1 & kume2)

#union: iki kumeyi toplar
print(kume1.union(kume2))

#isdisjoint() : iki kumenin kesimi bos mu
set1 = set([7,8,9])
set2 = set([1,2,3])

print(set1.isdisjoint(set2))

