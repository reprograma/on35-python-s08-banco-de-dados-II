# Exercício de Casa 🏠 Gerenciando uma Videoteca com SQLite e CSV
# 3-Importar os Dados para o Banco de Dados
import sqlite3
import csv

# Conectar ao banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Ler os dados do arquivo CSV
with open('filmes.csv', 'r', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    filmes = [
    (row['titulo'], row['diretor'], int(row['ano']), row['genero'], float(row['preco']))
    for row in reader
    ]

# Inserir os dados na tabela
cursor.executemany('''
    INSERT INTO filmes (titulo, diretor, ano, genero, preco)
    VALUES (?, ?, ?, ?, ?)
''', filmes)

# Confirmar a transação
conn.commit()

# Fechar a conexão
cursor.close()
conn.close()

print("Dados importados com sucesso para a tabela 'filmes'!")
