from pyspark.ml.feature import StandardScaler

scaler = StandardScaler(inputCol="features", outputCol="scaledFeatures",
                        withStd=True, withMean=False)

# Compute summary statistics by fitting the StandardScaler
scaler_model = scaler.fit(df)

# Normalize each feature to have unit standard deviation.
scaled_df = scaler_model.transform(df)
