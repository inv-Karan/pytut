s = set()

s.add(1)
s.add(2)

print(s)

s.clear()

s = {1,2,3}

sc = s.copy()

print(sc)

s.add(4)

print(s)
print(sc)

s.difference(sc)
s.difference_update(sc)

print(s)

s.discard(12)

s1 = {1,2,3}
s2 = {1,2,4}

s1.intersection(s2)
s1.intersection_update(s2)

s1 = {1,2}
s2 = {1,2,4}
s3 = {5}

s1.isdisjoint(s2)
s1.isdisjoint(s3)

s1.issubset(s2)
s2.issuperset(s1)

s1.symmetric_difference(s2)
s1.union(s2)

s1.update(s2)