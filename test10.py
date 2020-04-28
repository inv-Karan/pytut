def gensquares(N):
    for i in range(N):
        yield i**2

for x in gensquares():
    print(x)

#######################

import random

random.randint(1,10)

def rand_num(low,high,n):

    for i in range(n):
        yield random.randint(low,high)

for num in rand_num(1,10,12):
    print(num)