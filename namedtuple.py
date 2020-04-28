t = (1,2,3)

t[0]

############

from collections import namedtuple

Dog = namedtuple('Dog', 'age breed name')
sam = Dog(age=2,breed='Lab',name='Sammy')
sam
sam.age
sam[0]

Cat = namedtuple('Cat', 'fur claws name')
c = Cat(fur='Fuzzy',claws=False,name='kitty')
c.name
c[2]
c[1]
