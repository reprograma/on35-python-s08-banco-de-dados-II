import sqlite3

conn = sqlite3.connect('videoteca.bd')
cursor = conn.cursor()

cursor.execute('''
             CREATE TABLE filmes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT,
        diretor TEXT,
        ano INTEGER,
        genero TEXT,
        preco REAL
    )
 ''')

conn.commit()
conn.close()

