# 6. Remova um Filme:**

# Escreva um script Python (chamado `remover_filme.py`) que remova um filme específico da tabela (por exemplo, remova o filme com `id` 3).

import sqlite3

# Conectar ao banco de dados (ou criar um banco de dados)
conn = sqlite3.connect('banco_dados/videoteca.db')
cursor = conn.cursor()

id = 2

sql_query = (f'''
    SELECT titulo, genero, preco
    FROM filmes
    WHERE id = {id} 
''')

cursor.execute(sql_query)
resultado = cursor.fetchall() #significa buscar todos os registros que foi selecionada pelo select

#Remover um registro da tabela
cursor.execute("DELETE FROM filmes WHERE id = ?", (id,)) #dessa forma, precisa colocar a virgula mesmo sem um outro parametro

print(f'O filme com o id {id} foi deletado com sucesso: {resultado}')

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()