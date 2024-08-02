import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Seleciona todos os registros da tabela "estudantes"
cursor.execute("SELECT * FROM filmes")
registros = cursor.fetchall()

# Imprime os registros
for registro in registros:
    print(registro)

# Fecha a conexão
cursor.close()
conn.close()