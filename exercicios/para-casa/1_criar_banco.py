# Exercício de Casa 🏠 

## Gerenciando uma Videoteca com SQLite e CSV

# 1. Crie o Banco de Dados e a Tabela:

# Crie um banco de dados SQLite chamado `videoteca.db`.
# Crie uma tabela chamada `filmes` com as seguintes colunas:
#     `id` (INTEGER, chave primária, autoincremento)
#     `titulo` (TEXT)
#     `diretor` (TEXT)
#     `ano` (INTEGER)
#     `genero` (TEXT)
#     `preco` (REAL) 

import sqlite3

# Conectar ao banco de dados (ou criar um banco de dados)
conn = sqlite3.connect('banco_dados/videoteca.db')
cursor = conn.cursor()

# Criar a tabela de filmes
create_table_movies = ('''
    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        diretor TEXT NOT NULL,
        ano INT(4),
        genero TEXT,
        preco REAL
    )
''')

cursor.execute(create_table_movies)

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()