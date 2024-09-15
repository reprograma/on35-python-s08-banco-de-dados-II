#Importar os Dados para o Banco de Dados

import csv
import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

with open('filmes.csv', newline='', encoding='UTF-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  
    
    for linha in leitor:
        titulo, diretor, ano, genero, preco = linha
        cursor.execute('''
            INSERT INTO filmes (titulo, diretor, ano, genero, preco)
            VALUES (?, ?, ?, ?, ?)
        ''', (titulo, diretor, int(ano), genero, float(preco)))

conn.commit()
print("Dados importados com sucesso para a tabela 'filmes'.")

conn.close()