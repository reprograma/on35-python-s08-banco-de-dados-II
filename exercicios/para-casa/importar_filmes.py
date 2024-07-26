import csv
import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

with open('filmes.csv', 'r') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    
    next(leitor_csv)
    
    for linha in leitor_csv:
        cursor.execute("INSERT INTO filmes (titulo, diretor, ano, genero, preco) VALUES (?, ?, ?, ?, ?)", (linha[0], linha[1], linha[2], linha[3], linha[4]))

conn.commit()

cursor.close()
conn.close()