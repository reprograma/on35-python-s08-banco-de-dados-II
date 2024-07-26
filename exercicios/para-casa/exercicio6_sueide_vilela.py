#Remova um Filme

import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

id_filme = 3

cursor.execute('''
    DELETE FROM filmes
    WHERE id = ?
''', (id_filme,))

conn.commit()
conn.close()