# Regression with Decision Trees
from pyspark.ml.regression import DecisionTreeRegressor, DecisionTreeRegressorModel

decision_tree = DecisionTreeRegressor(maxDepth=5, minInstancesPerNode=5)
decision_tree_model = decision_tree.fit(df)