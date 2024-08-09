import sqlite3
conn = sqlite3.connect('videoteca.db')

cursor = conn.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS filmes(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                titulo TEXT NOT NULL,
                diretor INTEGER NOT NULL,
                lancamento INTEGER NOT NULL,
                genero TEXT NOT NULL,
                preco REAL NOT NULL
                )    
               """)

conn.commit()
cursor.close()
conn.close()