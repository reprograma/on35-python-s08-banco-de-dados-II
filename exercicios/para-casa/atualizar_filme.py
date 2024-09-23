# Exercício 5 >> Atualize os Dados:
# Escreva um script Python (chamado atualizar_filme.py) que atualize o preço de um filme específico 
# (por exemplo, aumente o preço do filme com id 2).

import sqlite3

# Conectando ao banco de dados
conn = sqlite3.connect('videoteca.db')

# Criando um cursor
cursor = conn.cursor()

# Atualizando o preço do filme com id 2
novo_preco = 19.99  # Novo preço para o filme
id_filme = 2  # ID do filme que queremos atualizar

cursor.execute("""
    UPDATE filmes
    SET preco = ?
    WHERE id = ?
""", (novo_preco, id_filme))

# Salvando as mudanças no banco de dados
conn.commit()

# Verificando se a alteração foi bem-sucedida
print(f"Preço do filme com ID {id_filme} atualizado para {novo_preco}.")

# Fechando a conexão
cursor.close()
conn.close()
