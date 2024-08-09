import sqlite3
import csv
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM filmes")
dados = cursor.fetchall()
with open('exportados_filmes.csv', 'w', newline = '', encoding = 'UTF-8' ) as csvfile:
     escritor = csv.writer(csvfile) 
     escritor.writerow(['id', 'titulo', 'diretor', 'lancamento', 'genero', 'preco']) 
     escritor.writerows(dados)

conn.commit()
cursor.close()
conn.close()
