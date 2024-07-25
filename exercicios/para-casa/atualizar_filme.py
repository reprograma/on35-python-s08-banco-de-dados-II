# **5. Atualize os Dados:**

# * Escreva um script Python (chamado `atualizar_filme.py`) que atualize o preço de um filme específico (por exemplo, aumente o preço do filme com `id` 2).

import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute("UPDATE filmes SET preco = ? WHERE titulo = ?", (54.90, 'A Hora da Estrela'))


conn.commit()

cursor.close()
conn.close()

