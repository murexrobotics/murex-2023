import cgi
import sqlite3

cgitb.enable()

form = cg.FieldStorage()
data = form.getvalue('test-form')

conn = sqlite3.connect('sample.db')
conn.execute("INSERT INTO test_table [test_column] VALUES (data)")
conn.commit()
conn.close()