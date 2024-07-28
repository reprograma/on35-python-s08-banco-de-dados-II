
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Atualiza o preço de um filme
cursor.execute("UPDATE filmes SET preco = ? WHERE id = ?", (37.99, 2))

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()