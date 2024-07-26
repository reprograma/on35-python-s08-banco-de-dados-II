#Atualize os Dados:

import sqlite3

conn - sqlite3.connect('videoteca.db')
cursor = conn.cursor()

id_filme = 2
novo_preco = 29.99

cursor.execute('''
    UPDATE filmes
    SET preco = ?
    WHERE id = ?
''', (novo_preco, id_filme))

conn.commit()
conn.close()