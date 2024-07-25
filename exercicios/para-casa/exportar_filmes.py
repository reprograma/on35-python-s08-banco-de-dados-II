#Exporte os Dados para um Novo CSV:

import sqlite3
import csv

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

query = ("SELECT * FROM filmes")

cursor.execute(query)
datas = cursor.fetchall() 

with open('arquivos_csv/exportados_filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['titulo', 'diretor', 'ano', 'genero', 'preco'])
    escritor.writerows(datas)

conn.commit()

cursor.close()
conn.close()