import ipywidgets as widgets
from IPython.display import display

w=widgets.IntSlider()
display(w)

w.layout.margin='auto'
w.layout.height='75px'

x=widgets.IntSlider(value=15,description='New Slider')
display(x)

x.layout=w.layout
widgets.Button(description='Ordinary Button',button_style='danger')
widgets.Button(description='Ordinary Button',button_style='warning')
widgets.Button(description='Ordinary Button',button_style='info')

b1=widgets.Button(description='Custom Color')
b1.style.button_color='lightgreen'
b1.style.keys
b2=widgets.Button()
b2.style=b1.style

s1=widgets.IntSlider(description='My Handle')
s1.stle.handle_color='black'
s1.stle.handle_color='lightblue'