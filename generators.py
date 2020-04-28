def create_cubes(n):
    result = []
    for x in range(n):
        result.append(x**3)
    return result

for x in create_cubes(10):
    print(x)

def create_cubes(n):

    for x in range(n):
        yield x**3

for x in create_cubes(10000):
    print(x)

list(create_cubes(10))
print(list)
list(create_cubes(10000))
print(list)

def gen_fibon(n):

    a=1
    b=1

    for i in range(n):
        yield a
        a,b = b,a+b

for number in gen_fibon(10):
    print(number)

def gen_fibon(n):

    a=1
    b=1
    output = []

    for i in range(n):
        output.append(a)
        a,b = a,a+b
    return output

def simple_gen():
    for x in range(3):
        yield x

for number in simple_gen():
    print(number)

g = simple_gen()

print(next(g)) # run it 4 times

s = 'hello'

for letter in s:
    print(letter)

next(s) # will generate data-type error because next only works with integer data

s_iter = iter(s)

next(s_iter) # run it 6 times

