import ipywidgets as widgets
widgets.IntSlider()

w=widgets.IntSlider()

from IPython.display import display
display(w)

w.close()

w.value
w.keys
w.max

a=widgets.FloatText()
b=widgets.FloatSlider()
display(a,b)

mylink=widgets.jslink((a,'value'),(b,'value'))
mylink=widgets.jslink((a,'value'),(b,'max'))

mylink.unlink()