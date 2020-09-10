attribute = 'mag'

data[attribute].groupby([data.index.hour]).count().plot(title="Activities for each hour of the day", color='k')
pl.show()

data[attribute].groupby([data.index.day]).count().plot(title="Activities for each day of the month", color='k')
pl.show()