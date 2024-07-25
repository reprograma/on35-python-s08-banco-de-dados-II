# 1. Crie o Banco de Dados e a Tabela:

# Crie um banco de dados SQLite chamado videoteca.db.
# Crie uma tabela chamada filmes com as seguintes colunas:
# id (INTEGER, chave primária, autoincremento)
# titulo (TEXT)
# diretor (TEXT)
# ano (INTEGER)
# genero (TEXT)
# preco (REAL)

import sqlite3

conn = sqlite3.connect ("videoteca.db")
cursor = conn.cursor()

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

cursor.close()
conn.close()