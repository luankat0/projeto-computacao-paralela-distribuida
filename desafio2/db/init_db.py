import sqlite3

conn = sqlite3.connect('/data/meubanco.db')
cursor = conn.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS usuarios (id INTEGER PRIMARY KEY, nome TEXT)')
cursor.execute("INSERT INTO usuarios (nome) VALUES ('Alice'), ('Bob'), ('Carol')")
conn.commit()

print("Banco criado e dados inseridos com sucesso.")
conn.close()