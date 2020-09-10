# Barplot of the mean values, given an attribute value

def bars(data, groupby_attribute):
    errors = data.groupby(groupby_attribute).std()
    data.groupby(groupby_attribute).mean().plot(kind='bar', figsize=(8,5), yerr=errors, colormap=plt.cm.Blues)



i = interact(bars, data=fixed(data), groupby_attribute=data.columns[data.dtypes == object]);