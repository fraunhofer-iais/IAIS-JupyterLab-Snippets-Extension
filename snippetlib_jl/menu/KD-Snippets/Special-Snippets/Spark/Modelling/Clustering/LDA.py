from pyspark.ml.clustering import LDA

# Trains a LDA model.
lda = LDA(k=10, maxIter=10)
lda_model = lda.fit(df)

# Shows the result
lda_df = model.transform(df)