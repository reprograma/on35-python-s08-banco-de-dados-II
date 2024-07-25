#Importe os Dados para o Banco de Dados:


import sqlite3
import csv

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

with open('arquivos_csv/filmes.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  
    for linha in leitor:
        insert_datas = "INSERT INTO filmes (titulo, diretor, ano, genero, preco) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(insert_datas,(linha[0],linha[1],linha[2],linha[3],linha[4]))

query = ("SELECT * FROM filmes")

cursor.execute(query)
dados = cursor.fetchall() 

conn.commit()

cursor.close()
conn.close()