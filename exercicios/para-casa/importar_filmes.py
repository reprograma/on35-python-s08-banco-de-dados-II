import sqlite3
import csv

conn=sqlite3.connect("videoteca.db")
cursor=conn.cursor()

with open('filmes.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  # Pula a primeira linha que é o cabeçalho
    for linha in leitor: #itera sobre as linhas
        cursor.execute("INSERT INTO filmes (titulo, diretor, ano, genero, preco) VALUES (?, ?, ?, ?, ?)", (linha[1], linha[2], linha[3], linha[4], linha[5])) #insere dados

cursor.execute('SELECT * FROM filmes')
       
conn.commit()
cursor.close()
conn.close()
       
