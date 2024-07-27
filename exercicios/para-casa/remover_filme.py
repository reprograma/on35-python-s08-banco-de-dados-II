# **6. Remova um Filme:**

# * Escreva um script Python (chamado `remover_filme.py`) que remova um filme específico da tabela 
# (por exemplo, remova o filme com `id` 3).

import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Remove o filme id 3
cursor.execute("DELETE FROM filmes WHERE id = ?", (3,))

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()