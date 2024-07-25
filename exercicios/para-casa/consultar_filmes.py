# **4. Consulte e Exiba os Dados:**

# * Escreva um script Python (chamado `consultar_filmes.py`) que selecione e exiba todos os registros da tabela `filmes`.

import sqlite3

conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM FILMES")
filmes = cursor.fetchall()

for linha in filmes:
    print(linha)

cursor.close()
conn.close()
