s = set()
s.add(1)
s.add(2)
print(s)

s.clear()
print(s)

# copy
s = {1,2,3}
sc = s.copy()
print(sc)
s.add(4)
print(s)
print(sc)

# difference
print(s.difference(sc))
s1 = {1,2,3}
s2 = {1,4,5}
s1.difference_update(s2)
print(s1)

# discard
s1.discard(2)
print(s1)

# intersection and intersection_update
s1 = {1,2,3}
s2 = {1,2,4}
print(s1.intersection(s2))
print(s1)
s1.intersection_update(s2)
print(s1)

# isdisjoint
s1 = {1,2}
s2 = {1,2,4}
s3 = {5}
print(s1.isdisjoint(s2))
print(s1.isdisjoint(s3))

# issubset
print(s1.issubset(s2))

# issuperset
print(s2.issuperset(s1))

# symmetric_difference and symmetric_update
print(s1.symmetric_difference(s2))
print(s1.union(s2))
print(s1)

# update
s1.update(s2)
print(s1)