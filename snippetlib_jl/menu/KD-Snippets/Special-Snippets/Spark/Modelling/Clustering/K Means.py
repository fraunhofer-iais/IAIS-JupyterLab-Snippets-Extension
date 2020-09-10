# K-Means Clustering
from pyspark.ml.clustering import KMeans, KMeansModel

k_means = KMeans(k=3, maxIter=20)
k_means_model = k_means.fit(df.select('features'))