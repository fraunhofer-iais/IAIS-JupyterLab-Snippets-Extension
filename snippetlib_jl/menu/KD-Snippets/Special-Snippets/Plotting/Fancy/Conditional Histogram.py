# a histogram of an attribute, constrained on the values of another attribute


def conditionalHistogram(data, attribute, given, condition, value, bins, logscale):
    histData = data[attribute].dropna(axis=0)
    bins = np.histogram(histData, bins=bins)[1]

    fig, ax = plt.subplots(figsize=(8,5))
    a = ax.hist(histData.values, color='k', bins=bins, alpha=0.2, histtype='stepfilled', label=attribute) 
    try:
        try:
            selection = "data['%s'][data['%s'] %s %s]" %(attribute, given, condition, str(value))
            condData = eval(selection)
            g = ax.hist(condData.values, color='steelblue', alpha=0.5, bins=bins, histtype='stepfilled', label='given %s'%given)
        except:
            selection = "data['%s'][data['%s'] %s '%s']" %(attribute, given, condition, str(value))
            condData = eval(selection)
            g = ax.hist(condData.values, color='steelblue', alpha=0.5, bins=bins, histtype='stepfilled', label='given %s'%given)
    except:
        pass

    # beautyfy the plot
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    #plt.setp(pl.xticks()[1], rotation=-30)
    ax.set_xlabel("%s|(%s %s %s)" %(attribute, given, condition, str(value)), fontsize=12)
    ax.set_ylabel("Count", fontsize=12)
    if logscale == True:
        ax.set_yscale('log', nonposy='clip')
    plt.legend(loc=1)
    plt.tight_layout()

i = interact(conditionalHistogram, data=fixed(data), attribute=data.columns, given=data.columns, condition=['<', '>', '=='], value=(0.,10.), bins=(5, 25), logscale=False);
#i = interact(conditionalHistogram, attribute=data.columns, given=data.columns, condition=['!=', '=='], value=data.label.unique()) bins=(5, 25), logscale=False);