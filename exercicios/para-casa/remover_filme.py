import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute("DELETE FROM filmes WHERE titulo = ?", ('Cléo de 5 às 7',))

conn.commit()
cursor.close()
conn.close()