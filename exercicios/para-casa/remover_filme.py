import sqlite3
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM filmes WHERE titulo = ?", ( "A Origem", ))

conn.commit()
cursor.close()
conn.close()