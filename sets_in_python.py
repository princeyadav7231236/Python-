s = set()
# print(type(s))
l = [1, 1, 2, 3, 8, 8, 4, 6, 3, 5]
set1 = set(l)
print(set1)
print(type(set1))

s.add(45)
s.add(55)
s.add(5)
print(s.isdisjoint(set1))
print(s.intersection(set1))
print(s.union(set1))
