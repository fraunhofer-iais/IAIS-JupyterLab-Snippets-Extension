# two scatterplots with a linked selection

from ipywidgets import interact_manual
from bokeh.plotting import figure, show
from bokeh.layouts import gridplot
from bokeh.models import ColumnDataSource
from bokeh.io import output_notebook
from bokeh.resources import INLINE
output_notebook(resources=INLINE)


def double_scatter(data, x1, y1, x2, y2):
    source = ColumnDataSource(data)
    TOOLS = "pan, wheel_zoom, lasso_select, reset"

    left = figure(tools=TOOLS, plot_width=300, plot_height=300, title=None)
    left.circle(x1, y1, source=source)
    left.xaxis.axis_label = x1.replace('_', ' ').capitalize()
    left.yaxis.axis_label = y1.replace('_', ' ').capitalize()

    right = figure(tools=TOOLS, plot_width=300, plot_height=300, title=None)
    right.circle(x2, y2, source=source)
    right.xaxis.axis_label = x2.replace('_', ' ').capitalize()
    right.yaxis.axis_label = y2.replace('_', ' ').capitalize()

    p = gridplot([[left, right]])
    show(p)

attrs = data.columns.tolist()
interact_manual(double_scatter, data=fixed(data), x1=attrs, y1=attrs, x2=attrs, y2=attrs);