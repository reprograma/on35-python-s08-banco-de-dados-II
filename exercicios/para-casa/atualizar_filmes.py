## Exercício de Casa 🏠 Gerenciando uma Videoteca com SQLite e CSV
#5-Atualizar os Dados:

import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('videoteca.db')
cursor = conn.cursor()

# Atualizar o preço do filme com id 2
novo_preco = 23.99
id_filme = 2
cursor.execute('''
    UPDATE filmes
    SET preco = ?
    WHERE id = ?
''', (novo_preco, id_filme))

# Confirmar a transação
conn.commit()

# Fechar a conexão
cursor.close()
conn.close()

print(f"Preço do filme com id {id_filme} atualizado para {novo_preco}!")
