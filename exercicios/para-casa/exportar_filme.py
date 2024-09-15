import csv
import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('SELECT titulo, diretor, ano, genero, preco FROM filmes')
filmes = cursor.fetchall()

with open('exportados_filmes.csv', mode='w', newline='', encoding='UTF-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['titulo', 'diretor', 'ano', 'genero', 'preco']) 
    escritor.writerows(filmes)

print("Dados exportados com sucesso para 'exportados_filmes.csv'.")

conn.close()