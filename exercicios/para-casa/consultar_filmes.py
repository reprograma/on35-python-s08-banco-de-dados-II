import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM filmes")
registros = cursor.fetchall()

for registro in registros:
    print(registro)

cursor.close()
conn.close()