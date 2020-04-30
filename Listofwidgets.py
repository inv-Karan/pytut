import ipywidgets as widgets

# Show all available widgets!

for item in widgets.Widget.widget_types.items():
    print(item[0])