## Exercício de Casa 🏠 Gerenciando uma Videoteca com SQLite e CSV
#6-Remover um Filme:

import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Remover o filme com id 3
id_filme = 3
cursor.execute('''
    DELETE FROM filmes
    WHERE id = ?
''', (id_filme,))

# Confirmar a transação
conn.commit()

# Fechar a conexão
cursor.close()
conn.close()

print(f"Filme com id {id_filme} removido com sucesso!")
