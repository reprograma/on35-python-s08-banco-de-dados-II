import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('DELETE FROM filmes WHERE id = ?', (3,))

conn.commit()
conn.close()
