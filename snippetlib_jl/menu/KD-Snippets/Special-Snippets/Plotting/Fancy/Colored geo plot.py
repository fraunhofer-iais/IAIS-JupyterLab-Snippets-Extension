# plotting with a geographic map-tile provider requires web-mercator coordinates 

# instead of longitude and latitude
def lng_to_mercator(lng):
    return 6378137.0 * lng * 0.017453292519943295

def lat_to_mercator(lat):
    north = lat * 0.017453292519943295
    return 3189068.5 * np.log((1.0 + np.sin(north)) / (1.0 - np.sin(north)))
    
def geo_color_plot(data, color_by):
    source = ColumnDataSource(data)
    source.add(lng_to_mercator(data['longitude']), 'mercator_longitude')
    source.add(lat_to_mercator(data['latitude']), 'mercator_latitude')
    fig = figure(tools='pan,wheel_zoom,reset', plot_width=800, plot_height=450)
    fig.add_tile(get_provider('CARTODBPOSITRON'), alpha=1.0)
    hover = HoverTool(tooltips=list(zip(data.columns, ['@{%s}'%str(s) for s in data.columns])))
    fig.add_tools(hover)
    color_mapper = LinearColorMapper(palette=palettes.Viridis256, 
                                     low=data[color_by].min(), 
                                     high=data[color_by].max())
    fig.scatter(x='mercator_longitude', 
                y='mercator_latitude', 
                source=source, 
                size=5, 
                alpha=0.3,
                fill_color={'field': color_by, 'transform': color_mapper}, 
                line_color=None)
    fig.axis.visible = False
    show(fig)
    
i = interact(geo_color_plot, data=fixed(data), color_by=data._get_numeric_data().columns)