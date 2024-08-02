import sqlite3
import csv

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM filmes")
dados = cursor.fetchall()

with open('exportados_filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['id','titulo', 'diretor', 'ano', 'genero', 'preco'])
    escritor.writerows(dados)

cursor.close()
conn.close()