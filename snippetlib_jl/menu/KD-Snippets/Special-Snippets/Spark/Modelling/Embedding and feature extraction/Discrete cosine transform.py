from pyspark.ml.feature import DCT

dct = DCT(inverse=False, inputCol="features", outputCol="featuresDCT")
dct_df = dct.transform(df)