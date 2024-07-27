import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

novo_preco = 32.99
cursor.execute('UPDATE filmes SET preco = ? WHERE id = ?', (novo_preco, 2))

conn.commit()
conn.close()
