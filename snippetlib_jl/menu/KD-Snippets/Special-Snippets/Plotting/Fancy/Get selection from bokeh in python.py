# create a scatterplot with lasso-selection.
# the indices of the selected points will be passed back to python into the variable ***selected_indices***

from bokeh.plotting import figure, show
from bokeh.models import ColumnDataSource
from bokeh.models import CustomJS
from bokeh.io import output_notebook
output_notebook()

source = ColumnDataSource(data)
source.callback = CustomJS(args=dict(source=source), code="""
        var inds = cb_obj.selected['1d'].indices;
        var kernel = IPython.notebook.kernel;
        kernel.execute('selected_indices = [' + inds + ']');
        """)

fig = figure(tools='wheel_zoom,lasso_select,reset', plot_width=400, plot_height=400)
fig.scatter('sepal_length', 'sepal_width', source=source)
show(fig)