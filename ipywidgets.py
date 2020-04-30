from ipywidgets import interact,interactive,fixed
import ipywidgets as widgets

def func(x):
    return x

interact(func,x=10)

def func(x):
    return x**2

interact(func,x=10)

def func(x):
    return x

interact(func,x='Hello')
interact(func,x=fixed('Hello'))

@interact(x=True,y=1.0)
def g(x,y):
    return (x,y)

@interact(x=True,y=fixed(1.0))
def g(x,y):
    return (x,y)

interact(func,x=1)

interact(func,x=widgets.IntSlider(min=-100,max=100,step=1,value=0))

interact(func,x=(-10,10,1))

interact(func,x=(-10.0,10.0,0.1))

@interact(x=(0.0,20.0,0.5))
def h(x=5.0):
    return x

interact(func,x=['hello','option 2','option 3'])

interact(func,x={'one':10,'two':20})

#####################################################################

from IPython.display import display

def f(a,b):
    display(a+b)
    return a+b

w = interactive(f,a=10,b=20)

type(w)

w.children

display(w)

