#Consulte e Exiba os Dados:

import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('SELECT * FROM filmes')

filmes = cursor.fetchall()

print("Registros da tabela filmes:")
for filme in filmes:
    print(filme)

conn.close()