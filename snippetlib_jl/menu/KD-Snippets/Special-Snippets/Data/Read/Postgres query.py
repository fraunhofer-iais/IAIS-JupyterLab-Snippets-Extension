# Query Postgres database into a Pandas dataframe




"""
MIT,https://datatofish.com/sql-to-pandas-dataframe/

"""

import pyodbc
import pandas as pd

conn = pyodbc.connect(r'Driver={};DBQ=;')

SQL_Query = pd.read_sql_query(
'''select
product_name,
product_price_per_unit,
units_ordered,
((units_ordered) * (product_price_per_unit)) AS revenue
from tracking_sales''', conn)

df = pd.DataFrame(SQL_Query, columns=['product_name','product_price_per_unit','units_ordered','revenue'])
print (df)

