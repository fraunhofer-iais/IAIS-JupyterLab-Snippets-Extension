# Read CSV with colum separator ',' and try to guess the Types of the columns (needs to read data twice)
# and assumes the first row to be a header
df = spark.read.csv('path/to/data.csv', sep=',', inferSchema=True, header=True)