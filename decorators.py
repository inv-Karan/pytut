def func():
    return 1
func()

def hello():
    return "Hello!"
hello()

def hello(name='Jose'):
    print('The hello() function has been executed!')

    def greet():
        return '\t This is the greet() fun inside hello!'

    def welcome():
        return '\t This is welcome() inside hello'

    print(greet())
    print(welcome())
    print('This is the end of the hello function!')

    print("I am going to return function!!")

    if name == 'Jose':
        return greet
    else:
        return welcome

    my_new_func = hello('Jose')

    print(my_new_func())

def cool():

    def super_cool():
        return 'I am very cool!'

    return super_cool
    some_func = cool()
    print(some_func())

def hello():
    return 'Hi Jose!'

def other(some_def_func):
    print('Other code runs here!')
    print(some_def_func())

hello()

other(hello)

def new_decorator(original_func):

    def wrap_func():

        print('Some extra code, before the original function')

        original_func()

        print('Some extra code, after the original function!')

    return wrap_func

@new_decorator
def func_needs_decorator():

    print("I want to be decorated!!")

    return func_needs_decorator

func_needs_decorator()

decorated_func = new_decorator(func_needs_decorator)

decorated_func()

