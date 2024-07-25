# 4. Consulte e Exiba os Dados:

# Escreva um script Python (chamado consultar_filmes.py) 
# que selecione e exiba todos os registros da tabela filmes.

import sqlite3 

conn=sqlite3.connect ('videoteca.db') # ou filmes.csv?
cursor=conn.cursor()

cursor.execute("SELECT * FROM filmes")
registros = cursor.fetchall()

for filmes in registros:
    print (filmes)


cursor.close()
conn.close()
