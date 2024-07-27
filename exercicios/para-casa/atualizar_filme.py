# * Escreva um script Python (chamado `atualizar_filme.py`) que atualize o preço de um filme específico 
# (por exemplo, aumente o preço do filme com `id` 2).

# ```python
import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Atualiza o valor do id 2
cursor.execute("UPDATE filmes SET preco = ? WHERE id = ?", (32.25, 2))

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()


# * **`UPDATE estudantes SET idade = ? WHERE nome = ?`**: 
# Atualiza a coluna "idade" na tabela "estudantes" para o valor `?` (23) 
# onde a coluna "nome" é igual a `?` (Bob).
