# **5. Atualize os Dados:**

# * Escreva um script Python (chamado `atualizar_filme.py`) que atualize o preço de um filme específico (por exemplo, aumente o preço do filme com `id` 2).

import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor =  conn.cursor()
# Prepare a consulta com parâmetros nomeados
consulta =("UPDATE filmes SET preco = :preco WHERE id = :id")
# Valores para os parâmetros (dicionário com valores corretos)
valores = {"preco": 28.55 , "id": 2}
cursor.execute(consulta, valores)
#cursor.execute("UPDATE filmes SET preco = ? WHERE id = ?",(28.50, id)) outra forma de atualizar

conn.commit()

cursor.close()
conn.close() 