from collections import defaultdict
d = {'k1':1}
d[k1]
d[k2] # error

d = defaultdict(object)
d[one]

for item in d:
    print(item)

d = defaultdict(lambda:0)
d[one]
d[two]