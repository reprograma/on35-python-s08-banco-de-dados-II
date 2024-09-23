# 6. Remova um Filme:

# Escreva um script Python (chamado remover_filme.py) que remova um filme 
# específico da tabela (por exemplo, remova o filme com id 3).

import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('videoteca.db')

# Criando um cursor
cursor = conn.cursor()

# ID do filme que queremos remover
id_filme = 3

# Remover o filme com o ID especificado

cursor.execute("""
    DELETE FROM filmes
    WHERE id = ?
""", (id_filme,))

# Salvando as mudanças no banco de dados
conn.commit()

# Verificando se a remoção foi bem-sucedida
print(f"Filme com ID {id_filme} removido com sucesso.")

# Fechando a conexão
cursor.close()
conn.close()
