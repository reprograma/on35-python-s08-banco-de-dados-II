# **1. Crie o Banco de Dados e a Tabela:**

# * Crie um banco de dados SQLite chamado `videoteca.db`.

import sqlite3

conn = sqlite3.connect('videoteca.db')

cursor = conn.cursor()


# * Crie uma tabela chamada `filmes` com as seguintes colunas:
#     * `id` (INTEGER, chave primária, autoincremento)
#     * `titulo` (TEXT)
#     * `diretor` (TEXT)
#     * `ano` (INTEGER)
#     * `genero` (TEXT)
#     * `preco` (REAL)  

cursor.execute("""
    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        titulo TEXT NOT NULL,
        diretor TEXT NOT NULL,
        ano INTEGER NOT NULL, 
        genero TEXT NOT NULL,
        preco REAL NOT NULL 
    )
""")
conn.commit()
conn.close()

# **2. Crie o Arquivo CSV:**

# * Crie um arquivo CSV chamado `filmes.csv` com as seguintes colunas:
#     * `titulo`
#     * `diretor`
#     * `ano`
#     * `genero`
#     * `preco` 
# * Adicione pelo menos 5 filmes diferentes ao arquivo `filmes.csv`.

import csv

dados_filmes = [
    ["Central do Brasil", "Walter Salles", 1998, "Drama", 29.99],
    ["A Hora da Estrela", "Suzana Amaral", 1985, "Drama", 15.98],
    ["Que Horas ela Volta?", "Anna Muylaert", 2015, "Comédia/Drama", 24.99],
    ["Cidade Baixa", "Sérgio Machado", 2005, "Drama", 27.50],
    ["Cidade dos Homens", "Paulo Morelli", 2007, "Ação/Thriller", 29.99]
]

with open('filmes.csv', 'w', newline= '', encoding='utf-8') as csvfile:
    escritor = csv.writer(csvfile)
    escritor.writerow(['titulo', 'diretor', 'ano', 'genero', 'preco'])
    escritor.writerows(dados_filmes)


