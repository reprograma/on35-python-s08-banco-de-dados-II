# Crie o Banco de Dados e a Tabela:

import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

#Criação da tabela
cursor.execute('''
CREATE TABLE IF NOT EXISTS filmes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    diretor TEXT,
    ano TEXT,
    genero TEXT,
    preco REAL
)
''')

conn.commit()

cursor.close()
conn.close()