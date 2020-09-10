### Query SQLite database into a Pandas dataframe

con = sqlite3.connect("data.sqlite")
query = "SELECT * FROM table"
data = pd.read_sql_query(query, con)