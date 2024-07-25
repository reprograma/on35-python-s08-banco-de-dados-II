import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS filmes (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               titulo TEXT NOT NULL,
               diretor TEXT,
               ano INTEGER,
               genero TEXT,
               preco REAL
               )
''')


conn.commit()

cursor.close()
conn.close()
