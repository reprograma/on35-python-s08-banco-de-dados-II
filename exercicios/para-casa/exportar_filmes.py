import csv
import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute("SELECT titulo, genero FROM filmes")
dados = cursor.fetchall()

with open('exportados.csv', 'w', newline='') as arquivo_csv:
    escritor_csv = csv.writer(arquivo_csv)
    
    escritor_csv.writerow(['titulo', 'genero'])
    
    escritor_csv.writerows(dados)

cursor.close()
conn.close()