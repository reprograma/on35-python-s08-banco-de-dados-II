import sqlite3
import csv

# Conectando ao banco de dados (cria se não existir)
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Criando a tabela (se já existir, será ignorada)
cursor.execute('''
    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        diretor TEXT,
        ano INTEGER,
        genero TEXT,
        preco REAL
    )
''')

# Abrindo o arquivo CSV
# with open('filmes.csv', 'r') as csvfile:
#     reader = csv.DictReader(csvfile)

import csv
filmes = [
    ["O Poderoso Chefão", "Francis Ford Coppola", 1972, "Crime", 25.99],
    ["O Senhor dos Anéis: A Sociedade do Anel", "Peter Jackson", 2001, "Fantasia", 30.99],
    ["Pulp Fiction", "Quentin Tarantino", 1994, "Crime", 19.99],
    ["O Iluminado", "Stanley Kubrick", 1980, "Terror", 15.99],
    ["Matrix", "Lana Wachowski", 1999, "Ação", 22.99]
]

with open('filmes.csv', 'w', newline='', encoding='utf-8') as csvfile:
   
   escritor = csv.writer(csvfile)
   escritor.writerow(['titulo', 'diretor', 'ano', 'genero', 'preco'])
   escritor.writerows(filmes)

with open('filmes.csv', 'r', newline='', encoding='utf-8') as csvfile:
    leitor = csv.reader(csvfile)
    next(leitor)
    cursor.executemany('INSERT INTO filmes (titulo, diretor, ano, genero, preco) VALUES (?, ?, ?, ?, ?)', leitor)

    
    # Inserindo os dados na tabela
    # for row in reader:
    #     cursor.execute('''
    #         INSERT INTO filmes (titulo, diretor, ano, genero, preco)
    #         VALUES (:titulo, :diretor, :ano, :genero, :preco)
    #     ''', row)

# Confirmando as alterações

conn.commit()
conn.close()
