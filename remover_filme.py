import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

filme_id = 3

cursor.execute('DELETE FROM filmes WHERE id = ?', (filme_id,))

conn.commit()
conn.close()

print(f"Filme com ID {filme_id} removido com sucesso!")
