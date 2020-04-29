d = {'k1':1,'k2':2}
{x:x**2 for x in range(10)}

{k:v**2 for k,v in zip(['a','b'],range(2))}

for k in d.iteritems():
    print(k)

for k in d.iterkeys():
    print(k)

for k in d.itervalues():
    print(k)

d.viewitems()
d.viewkeys()
d.viewvalues()