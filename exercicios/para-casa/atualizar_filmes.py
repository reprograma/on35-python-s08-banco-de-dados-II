import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('UPDATE filmes SET preco = ? WHERE id = ?', (37.99, 2))


conn.commit()

cursor.close()
conn.close()
