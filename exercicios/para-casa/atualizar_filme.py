import sqlite3
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute("UPDATE filmes SET preco = ? WHERE titulo = ?", (55.90, "O Poderoso Chefão"))

conn.commit()
cursor.close()
conn.close()