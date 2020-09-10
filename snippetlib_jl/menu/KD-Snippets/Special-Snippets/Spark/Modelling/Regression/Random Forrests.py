# Regression with Random Forrests
from pyspark.ml.regression import RandomForestRegressor, RandomForestRegressorModel

random_forrest = RandomForestRegressor(maxDepth=5, numTrees=1000, minInstancesPerNode=5)
random_forrest_model = random_forrest.fit(df)