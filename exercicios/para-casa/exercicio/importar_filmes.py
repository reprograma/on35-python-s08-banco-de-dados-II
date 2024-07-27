import sqlite3
import csv

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

with open('filmes.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        cursor.execute('''
        INSERT INTO filmes (titulo, diretor, ano, genero, preco) 
        VALUES (?, ?, ?, ?, ?)
        ''', (row['titulo'], row['diretor'], row['ano'], row['genero'], row['preco']))

conn.commit()
conn.close()


import sqlite3
import csv
import os


csv_filename = 'filmes.csv'


if not os.path.exists(csv_filename):
    print(f"Erro: O arquivo {csv_filename} não foi encontrado.")
else:
    
    conn = sqlite3.connect('videoteca.db')
    cursor = conn.cursor()

    
    with open(csv_filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            cursor.execute('''
            INSERT INTO filmes (titulo, diretor, ano, genero, preco) 
            VALUES (?, ?, ?, ?, ?)
            ''', (row['titulo'], row['diretor'], row['ano'], row['genero'], row['preco']))


    conn.commit()
    conn.close()
    print("Dados importados com sucesso.")
