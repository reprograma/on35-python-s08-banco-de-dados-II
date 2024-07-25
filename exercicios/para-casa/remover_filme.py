# 6. Remova um Filme:

# Escreva um script Python (chamado remover_filme.py) que remova 
# um filme específico da tabela (por exemplo, remova o filme com id 3).

import sqlite3

conn=sqlite3.connect ('videoteca.db') 
cursor=conn.cursor()

cursor.execute("DELETE FROM filmes WHERE id=?", (3,))
print('O filme foi APAGADO com sucesso')

cursor.execute("INSERT INTO filmes (id,titulo,diretor,ano,genero,preco) VALUES (3,'O jogo da imitação','Morten Tyldum','2014','Thriller/Guerra',5.00)")
print('O filme foi inserido com sucesso')

conn.commit ()
cursor.close()
conn.close()