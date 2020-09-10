lag = 1

X = data.values[:-lag]
y = data[['X2','Y2']].values[lag:]

inSize         = 4
resSize        = 200
outSize        = 2

relearnEvery   = 100
memory         = 1000

leaking_rate   = 0.5
regularization = 1.0

esn = multi_value_ESN(inSize, outSize, resSize, relearnEvery=relearnEvery, memory=memory, leaking_rate=leaking_rate, regularization=regularization)
predictions = []

for i in range(len(X)):
    predictions.append(esn.feed(X[i], y[i]))
predictions = np.array(predictions).T