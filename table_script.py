import sqlite3

conn = sqlite3.connect('your_database.db')
c = conn.cursor()

c.execute('''
    CREATE TABLE IF NOT EXISTS answers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        timestamp REAL
    )
''')

conn.commit()
conn.close()
