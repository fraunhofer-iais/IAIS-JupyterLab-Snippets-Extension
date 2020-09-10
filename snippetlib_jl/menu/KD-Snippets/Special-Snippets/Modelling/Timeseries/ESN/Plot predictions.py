fig = pl.figure()
num_plots = len(predictions)
for i, prediction_channel in enumerate(predictions):
    fig.add_subplot("%d1%d" %(num_plots, i+1))
    ax = pl.gca()
    if len(y.T.shape) == 1:
        ax.plot(y, color='y', linewidth=2)
    else:
        ax.plot(y.T[i], color='y', linewidth=2)
    ax.plot(prediction_channel, color='k')