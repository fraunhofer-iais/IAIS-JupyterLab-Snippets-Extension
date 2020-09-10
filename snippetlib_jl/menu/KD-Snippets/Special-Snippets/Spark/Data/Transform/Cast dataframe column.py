# Create a new column from old column with new data type
df_cast = df.withColumn('new_column', df['old_column'].cast('new_type'))