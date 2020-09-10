# Stop Spark Session named 'spark'
if 'spark' in globals():
    spark.stop()

# Stop Spark Context named 'sc'
if 'sc' in globals():
    sc.stop()