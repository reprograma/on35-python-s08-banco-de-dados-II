import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Seleciona todos os registros da tabela "filmes"
cursor.execute("SELECT * FROM filmes")
filmes = cursor.fetchall()

# Imprime os registros
for filme in filmes:
    print(filmes)

# Fecha a conexão
cursor.close()
conn.close()