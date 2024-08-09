import sqlite3
import csv 

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute("""
               CREATE TABLE IF NOT EXISTS filmes(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                titulo TEXT NOT NULL,
                diretor INTEGER NOT NULL,
                lancamento INTEGER NOT NULL,
                genero TEXT NOT NULL,
                preco REAL NOT NULL
                )    
               """)
with open('filmes.csv',  newline = '', encoding = 'UTF-8' ) as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor) 
    for linha in leitor:
       cursor.execute("INSERT INTO filmes (titulo, diretor, lancamento, genero, preco) values (?, ?, ?, ?, ?)", (linha[1], linha[2], linha[3], linha[4], linha[5]))  

conn.commit()
cursor.close()
conn.close()
