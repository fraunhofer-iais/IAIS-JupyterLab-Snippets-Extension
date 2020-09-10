# Check out the list of widgets here:
# http://ipywidgets.readthedocs.io/en/latest/examples/Widget%20List.html
from ipywidgets import ToggleButton, IntRangeSlider, IntSlider, Dropdown, Text, Tab, HBox, VBox, interactive_output
from IPython.display import display

# Any plotting Function
def interactive_hist(data, column, datarange, color, bins, title):
    c = 'b'
    if color:
        c = 'r'
    fig, ax = plt.subplots(figsize=(7,3))
    i0 = int((datarange[0]/100)*len(data))
    i1 = int((datarange[1]/100)*len(data))
    ax.hist(data[column].iloc[i0:i1], bins=bins, color=c)
    ax.set_title(title)
    plt.show()


# User Interface
dropdown    = Dropdown(value=data.columns[0], options=data.columns, description='Column')

rangeslider = IntRangeSlider(description='Rows %%', continuous_update=False, min=0, max=100)
bins        = IntSlider(description='Bins', continuous_update=False, min=10, max=50)
box1        = HBox([rangeslider, bins])

button      = ToggleButton(value=False, description='Toggle color', icon='check')
text        = Text(value='', placeholder='Title', description='String:')
box2        = HBox([text, button])

ui = Tab(children = [dropdown, box1, box2])
ui.set_title(0, 'Select Attribute')
ui.set_title(1, 'Select Data Range')
ui.set_title(2, 'Sytling')


# Bringing UI and plot together
plot = interactive_output(interactive_hist, {'data':fixed(data), 
                                             'column':dropdown, 
                                             'datarange':rangeslider, 
                                             'color':button, 
                                             'bins':bins, 
                                             'title':text});

display(ui, plot)