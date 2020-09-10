from pyspark.ml.feature import PCA

pca = PCA(k=3, inputCol="features", outputCol="pcaFeatures")
pca_model = pca.fit(df)