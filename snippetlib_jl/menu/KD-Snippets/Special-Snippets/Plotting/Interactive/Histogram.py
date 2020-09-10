# Quickly plot a beautiful interactive histogram

def histogram(data, attribute, bins, logscale):
    histData = data[attribute].dropna(axis=0)

    fig, ax = plt.subplots(figsize=(8,5))
    a = ax.hist(histData.values, color='k', bins=bins, alpha=0.2, histtype='stepfilled', label=attribute) 

    # beautyfy the plot
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    #plt.setp(pl.xticks()[1], rotation=-30)
    ax.set_xlabel(attribute, fontsize=12)
    ax.set_ylabel("Count", fontsize=12)
    if logscale == True:
        ax.set_yscale('log', nonposy='clip')
    plt.legend(loc=1)
    plt.tight_layout()

i = interact(histogram, data=fixed(data), attribute=data.columns, bins=(5, 20), logscale=False);