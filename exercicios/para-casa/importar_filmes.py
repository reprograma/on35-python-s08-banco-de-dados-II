# **3. Importe os Dados para o Banco de Dados:**

# * Escreva um script Python (chamado `importar_filmes.py`) que leia os dados do `filmes.csv` e os insira na tabela `filmes` no banco de dados `videoteca.db`.

import sqlite3
import csv

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

with open('filmes.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  # Pular cabeçalho
    for linha in leitor:
        cursor.execute("INSERT INTO filmes (titulo, diretor, ano, genero, preco) VALUES (?, ?, ?, ?, ?)",
                       (linha[0], linha[1], linha[2], linha[3], linha[4]))

conn.commit()
cursor.close()
conn.close()
