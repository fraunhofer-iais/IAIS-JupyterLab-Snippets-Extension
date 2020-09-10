# Takes 'features_list' as input and transforms the selected columns to a new column named 'features'
# which contains a vector of the selected columns
from pyspark.ml.feature import VectorAssembler

feature_list = [col for col in df.columns if col != 'label']

vecAssembler = VectorAssembler(inputCols=feature_list, outputCol="features")
df_vec = vecAssembler.transform(df)