import sqlite3

con = sqlite3.connect('example.db')
cur = con.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, email TEXT) """)
cur.execute("""INSERT INTO users (id, name, age, email) VALUES (1, 'Shrimat Kapoor', 24, 'shrimatkapoor@gmail.com')""")
rows = cur.execute(""" SELECT * FROM users""").fetchall()
for row in rows:
    print(row)
con.commit()
con.close()