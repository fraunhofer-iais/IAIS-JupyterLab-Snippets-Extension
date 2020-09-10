# Reads a parquet file from path
df = spark.read.format("parquet").load("hdfs://localhost:54310/path/to/data.parquet")