# Tuning of Models
import numpy as np
from pyspark.ml.tuning import CrossValidator, ParamGridBuilder
from pyspark.ml.evaluation import BinaryClassificationEvaluator, MulticlassClassificationEvaluator, RegressionEvaluator

(df_train, df_test) = df.randomSplit([0.7, 0.3])

# Example for generic ML model, check parameter
paramGrid = ParamGridBuilder() \
    .addGrid(ml_model.regParam, np.logspace(-3,0,4)) \
    .addGrid(ml_model.elasticNetParam, np.logspace(-3,0,4)) \
    .build()

crossval = CrossValidator(estimator=ml_model,
                          estimatorParamMaps=paramGrid,
                          evaluator=BinaryClassificationEvaluator(metricName='f1'), # accuracy, precision, recall
                          # evaluator=MulticlassClassificationEvaluator(metricName='f1'), # accuracy, precision, recall
                          # evaluator=RegressionEvaluator(metricName='r2'), # mse
                          numFolds=3)  # use 3+ folds in practice

# Run cross-validation, and choose the best set of parameters.
cv_model = crossval.fit(df_train)

final_model = cv_model.bestModel