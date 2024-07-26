import sqlite3

conn = sqlite3.connect('videoteca.db')
cur = conn.cursor()

# Atualiza o preço do filme com id 2
cur.execute('''
    UPDATE filmes
    SET preco = 15
    WHERE id = 2
''')

# Salva as alterações e fecha a conexão
conn.commit()
conn.close()