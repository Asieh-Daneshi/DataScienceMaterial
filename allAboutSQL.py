import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
# =============================================================================
# conn = sqlite3.connect('chinook.db')    # no matter if we want to work with pandas or pure python, we need a connection for sql databases. So, this step is always the same
# cur = conn.cursor()     # after connection, we need a cursor to execute sql
# # we can use "db browser" software to see the tables inside our SQL database
# # here we have these tables: "albums", "artists", "customers", "employees", 
# # I am going to open "employees" database
# cur.execute('SELECT * FROM employees LIMIT 3;')     # there are 8 rows in "employees", if we set the limit higher than 8, it just shows all the 8 elementts that it has
# results = cur.fetchall()        # we have to fetch to see the results of SQL
# using pandas ----------------------------------------------------------------
conn = sqlite3.connect('chinook.db')
df1 = pd.read_sql('SELECT * FROM employees;', conn)
df1.head

df2 = pd.read_sql('SELECT * FROM employees', conn, index_col='EmployeeId', parse_dates=['BirthDate', 'HireDate'])
df2.head    # with "index_col" we select one of the columns as index. With "parse_dates" we convert the date format into "parse" format. However, here the dates were substantially parse

# read_sql returns both tables and quieries. However, there are specific commands to focus just on tables or queries
# let's start with queries
conn = sqlite3.connect('chinook.db')
df = pd.read_sql_query('SELECT *FROM employees LIMIT 5;', conn)

# the same goes for tables, but I will stick to the original read_sql method
# now, how do we handle writing SQL databases?

df.to_sql
