import sqlite3
conn = sqlite3.connect('database.db')
print "database opened successfully"
conn.execute('CREATE TABLE users(username TEXT,password TEXT)')
print "table created successfully"
conn.close()