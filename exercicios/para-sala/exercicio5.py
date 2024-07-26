import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Remove o estudante Charlie
cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Charlie',))

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()