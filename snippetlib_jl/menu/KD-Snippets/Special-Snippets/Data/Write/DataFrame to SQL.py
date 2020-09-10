# Save data into an SQL database

con = sqlite3.connect("data.sqlite")
vehicle_info.to_sql(con=con, name='table_name', flavor='sqlite', index=True)