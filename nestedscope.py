x=25
def printer():
    x=50
    return x
print(x)
print(printer())

name = 'THIS IS A GLOBAL THING'
def greet():
    name = 'THIS IS EMCLOSING THING'
    def hello():
        name = 'THIS IS LOCAL THING'
        print('Hello '+name)
    hello()
greet()

x=50
def func(x):
    print(f'X is {x}')
    x=200
    print(f'I JUST LOCALLY CHANGED X to {x}')
def func():
    global x
    print(f'X is {x}')
    x='NEW VALUE'
    print(f'I JUST LOCALLY CHANGED X TO {x}')