import scipy.linalg
from sklearn import linear_model

class multi_value_ESN():
    def __init__(self, inSize, outSize, resSize, relearnEvery=100, memory=1000, leaking_rate=0.3, regularization=0.1):
        self.counter        = 0                                         # Keep track of the passed timesteps
        self.inSize         = inSize                                    # Number of input neurons
        self.outSize        = outSize                                   # Number of output neurons
        self.resSize        = resSize                                   # Number of neurons in dynamic reservoir
        self.memory         = memory                                    # Number of past activation states to consider for learning the output
        self.relearnEvery   = relearnEvery                              # Re-train the model every x timesteps
        self.regularization = regularization                            # Regularization of the final ridge regression
        self.x              = np.zeros((self.resSize, 1))               # Current input value(s)
        self.X              = np.zeros((self.memory, 1 + self.resSize)) # Matrix of the collected past states
        self.y              = np.zeros((self.memory, self.outSize))     # The value that is to predict
        self.a              = leaking_rate                              # Fraction of the neurons activation that does not leak into the next timestep
        self.Win            = (np.random.rand(resSize, inSize)-0.5) * 1 # Weights that connect the input with the dynamic reservoir
        self.Wout           = np.zeros((self.outSize, self.resSize+1))  # Weights that connect the dynamic reservoir with the output... THIS IS WHAT IS LEARNED!
        
        # generate the ESN reservoir
        self.W = np.random.rand(self.resSize, self.resSize) - 0.5 
        
        # sparsify the reservoir
        self.W[abs(self.W) <= 0.25] = 0.0
        
        # cap the reservoir, to remedy resonance
        rhoW = max(abs(np.linalg.eig(self.W)[0]))
        self.W *= 1.25 / rhoW


    def feed(self, data, label):
        """Feed data and get predictions. The model is retrained every once in a while to cope with concept drift."""
        self.counter += 1

        # get the activity of the reservoir
        self.x = (1 - self.a)*self.x + self.a*np.tanh(np.dot(self.Win, data) + np.dot(self.W, self.x).T).T
        self.x[-1] = 0.5 # This is the intercept
        
        # update states matrix
        self.X[self.counter % self.memory] = np.hstack((1., self.x.T[0]))
        # update the labels
        self.y[self.counter % self.memory] = label

        # relearn the output weights from time to time
        if self.counter % self.relearnEvery == 0:
            self.Wout = np.dot(np.dot(self.y.T, self.X), np.linalg.inv(np.dot(self.X.T, self.X) + self.regularization*np.eye(len(self.X.T))))
                
        return np.dot(self.Wout, np.vstack((1., self.x))).T[0]
