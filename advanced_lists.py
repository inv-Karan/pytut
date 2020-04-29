l = [1,2,3]

l.append(4)

l.count(10)

l.count(1)

x = [1,2,3]

x.append([4,5])
print(x)

x = [1,2,3]

x.extend([4,5])
print(x)

l.index(2)

l.index(10)

l.insert(2,'inserted')
print(l)

ele = l.pop()
print(l)

l.pop(0)
print(l)

l.remove('inserted')
print(l)

l = [1,2,3,4,3]
l.remove(3)

l.reverse()
l.sort()