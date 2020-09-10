from pyspark.ml.clustering import GaussianMixture

gmm = GaussianMixture().setK(2).setSeed(538009335)
gmm_model = gmm.fit(df)

gmm_model.transform(df)