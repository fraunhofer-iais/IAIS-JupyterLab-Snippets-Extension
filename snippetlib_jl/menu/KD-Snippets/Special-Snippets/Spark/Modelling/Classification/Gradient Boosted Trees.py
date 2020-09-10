from pyspark.ml.classification import GBTClassifier, GBTClassifierModel

gbt = GBTClassifier(maxDepth=5, minInstancesPerNode=5)
gbt_model = gbt.fit(df)