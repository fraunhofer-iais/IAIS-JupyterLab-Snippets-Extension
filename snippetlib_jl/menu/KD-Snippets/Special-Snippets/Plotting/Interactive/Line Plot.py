# make a line-plot of a selected attribute

def scatter(data, attribute):
    fig, ax = plt.subplots(figsize=(8, 4))
    line = ax.plot(data[attribute], color='k')
    ax.set_xlabel(attribute, fontsize=12)
    ax.set_ylabel('Value', fontsize=12)
    plt.tight_layout()

i = interact(scatter, data=fixed(data), attribute=data.columns);