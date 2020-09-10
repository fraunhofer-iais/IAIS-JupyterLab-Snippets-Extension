from pyspark.ml.feature import PolynomialExpansion

poly_expansion = PolynomialExpansion(degree=3, inputCol="features", outputCol="polyFeatures")
poly_df = poly_expansion.transform(df)