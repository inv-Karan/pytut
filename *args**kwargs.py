def myfunc(a,b):
    return (sum(a,b)) * 0.05
def myfunc(a,b,c=0,d=0,e=0):
    return (sum(a,b,c,d,e)) * 0.05
def myfunc(*args):
    return(sum(args)) * 0.05
    print(args)
    for item in args:
        print(item)
def myfunc(**kwargs):
    print(kwargs)
    if 'fruit' in kwargs:
        print('My fruit of choice is {}'.format(kwargs['fruit']))
    else:
        print("I don't find any fruit here")
def myfunc(*args,**kwargs):
    print(args)
    print(kwargs)
    print('I would like {} {}'.format(args[0],kwargs['food']))
