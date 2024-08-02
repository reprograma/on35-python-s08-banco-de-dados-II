import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()



# aumente o preço do filme com id 2
cursor.execute("UPDATE filmes SET preco = ? WHERE id = ?", (76.99, 2))

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()