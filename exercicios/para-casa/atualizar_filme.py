import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute('''
    UPDATE filmes
    SET preco = 15.99
    WHERE id = 2
''')
conn.commit()
conn.close()
            