import sqlite3

conn = sqlite3.connect('/data/meubanco.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM usuarios')
for row in cursor.fetchall():
    print(row)

conn.close()