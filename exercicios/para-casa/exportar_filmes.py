#Exportando de SQlite para CSV
import sqlite3
import csv

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM filmes")
filmes = cursor.fetchall()

with open ('exportados_filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['titulo', 'diretor', 'ano', 'genero', 'preco' ])
    escritor.writerows(filmes)

cursor.close()
conn.close()