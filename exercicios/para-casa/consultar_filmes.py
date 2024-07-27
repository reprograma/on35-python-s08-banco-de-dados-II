import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# # Seleciona todos os registros da tabela "filmes"
cursor.execute("SELECT * FROM filmes")
registros = cursor.fetchall()

# # Imprime os registros
for registro in registros:
     print(registro)

# # Fecha a conexão
cursor.close()
conn.close()

#consulta do exercicio da sala
# * **`cursor.execute("SELECT * FROM estudantes")`**: Executa a consulta SQL para selecionar todos os registros da tabela "estudantes".
# * **`registros = cursor.fetchall()`**: Recupera todos os registros da consulta em uma lista de tuplas.
# * **`for registro in registros:`**: Itera sobre os registros e imprime cada um deles.