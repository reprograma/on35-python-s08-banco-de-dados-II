import sqlite3
import csv

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

with open('filmes.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        titulo = row['titulo']
        diretor = row['diretor']
        ano = int(row['ano'])
        genero = row['genero']
        preco = float(row['preco'])

        cursor.execute('''
            INSERT INTO filmes (titulo, diretor, ano, genero, preco)
            VALUES (?, ?, ?, ?, ?)
        ''', (titulo, diretor, ano, genero, preco))

conn.commit()
conn.close()

print("Dados importados com sucesso!")
