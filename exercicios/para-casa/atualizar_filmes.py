import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

filme_id = 2

novo_preco = 15.99

cursor.execute('UPDATE filmes SET preco = ? WHERE id = ?', (novo_preco, filme_id))

conn.commit()
conn.close()

print(f"Preço do filme com ID {filme_id} atualizado para R${novo_preco:.2f}")
