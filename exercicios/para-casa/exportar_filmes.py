import sqlite3
import csv

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM filmes')
filmes = cursor.fetchall()

with open('exportados_filmes.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['id', 'titulo', 'diretor', 'ano', 'genero', 'preco'])
    writer.writerows(filmes)

print("Dados exportados para exportados_filmes.csv com sucesso!")