import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM filmes')
for linha in cursor.fetchall():
    print(linha)

conn.commit()

cursor.close()
conn.close()
