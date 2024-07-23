import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM filmes WHERE titulo = ?", ('Um Tira da Pesada 4: Axel Foley',))

conn.commit()

cursor.close()
conn.close()