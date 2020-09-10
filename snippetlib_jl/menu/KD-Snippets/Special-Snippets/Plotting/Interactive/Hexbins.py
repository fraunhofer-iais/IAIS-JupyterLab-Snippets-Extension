# Interactive Hexbin plot

def scatter(data, x, y, gridsize):
    fig, ax = plt.subplots(figsize=(5,5))
    scatter = ax.hexbin(data[x], data[y], cmap=plt.cm.Blues_r, gridsize=gridsize)
    ax.set_xlabel(x, fontsize=12)
    ax.set_ylabel(y, fontsize=12)
    plt.tight_layout()

i = interact(scatter, data=fixed(data), x=data.columns, y=data.columns, gridsize=(10,20));