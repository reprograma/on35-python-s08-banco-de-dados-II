
#6. Remova um Filme:

#Escreva um script Python (chamado remover_filme.py) que remova um filme específico da tabela (por exemplo, remova o filme com id 3).



import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor =  conn.cursor()

#Delete um dado da banco de dados
cursor.execute("DELETE FROM filmes WHERE id = ?",(1,)) 

conn.commit()

cursor.close()
conn.close() 