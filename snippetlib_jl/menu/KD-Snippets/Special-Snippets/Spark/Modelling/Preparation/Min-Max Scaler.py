from pyspark.ml.feature import MinMaxScaler

scaler = MinMaxScaler(inputCol="features", outputCol="scaledFeatures")

# Compute summary statistics and generate MinMaxScalerModel
scaler_model = scaler.fit(df)

# rescale each feature to range [min, max].
scaled_df = scaler_model.transform(df)