#Crie o Banco de Dados e a Tabela:

import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        diretor TEXT NOT NULL,
        ano INT(4),
        genero TEXT,
        preco REAL
    )
''')

conn.commit()

cursor.close()
conn.close()