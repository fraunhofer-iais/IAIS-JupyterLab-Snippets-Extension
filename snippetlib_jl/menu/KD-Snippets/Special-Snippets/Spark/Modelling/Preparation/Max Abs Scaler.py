from pyspark.ml.feature import MaxAbsScaler

scaler = MaxAbsScaler(inputCol="features", outputCol="scaledFeatures")

# Compute summary statistics and generate MaxAbsScalerModel
scaler_model = scaler.fit(df)

# rescale each feature to range [-1, 1].
scaled_df = scaler_model.transform(df)