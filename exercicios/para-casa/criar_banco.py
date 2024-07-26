import sqlite3

#Conect to data base
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

#Create movies table
cursor.execute('''
    CREATE TABLE filmes (
        id INTERGER PRIMARY KEY AUTOINCREMENT,
        título TEXT,
        diretor TEXT,
        ano INTERGER,
        genero TEXT,
        preco REAL
    )
''')

#Save changes
conn.commit()
conn.close()

