from pyspark.ml.classification import LogisticRegression, LogisticRegressionModel

logistic_regression = LogisticRegression(maxIter=10, regParam=0.3, elasticNetParam=0.8, family='auto')
log_regression_model = logistic_regression.fit(df)