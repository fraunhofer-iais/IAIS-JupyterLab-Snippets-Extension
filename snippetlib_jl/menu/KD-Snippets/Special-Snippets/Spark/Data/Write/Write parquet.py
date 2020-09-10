# Writes dataframe to parquet file
df.write.format("parquet").save("hdfs://localhost:54310/path/to/data.parquet", mode='overwrite')
