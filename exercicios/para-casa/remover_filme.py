#Remova um Filme:

import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

id = 3

query = ('''
    SELECT titulo, genero, preco
    FROM filmes
    WHERE id = {id} 
''')

cursor.execute(query)
resultado = cursor.fetchall() 

cursor.execute("DELETE FROM filmes WHERE id = ?", (id,)) 

print(f'O filme de id {id} foi deletado com sucesso: {resultado}!!')

conn.commit()

cursor.close()
conn.close()