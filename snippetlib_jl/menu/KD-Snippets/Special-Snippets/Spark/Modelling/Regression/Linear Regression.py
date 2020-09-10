# Linear Regression
from pyspark.ml.regression import LinearRegression, LinearRegressionModel

# Linear Regression
linear_regression = LinearRegression(maxIter=100, regParam=0.0, elasticNetParam=0.0)
linear_regression_model = linear_regression.fit(df)