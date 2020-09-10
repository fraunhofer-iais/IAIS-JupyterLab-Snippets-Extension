# Register the dataframe as temp table
df.createOrReplaceTempView("temp_table")
# Use the SQL interface from SparkSession
new_df= spark.sql("""
            select temp_table.*
            from temp_table
            """)
# Persist result to memory and disk
new_df = new_df.persist(pyspark.StorageLevel.MEMORY_AND_DISK)
