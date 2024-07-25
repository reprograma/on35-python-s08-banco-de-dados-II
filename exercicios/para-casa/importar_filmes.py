# 3. Importe os Dados para o Banco de Dados:

# Escreva um script Python (chamado importar_filmes.py) que 
# leia os dados do filmes.csv e 
# os insira na tabela filmes no banco de dados videoteca.db.

import sqlite3
import csv

conn = sqlite3.connect('videoteca.db')
cursor=conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS filmes (
               id INTERGER PRIMARY KEY AUTOINCREMENT,
               titulo TEXT NOT NULL,
               diretor TEXT NOT NULL,
               ano INTERGER NOT NULL,
               genero TEXT NOT NULL,
               preco REAL NOT NULL
            )    
""")
with open ('filmes.csv', newline='', encoding='utf-8') as csvfile:
    leitor=csv.reader(csvfile)
    next(leitor)
    for linha in leitor:
        insert_datas = "INSERT INTO filmes (id,titulo,diretor,ano,genero,preco) VALUES (?,?,?,?,?, ?)" # duvidas aqui
        cursor.execute(insert_datas,(linha[0], linha [1], linha[2], linha[3], linha[4], linha[5]))  # duvidas aqui


cursor.execute("SELECT * FROM filmes")
filmes = cursor.fetchall() # fetchall vai buscar todos os registros que foi selecionada pelo select

print('Filmes importados para para o banco de dados Videoteca!')       

conn.commit()
cursor.close()
conn.close()