# Create multiplicative relations between the features to a polynomial degree of 2
from sklearn import preprocessing as pp

degree = 2
poly = pp.PolynomialFeatures(degree)
names = poly.get_feature_names(attributes)

X_train_p = poly.fit_transform(X_train)
X_test_p  = poly.fit_transform(X_test)