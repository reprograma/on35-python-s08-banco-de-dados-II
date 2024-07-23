import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute("UPDATE filmes SET preco = ? WHERE titulo = ?", (25.40, 'Em Trânsito'))

conn.commit()
cursor.close()
conn.close()