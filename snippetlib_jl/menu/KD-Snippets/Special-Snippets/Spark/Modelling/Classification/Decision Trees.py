from pyspark.ml.classification import DecisionTreeClassifier, DecisionTreeClassifierModel

decision_tree = DecisionTreeClassifier(maxDepth=3, minInstancesPerNode=5, minInfoGain=0.01)
decision_tree_model = decision_tree.fit(df)
