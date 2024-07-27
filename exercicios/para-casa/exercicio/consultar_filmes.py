import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM filmes')
filmes = cursor.fetchall()

for filme in filmes:
    print(filme)

conn.close()
