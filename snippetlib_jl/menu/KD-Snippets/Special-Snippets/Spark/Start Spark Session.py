# Start a Spark Context and a Spark Session
try:               
    import pyspark
except:       
    import findspark                                                    
    findspark.init()                   
    import pyspark
from pyspark.sql import SparkSession
from pyspark.sql import functions as F
               
# Create Spark Context
sc = pyspark.SparkContext(appName='Spark Context Name')
                         
# Create Spark Session
spark = SparkSession.builder \
        .appName('Spark Session Name') \
        .config('spark.executor.memory','5g') \
        .config('spark.executor.cores','4') \
        .getOrCreate()
