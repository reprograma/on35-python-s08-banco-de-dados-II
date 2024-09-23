# Exercicio 4 >>  Consulte e Exiba os Dados:
#Escreva um script Python (chamado consultar_filmes.py) que selecione e exiba todos os registros da tabela filmes.

import sqlite3

# Conectando ao banco de dados 'videoteca.db'
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Executando a consulta para selecionar todos os registros da tabela 'filmes'
cursor.execute("SELECT * FROM filmes")

# Recuperando todos os resultados da consulta
filmes = cursor.fetchall()

# Exibindo os resultados
print("Lista de Filmes na Videoteca:")
print("-" * 50)
for filme in filmes:
    print(f"ID: {filme[0]}")
    print(f"Título: {filme[1]}")
    print(f"Diretor: {filme[2]}")
    print(f"Ano: {filme[3]}")
    print(f"Gênero: {filme[4]}")
    print(f"Preço: R$ {filme[5]:.2f}")
    print("-" * 50)

# Fechando a conexão
cursor.close()
conn.close()
  