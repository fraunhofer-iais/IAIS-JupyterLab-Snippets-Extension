# Interactive colored XY-plot 

def scatter(data, x, y, color):
    myColor='k'
    if data[color].dtype == object:
        d = data[color]
        uniques = d.unique()
        mapping = dict(zip(uniques, np.arange(len(uniques), dtype=float)))
        myColor = plt.cm.RdYlGn(minmax_scale([mapping[i] for i in d]))
    else:
        myColor = plt.cm.RdYlGn(minmax_scale(data[color].values))
    fig, ax = plt.subplots(figsize=(8, 5))
    scatter = ax.scatter(data[x], data[y], color='k', facecolor=myColor, s=50, alpha=0.5)
    ax.set_xlabel(x, fontsize=12)
    ax.set_ylabel(y, fontsize=12)
    plt.tight_layout()
    
i = interact(scatter, data=fixed(data), x=data.columns, y=data.columns, color=data.columns);