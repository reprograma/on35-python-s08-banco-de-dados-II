# 4. Consulte e Exiba os Dados:**

# Escreva um script Python (chamado `consultar_filmes.py`) que selecione e exiba todos os registros da tabela `filmes`.

import sqlite3

# Conectar ao banco de dados (ou criar um banco de dados)
conn = sqlite3.connect('banco_dados/videoteca.db')
cursor = conn.cursor()

sql_query = ('''
    SELECT titulo, diretor, ano, genero, preco
    FROM filmes
''')

cursor.execute(sql_query)
resultado = cursor.fetchall() #significa buscar todos os registros que foi selecionada pelo select
print("Filmes da videoteca: ")
for linha in resultado:
    print(linha)

# Fecha a conexão
cursor.close()
conn.close()