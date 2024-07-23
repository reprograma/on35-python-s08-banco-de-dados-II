import sqlite3

# Conexão com o banco de dados
conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# Cria a tabela estudantes se ela não existir
cursor.execute("""
CREATE TABLE IF NOT EXISTS estudantes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade INTEGER NOT NULL
)
""")

# Lista de estudantes para inserir
estudantes = [
    ('Alice', 21),
    ('Bob', 22),
    ('Charlie', 23)
]
# Insere vários estudantes de uma vez
cursor.executemany("INSERT INTO estudantes (nome, idade) VALUES (?, ?)", estudantes)



# Atualiza a idade de Bob para 23
cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?", (23, 'Bob'))

# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()

#parte3
# cursor.execute("SELECT * FROM estudantes"): Executa a consulta SQL para selecionar todos os registros da tabela "estudantes".
# registros = cursor.fetchall(): Recupera todos os registros da consulta em uma lista de tuplas.
# for registro in registros:: Itera sobre os registros e imprime cada um deles.

#parte 4
cursor.execute("UPDATE estudantes SET idade = ? WHERE nome = ?",(23,"Bob"))                           
#parte5
# Remove o estudante Charlie
cursor.execute("DELETE FROM estudantes WHERE nome = ?", ('Charlie',))

cursor.execute("DELETE FROM estudantes WHERE nome = 'Charlie'")


# Salva as alterações no banco de dados
conn.commit()
cursor.execute("DELETE FROM estudantes WHERE nome = 'Charlie'")


# Salva as alterações no banco de dados
conn.commit()

# Fecha a conexão
cursor.close()
conn.close()
