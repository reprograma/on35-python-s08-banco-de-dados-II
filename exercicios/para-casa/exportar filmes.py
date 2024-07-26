## Exercício de Casa 🏠 Gerenciando uma Videoteca com SQLite e CSV
#7-Exporte os dados para um novo CSV:

import sqlite3
import csv

# Conectar ao banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Executar consulta
cursor.execute("SELECT titulo, diretor, ano, genero, preco FROM filmes")
dados = cursor.fetchall()

# Escrever os dados no arquivo CSV
with open('exportados_filmes.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['titulo', 'diretor', 'ano', 'genero', 'preco'])  # Cabeçalhos
    writer.writerows(dados)

# Fechar a conexão
cursor.close()
conn.close()

print("Dados exportados com sucesso para 'exportados_filmes.csv'!")

