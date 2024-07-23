import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute("UPDATE filmes SET ano = ? WHERE titulo = ?", (2023, 'Pulp Fiction'))

conn.commit()

cursor.close()
conn.close()