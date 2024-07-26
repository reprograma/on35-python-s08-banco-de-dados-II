import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Removendo o filme com id 3
cursor.execute('DELETE FROM filmes WHERE id = 3')

# Confirmando as alterações
conn.commit()
conn.close()