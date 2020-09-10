# Discretize all continuous numeric data 

ddata = data.copy()
num_bins = 10

# ... into bins of equal size
#ddata[ddata._get_numeric_data().columns] = ddata._get_numeric_data().apply(lambda x: list(pd.qcut(x, num_bins)), axis=0)
# single attribute
#ddata['ATTRIBUTE'] = ddata[['ATTRIBUTE']].apply(lambda x: list(pd.qcut(x, num_bins)), axis=0)

# ... into bins of equal width
ddata[ddata._get_numeric_data().columns] = ddata._get_numeric_data().apply(lambda x: list(pd.cut(x, num_bins)), axis=0)
# single attribute
#ddata['ATTRIBUTE'] = ddata[['ATTRIBUTE']].apply(lambda x: list(pd.cut(x, num_bins)), axis=0)

ddata.head()