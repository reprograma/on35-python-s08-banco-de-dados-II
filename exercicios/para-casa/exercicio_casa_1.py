# 1. Crie o Banco de Dados e a Tabela:
import sqlite3

conn = sqlite3.connect('videoteca.db')

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    diretor TEXT NOT NULL,
    ano INTERGER,
    genero TEXT NOT NULL,
    preco REAL
)
""")    

# 2. Crie o Arquivo CSV:
import csv

nome_arquivo = 'filmes.csv'

colunas = ['titulo', 'diretor', 'ano', 'genero', 'preco']

filmes = [
        ['O Poderoso Chefão', 'Francis Ford Coppola', 1972, 'Drama', 25.99],
        ['O Senhor dos Anéis: A Sociedade do Anel', 'Peter Jackson', 2001, 'Fantasia', 30.99],
        ['A Origem', 'Christopher Nolan', 2010, 'Ficção Científica', 19.99],
        ['A Vida de Brian','Terry Gilliam', 1979, 'Comédia', 15.99],
        ['Pulp Fiction', 'Quentin Tarantino', 1994, 'Crime', 22.99]
]

with open(nome_arquivo, 'w', newline='', encoding='UTF-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['titulo', 'diretor', 'ano', 'genero', 'preco'])
    escritor.writerows(filmes)

#3. Importe os Dados para o Banco de Dados:

import sqlite3
import csv
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM filmes")    
with open('filmes.csv', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)  # Pula o cabeçalho
    for linha in leitor:
        cursor.execute("INSERT INTO filmes (titulo, diretor, ano, genero, preco) VALUES (?, ?, ?, ?, ?)", (linha[1], linha[2], linha[3], linha[4], linha[5]))
        
conn.commit()
cursor.close()
conn.close()






