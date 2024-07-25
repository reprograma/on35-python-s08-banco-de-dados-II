import sqlite3
import csv
import tabulate

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM filmes')
dados = cursor.fetchall()

headers = ['id', 'titulo', 'diretor', 'ano', 'genero', 'preco']

with open('exportados_filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(headers)
    escritor.writerows(dados)

cursor.close()
conn. close()
