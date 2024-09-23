# Exercício 3 >> Importe os Dados para o Banco de Dados:
# Escreva um script Python (chamado `importar_filmes.py`) que leia os dados do `filmes.csv`
# e os insira na tabela `filmes` no banco de dados `videoteca.db`.

import sqlite3
import csv

# Conectando ao banco de dados 'videoteca.db'
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Abrindo o arquivo CSV e lendo os dados
with open('filmes.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    
    # Ignorando o cabeçalho (assumindo que a primeira linha é o cabeçalho)
    next(reader)

    # Inserindo os dados na tabela 'filmes'
    for row in reader:
        cursor.execute("""
            INSERT INTO filmes (titulo, diretor, ano, genero, preco)
            VALUES (?, ?, ?, ?, ?)""", 
            (row[0], row[1], int(row[2]), row[3], float(row[4]))
        )

# Salvando as alterações no banco de dados
conn.commit()

# Fechando a conexão
cursor.close()
conn.close()

print("Dados importados com sucesso!")
