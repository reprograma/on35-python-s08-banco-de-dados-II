#Atualize os Dados:

import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute("UPDATE filmes SET preco = ? WHERE id = 2", (26.99))

query = ('''
    SELECT titulo, genero, preco
    FROM filmes
    WHERE id = 2 
''')

cursor.execute(query)

resultado = cursor.fetchall() 

conn.commit()

cursor.close()
conn.close()