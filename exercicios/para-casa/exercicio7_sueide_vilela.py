#Exporte os Dados para um Novo CSV

import sqlite3
import csv

conn = sqlite3.conect('videoteca.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM filmes')

filmes = cursor.fetchall()

nome_arquivo_csv = 'exportados_filmes.csv'

with open(nome_arquivo_csv, 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)

    escritor.writerow(['id', 'titulo', 'diretor', 'ano', 'genero', 'preco'])

    escritor.writerows(filmes)