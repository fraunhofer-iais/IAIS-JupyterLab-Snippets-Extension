# To define a UDF you have to import the correct return type
from pyspark.sql.types import IntegerType
def my_func(inp):
    return int(inp) + 42
my_udf = F.udf(my_func, IntegerType())