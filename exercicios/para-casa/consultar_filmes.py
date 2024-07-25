#Consulte e Exiba os Dados:

import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

query = ('''
    SELECT titulo, diretor, ano, genero, preco
    FROM filmes
''')

cursor.execute(query)
resultado = cursor.fetchall() 

for linha in resultado:
    print(linha)

cursor.close()
conn.close()